#!/usr/bin/env python3
import argparse
import json
import os
import sys
import time
from pathlib import Path

import requests

API_BASE = "https://api.openai.com/v1"


def fail(message: str, response: requests.Response | None = None) -> None:
    print(f"\nERROR: {message}", file=sys.stderr)
    if response is not None:
        print(f"HTTP {response.status_code}", file=sys.stderr)
        try:
            print(json.dumps(response.json(), ensure_ascii=False, indent=2), file=sys.stderr)
        except Exception:
            print(response.text, file=sys.stderr)
    sys.exit(1)


def request_json(method, url, headers=None, **kwargs):
    try:
        response = requests.request(
            method,
            url,
            headers=headers,
            timeout=120,
            **kwargs,
        )
    except requests.RequestException as e:
        fail(f"HTTP request failed: {e}")

    if not response.ok:
        fail(f"{method} {url} failed", response)

    try:
        return response.json()
    except ValueError:
        fail(f"{method} {url} returned non-JSON response", response)


def create_vector_store(headers, name: str) -> str:
    data = request_json(
        "POST",
        f"{API_BASE}/vector_stores",
        headers={**headers, "Content-Type": "application/json"},
        json={"name": name},
    )

    vector_store_id = data.get("id")
    if not vector_store_id:
        fail(f"Vector Store response has no id: {data}")

    return vector_store_id


def upload_file(headers, path: Path) -> str:
    # Do not set Content-Type manually here: requests builds multipart/form-data.
    upload_headers = {"Authorization": headers["Authorization"]}

    with path.open("rb") as f:
        data = request_json(
            "POST",
            f"{API_BASE}/files",
            headers=upload_headers,
            data={"purpose": "user_data"},
            files={"file": (path.name, f, "text/markdown")},
        )

    file_id = data.get("id")
    if not file_id:
        fail(f"File upload response has no id for {path}: {data}")

    return file_id


def attach_file(headers, vector_store_id: str, file_id: str) -> str:
    data = request_json(
        "POST",
        f"{API_BASE}/vector_stores/{vector_store_id}/files",
        headers={**headers, "Content-Type": "application/json"},
        json={"file_id": file_id},
    )

    vector_file_id = data.get("id")
    if not vector_file_id:
        fail(f"Attach response has no id for {file_id}: {data}")

    return vector_file_id


def wait_until_indexed(
    headers,
    vector_store_id: str,
    vector_file_id: str,
    poll_interval: float,
    max_wait: int,
) -> None:
    started = time.time()

    while True:
        data = request_json(
            "GET",
            f"{API_BASE}/vector_stores/{vector_store_id}/files/{vector_file_id}",
            headers=headers,
        )

        status = data.get("status", "unknown")

        if status == "completed":
            return

        if status in {"failed", "cancelled"}:
            error = data.get("last_error")
            fail(
                f"Vector indexing ended with status={status}; "
                f"file={vector_file_id}; last_error={error}"
            )

        if time.time() - started > max_wait:
            fail(
                f"Timed out waiting for indexing of {vector_file_id} "
                f"after {max_wait} seconds"
            )

        print(f"      indexing: {status}", end="\r", flush=True)
        time.sleep(poll_interval)


def collect_md_files(folder: Path, recursive: bool) -> list[Path]:
    pattern = "**/*.md" if recursive else "*.md"
    return sorted(
        (p for p in folder.glob(pattern) if p.is_file()),
        key=lambda p: str(p).lower(),
    )


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Upload all Markdown files from a folder to one OpenAI Vector Store "
            "sequentially and print vector_store_ids."
        )
    )
    parser.add_argument(
        "folder",
        nargs="?",
        default=".",
        help="Folder containing .md files (default: current directory)",
    )
    parser.add_argument(
        "--name",
        default="Markdown Knowledge Base",
        help="Vector Store name",
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Read only .md files directly in the folder, without subfolders",
    )
    parser.add_argument(
        "--poll-interval",
        type=float,
        default=2.0,
        help="Indexing status polling interval in seconds (default: 2)",
    )
    parser.add_argument(
        "--max-wait",
        type=int,
        default=1800,
        help="Maximum indexing wait per file in seconds (default: 1800)",
    )
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        fail(
            "OPENAI_API_KEY is not set.\n"
            'Linux/macOS: export OPENAI_API_KEY="sk-..."\n'
            'PowerShell:  $env:OPENAI_API_KEY="sk-..."'
        )

    folder = Path(args.folder).expanduser().resolve()
    if not folder.exists() or not folder.is_dir():
        fail(f"Folder does not exist or is not a directory: {folder}")

    md_files = collect_md_files(folder, recursive=not args.no_recursive)
    if not md_files:
        fail(f"No .md files found in: {folder}")

    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    print(f"Folder: {folder}")
    print(f"Markdown files found: {len(md_files)}")
    print(f"Creating Vector Store: {args.name!r}")

    vector_store_id = create_vector_store(headers, args.name)

    print(f"Vector Store created: {vector_store_id}")
    print()

    uploaded = []

    for index, path in enumerate(md_files, 1):
        relative = path.relative_to(folder)
        size_kb = path.stat().st_size / 1024

        print(f"[{index}/{len(md_files)}] {relative} ({size_kb:.1f} KB)")

        print("    1) Uploading file...")
        file_id = upload_file(headers, path)
        print(f"       file_id: {file_id}")

        print("    2) Attaching to Vector Store...")
        vector_file_id = attach_file(headers, vector_store_id, file_id)
        print(f"       vector_file_id: {vector_file_id}")

        print("    3) Waiting for indexing...")
        wait_until_indexed(
            headers,
            vector_store_id,
            vector_file_id,
            args.poll_interval,
            args.max_wait,
        )
        print("       status: completed" + " " * 20)

        uploaded.append(
            {
                "path": str(relative),
                "file_id": file_id,
                "vector_file_id": vector_file_id,
            }
        )
        print()

    result = {
        "vector_store_ids": [vector_store_id],
        "files_count": len(uploaded),
        "files": uploaded,
    }

    print("=" * 70)
    print("DONE")
    print(json.dumps({"vector_store_ids": [vector_store_id]}, ensure_ascii=False, indent=2))
    print()
    print(f"VECTOR_STORE_ID={vector_store_id}")
    print("=" * 70)

    # Also save a reusable local result file next to the script's current directory.
    result_file = Path("vector_store_result.json")
    result_file.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Saved details to: {result_file.resolve()}")


if __name__ == "__main__":
    main()
