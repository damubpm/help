# DamuBPM REST API + Lua

[← Вернуться на Главную](index.html)

Практический справочник по созданию REST API на Lua в DamuBPM.

---

## Содержание

1. [Быстрый старт](#быстрый-старт)
2. [URL и методы](#url-и-методы)
3. [Объект request](#объект-request)
4. [Формирование ответа](#формирование-ответа)
5. [Настройки REST-сервиса](#настройки-rest-сервиса)
6. [Примеры Lua](#примеры-lua)
7. [Примеры вызова](#примеры-вызова)
8. [Авторизация и сессия](#авторизация-и-сессия)
9. [Async и no_parallel](#async-и-no_parallel)
10. [Headers и CORS](#headers-и-cors)
11. [Рекомендуемые шаблоны](#рекомендуемые-шаблоны)
12. [Чек-лист](#чек-лист)

---

# Быстрый старт

REST-сервисы доступны по адресу:

```text
/restapi/services/run/<code>
```

Например, если код сервиса:

```text
api/v1/customer/create
```

то URL будет:

```text
/restapi/services/run/api/v1/customer/create
```

Поддерживаемые методы:

```text
GET
POST
PUT
OPTIONS
```

Простейший Lua-сервис:

```lua
output = {
    success = true,
    message = "Hello from DamuBPM"
}
```

---

# URL и методы

## GET

```http
GET /restapi/services/run/customer/get?id=123
```

```lua
local id = request.get.id

output = {
    success = true,
    id = id
}
```

## POST

```http
POST /restapi/services/run/customer/create
Content-Type: application/json

{
    "title": "ТОО Test",
    "email": "info@test.kz"
}
```

```lua
local input = request.input

output = {
    success = true,
    title = input.title,
    email = input.email
}
```

## PUT

```http
PUT /restapi/services/run/customer/update?id=123
Content-Type: application/json

{
    "title": "Новое название"
}
```

```lua
local id = tonumber(request.get.id)
local input = request.input

output = {
    success = true,
    id = id,
    title = input.title
}
```

---

# Объект request

В каждом Lua REST-сервисе доступен глобальный объект `request`.

| Поле | Назначение | Пример |
|---|---|---|
| `request.input` | JSON body как Lua-таблица | `request.input.title` |
| `request.input_raw` | исходное тело запроса строкой | `request.input_raw` |
| `request.get` | query/form параметры | `request.get.id` |
| `request.header` | входящие HTTP headers | `request.header["X-Api-Key"]` |
| `request.user_id` | ID текущего пользователя, строка | `tonumber(request.user_id)` |
| `request.last_user_id` | предыдущий пользователь | `request.last_user_id` |
| `request.lang` | язык | `request.lang` |
| `request.anonymous_session_id` | ID анонимной сессии | `request.anonymous_session_id` |
| `request.host` | HTTP Host | `request.host` |
| `request.method` | HTTP method | `request.method` |
| `request.RemoteAddr` | удалённый адрес | `request.RemoteAddr` |
| `request.NTLM_DOMAIN` | NTLM domain | `request.NTLM_DOMAIN` |
| `request.NTLM_USER` | NTLM user | `request.NTLM_USER` |
| `request.NTLM_HOST` | NTLM host | `request.NTLM_HOST` |

`request.user_id` удобно сразу преобразовывать:

```lua
local userId = tonumber(request.user_id)
```

---

# Формирование ответа

Основные глобальные переменные:

```lua
output
http_response_code
header
```

Пример:

```lua
http_response_code = 200

header = {
    ["X-Service"] = "customer",
    ["X-Version"] = "1"
}

output = {
    success = true,
    data = {
        id = 123,
        title = "Test"
    }
}
```

## output

Строковый ответ:

```lua
output = "OK"
```

JSON-подобный ответ:

```lua
output = {
    success = true,
    id = 123
}
```

## HTTP status

```lua
http_response_code = 200
```

```lua
http_response_code = 201
```

```lua
http_response_code = 400
```

```lua
http_response_code = 401
```

```lua
http_response_code = 404
```

```lua
http_response_code = 409
```

## Response headers

```lua
header = {
    ["X-Service"] = "customer",
    ["Cache-Control"] = "no-store"
}
```

---

# Настройки REST-сервиса

| Настройка | Назначение |
|---|---|
| `code` | код сервиса и часть URL |
| `body` | Lua-код сервиса |
| `res_content_type_id` | тип ответа / MIME |
| `is_public` | публичный доступ |
| `only_auth` | доступ только для авторизованных пользователей |
| `cut_status_info` | возвращать непосредственно `output` |
| `is_redirect_output` | использовать `output` как URL редиректа |
| `no_parallel` | запретить параллельный запуск одного сервиса |

Для обычного JSON API удобно:

```text
Content-Type = application/json
cut_status_info = 1
```

---

# Примеры Lua

## 1. Hello

```lua
output = {
    success = true,
    message = "Hello from DamuBPM"
}
```

## 2. GET параметр

```lua
local id = request.get.id

output = {
    id = id
}
```

## 3. Несколько GET параметров

```lua
local page = request.get.page or "1"
local limit = request.get.limit or "20"

output = {
    page = tonumber(page),
    limit = tonumber(limit)
}
```

## 4. Обязательный GET параметр

```lua
local id = request.get.id

if id == nil or id == "" then
    http_response_code = 400
    output = {
        success = false,
        error = "id is required"
    }
    return
end

output = {
    success = true,
    id = id
}
```

## 5. Числовой GET параметр

```lua
local id = tonumber(request.get.id)

if id == nil then
    http_response_code = 400
    output = {
        success = false,
        error = "id must be a number"
    }
    return
end

output = {
    success = true,
    id = id
}
```

## 6. Определить HTTP method

```lua
output = {
    method = request.method
}
```

## 7. Host

```lua
output = {
    host = request.host
}
```

## 8. RemoteAddr

```lua
output = {
    remote_addr = request.RemoteAddr
}
```

## 9. POST JSON

```lua
local input = request.input

output = {
    title = input.title,
    email = input.email
}
```

## 10. Проверка body

```lua
local input = request.input

if input == nil then
    http_response_code = 400
    output = {
        success = false,
        error = "Request body required"
    }
    return
end

output = {
    success = true
}
```

## 11. Обязательное поле

```lua
local input = request.input

if input.title == nil or input.title == "" then
    http_response_code = 400
    output = {
        success = false,
        error = "title is required"
    }
    return
end

output = {
    success = true,
    title = input.title
}
```

## 12. Несколько обязательных полей

```lua
local input = request.input

if not input.title or not input.email then
    http_response_code = 400
    output = {
        success = false,
        error = "title and email are required"
    }
    return
end

output = {
    success = true
}
```

## 13. Число из JSON

```lua
local amount = tonumber(request.input.amount)

if amount == nil then
    http_response_code = 400
    output = {
        success = false,
        error = "amount must be numeric"
    }
    return
end

output = {
    success = true,
    amount = amount
}
```

## 14. Вложенный объект

```lua
local input = request.input
local customer = input.customer or {}

output = {
    success = true,
    customer = {
        title = customer.title,
        email = customer.email
    }
}
```

## 15. Исходный body

```lua
output = {
    raw = request.input_raw
}
```

## 16. Echo endpoint

```lua
output = {
    success = true,
    received = request.input,
    method = request.method
}
```

## 17. PUT update

```lua
local id = tonumber(request.get.id)
local input = request.input

if id == nil then
    http_response_code = 400
    output = {
        success = false,
        error = "id is required"
    }
    return
end

output = {
    success = true,
    updated = {
        id = id,
        title = input.title
    }
}
```

## 18. Частичное изменение

```lua
local input = request.input

output = {
    success = true,
    patch = {
        title = input.title,
        email = input.email
    }
}
```

## 19. HTTP 201

```lua
http_response_code = 201

output = {
    success = true,
    id = 123
}
```

## 20. HTTP 400

```lua
http_response_code = 400

output = {
    success = false,
    error = "Bad Request"
}
```

## 21. HTTP 401

```lua
http_response_code = 401

output = {
    success = false,
    error = "Unauthorized"
}
```

## 22. HTTP 404

```lua
http_response_code = 404

output = {
    success = false,
    error = "Not found"
}
```

## 23. HTTP 409

```lua
http_response_code = 409

output = {
    success = false,
    error = "Conflict"
}
```

## 24. Свои response headers

```lua
header = {
    ["X-Service"] = "customer",
    ["X-Version"] = "1"
}

output = {
    success = true
}
```

## 25. X-Api-Key

```lua
local apiKey = request.header["X-Api-Key"]

if not apiKey or apiKey == "" then
    http_response_code = 401
    output = {
        success = false,
        error = "X-Api-Key required"
    }
    return
end

output = {
    success = true
}
```

## 26. Authorization header

```lua
local authorization = request.header.Authorization

output = {
    has_authorization = authorization ~= nil
}
```

## 27. Текущий user_id

```lua
local userId = tonumber(request.user_id)

output = {
    success = true,
    user_id = userId
}
```

## 28. last_user_id

```lua
output = {
    current_user_id = tonumber(request.user_id),
    last_user_id = request.last_user_id
}
```

## 29. Язык

```lua
local lang = request.lang or "ru"

output = {
    success = true,
    lang = lang
}
```

## 30. Анонимная сессия

```lua
output = {
    anonymous_session_id = request.anonymous_session_id
}
```

## 31. Login

```lua
local userId = 123
local deviceToken = ""

local errText, errCode = Login(userId, deviceToken)

if errCode ~= 0 then
    http_response_code = 401
    output = {
        success = false,
        error = errText
    }
    return
end

output = {
    success = true
}
```

## 32. LoginAs

```lua
local userId = 123
local lastUserId = 10
local deviceToken = ""

local errText, errCode = LoginAs(
    userId,
    lastUserId,
    deviceToken
)

if errCode ~= 0 then
    http_response_code = 401
    output = {
        success = false,
        error = errText
    }
    return
end

output = {
    success = true
}
```

## 33. SendEmailOTP

```lua
local email = request.input.email
local errText, errCode = SendEmailOTP(email)

if errCode ~= 0 then
    http_response_code = 400
    output = {
        success = false,
        error = errText
    }
    return
end

output = {
    success = true
}
```

## 34. CheckOTP

```lua
local otp = request.input.otp
local ok = CheckOTP(otp)

if not ok then
    http_response_code = 401
    output = {
        success = false,
        error = "Invalid OTP"
    }
    return
end

output = {
    success = true
}
```

## 35. NTLM данные

```lua
output = {
    domain = request.NTLM_DOMAIN,
    user = request.NTLM_USER,
    host = request.NTLM_HOST
}
```

## 36. Plain text

```lua
http_response_code = 200
output = "OK"
```

## 37. HTML response

```lua
output = [[
<!doctype html>
<html>
<body>
    <h1>Hello DamuBPM</h1>
</body>
</html>
]]
```

Для такого сервиса используется MIME:

```text
text/html
```

## 38. Redirect

```lua
output = "https://example.kz/dashboard"
```

Используется совместно с:

```text
is_redirect_output = 1
```

## 39. Единый формат success/error

```lua
local input = request.input

if not input or not input.title then
    http_response_code = 400
    output = {
        success = false,
        error = {
            code = "TITLE_REQUIRED",
            message = "title is required"
        }
    }
    return
end

http_response_code = 200

output = {
    success = true,
    data = {
        title = input.title
    }
}
```

## 40. Helper ошибки

```lua
local function fail(status, code, message)
    http_response_code = status

    output = {
        success = false,
        error = {
            code = code,
            message = message
        }
    }
end

local input = request.input

if not input then
    fail(
        400,
        "INVALID_BODY",
        "JSON body required"
    )
    return
end

output = {
    success = true
}
```

## 41. Один endpoint для GET / POST / PUT

```lua
if request.method == "GET" then
    output = {
        action = "read"
    }
    return
end

if request.method == "POST" then
    output = {
        action = "create",
        input = request.input
    }
    return
end

if request.method == "PUT" then
    output = {
        action = "update",
        input = request.input
    }
    return
end

http_response_code = 405

output = {
    success = false,
    error = "Method not allowed"
}
```

## 42. Версия API в header

```lua
header = {
    ["X-API-Version"] = "v1"
}

output = {
    success = true,
    api_version = "v1"
}
```

## 43. Диагностика request

```lua
output = {
    method = request.method,
    host = request.host,
    lang = request.lang,
    user_id = request.user_id,
    remote_addr = request.RemoteAddr
}
```

## 44. Проверка простого API key

```lua
local expected = "demo-secret"
local token = request.header["X-Api-Key"]

if token ~= expected then
    http_response_code = 401
    output = {
        success = false,
        error = "Invalid API key"
    }
    return
end

output = {
    success = true
}
```

## 45. Проверка длины строки

```lua
local title = request.input.title or ""

if #title < 3 then
    http_response_code = 400
    output = {
        success = false,
        error = "title is too short"
    }
    return
end

output = {
    success = true,
    title = title
}
```

## 46. Значения по умолчанию

```lua
local sort = request.get.sort or "id"
local order = request.get.order or "asc"

output = {
    sort = sort,
    order = order
}
```

## 47. Boolean

```lua
local enabled = request.input.enabled == true

output = {
    success = true,
    enabled = enabled
}
```

## 48. Health check

```lua
http_response_code = 200

output = {
    status = "ok",
    service = "damubpm"
}
```

---

# Примеры вызова

## 1. GET через cURL

```bash
curl "https://example.kz/restapi/services/run/api/v1/customer/get?id=123"
```

## 2. GET с несколькими параметрами

```bash
curl "https://example.kz/restapi/services/run/api/v1/customer/list?page=1&limit=20"
```

## 3. POST JSON

```bash
curl -X POST \
  "https://example.kz/restapi/services/run/api/v1/customer/create" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "ТОО Test",
    "email": "info@test.kz"
  }'
```

## 4. PUT JSON

```bash
curl -X PUT \
  "https://example.kz/restapi/services/run/api/v1/customer/update?id=123" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Новое название"
  }'
```

## 5. POST с X-Api-Key

```bash
curl -X POST \
  "https://example.kz/restapi/services/run/api/v1/order/create" \
  -H "Content-Type: application/json" \
  -H "X-Api-Key: demo-secret" \
  -d '{"amount":1000}'
```

## 6. Async

```bash
curl -X POST \
  "https://example.kz/restapi/services/run/import/run?async=1" \
  -H "Content-Type: application/json" \
  -d '{"source":"crm"}'
```

## 7. GET через fetch

```javascript
const res = await fetch(
    "/restapi/services/run/api/v1/customer/get?id=123"
)

const data = await res.json()
console.log(data)
```

## 8. POST через fetch

```javascript
const res = await fetch(
    "/restapi/services/run/api/v1/customer/create",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: "ТОО Test",
            email: "info@test.kz"
        })
    }
)

const data = await res.json()
```

## 9. PUT через fetch

```javascript
const res = await fetch(
    "/restapi/services/run/api/v1/customer/update?id=123",
    {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: "Новое название"
        })
    }
)
```

## 10. fetch с X-Api-Key

```javascript
const res = await fetch(
    "/restapi/services/run/api/v1/private/check",
    {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-Api-Key": "demo-secret"
        },
        body: JSON.stringify({
            action: "check"
        })
    }
)
```

## 11. NTLM

```bash
curl "https://example.kz/restapi/services/run/auth/check?sys_ntlm_req=1"
```

## 12. Проверка HTTP status

```javascript
const res = await fetch(
    "/restapi/services/run/health"
)

if (!res.ok) {
    console.error(
        "HTTP status:",
        res.status
    )
}
```

---

# Авторизация и сессия

## Текущий пользователь

```lua
local userId = tonumber(request.user_id)
```

## Login

```lua
local errText, errCode = Login(
    userId,
    deviceToken
)
```

## LoginAs

```lua
local errText, errCode = LoginAs(
    userId,
    lastUserId,
    deviceToken
)
```

## SendEmailOTP

```lua
local errText, errCode = SendEmailOTP(
    "user@example.kz"
)
```

## CheckOTP

```lua
local ok = CheckOTP("123456")
```

---

# Async и no_parallel

## Async

Для POST/PUT можно добавить:

```text
?async=1
```

Пример:

```text
/restapi/services/run/import/run?async=1
```

Клиент сразу получает:

```text
ASYNC OK
```

## no_parallel

Если:

```text
no_parallel = 1
```

одновременно может выполняться только один экземпляр данного REST-сервиса.

Полезно для:

- импорта;
- синхронизации;
- больших отчётов;
- перерасчётов;
- массовых операций;
- интеграционных процедур.

Если сервис уже выполняется:

```text
Service already started
```

служебный код:

```text
7
```

---

# Headers и CORS

Lua response headers:

```lua
header = {
    ["X-Service"] = "customer",
    ["Cache-Control"] = "no-store"
}
```

В настройках headers можно использовать шаблоны входящих заголовков:

```text
Access-Control-Allow-Origin: {{Origin}}
```

Это удобно для CORS и отдельных настроек GET/POST/PUT/OPTIONS.

---

# Рекомендуемые шаблоны

## Базовый JSON endpoint

```lua
local function fail(status, code, message)
    http_response_code = status

    output = {
        success = false,
        error = {
            code = code,
            message = message
        }
    }
end

local input = request.input

if not input then
    fail(
        400,
        "INVALID_BODY",
        "JSON body required"
    )
    return
end

http_response_code = 200

output = {
    success = true,
    data = {}
}
```

## GET с обязательным ID

```lua
local id = tonumber(request.get.id)

if not id then
    http_response_code = 400
    output = {
        success = false,
        error = "id is required"
    }
    return
end

output = {
    success = true,
    data = {
        id = id
    }
}
```

## Приватный POST

```lua
local userId = tonumber(request.user_id)
local input = request.input

if not userId or userId == 0 then
    http_response_code = 401
    output = {
        success = false,
        error = "Unauthorized"
    }
    return
end

if not input then
    http_response_code = 400
    output = {
        success = false,
        error = "JSON body required"
    }
    return
end

output = {
    success = true,
    user_id = userId,
    data = input
}
```

## API Key endpoint

```lua
local apiKey = request.header["X-Api-Key"]

if apiKey ~= "replace-with-secret" then
    http_response_code = 401
    output = {
        success = false,
        error = "Invalid API key"
    }
    return
end

output = {
    success = true
}
```

## Универсальный GET / POST / PUT endpoint

```lua
if request.method == "GET" then
    output = {
        success = true,
        action = "read"
    }
    return
end

if request.method == "POST" then
    output = {
        success = true,
        action = "create",
        input = request.input
    }
    return
end

if request.method == "PUT" then
    output = {
        success = true,
        action = "update",
        input = request.input
    }
    return
end

http_response_code = 405

output = {
    success = false,
    error = "Method not allowed"
}
```

---

# Чек-лист

Перед публикацией REST-сервиса проверь:

- [ ] понятный `code`;
- [ ] при необходимости версия `api/v1/...`;
- [ ] правильный Content-Type;
- [ ] для JSON используется `application/json`;
- [ ] при необходимости `cut_status_info = 1`;
- [ ] корректно настроен `is_public`;
- [ ] корректно настроен `only_auth`;
- [ ] назначены необходимые роли;
- [ ] проверяются обязательные поля `request.input`;
- [ ] GET параметры валидируются;
- [ ] `request.user_id` преобразуется через `tonumber`;
- [ ] используются правильные HTTP status codes;
- [ ] ошибки имеют единый формат;
- [ ] CORS headers настроены корректно;
- [ ] `no_parallel` включён для тяжёлых процедур;
- [ ] async используется только при необходимости;
- [ ] endpoint проверен через cURL;
- [ ] endpoint проверен через fetch;
- [ ] проверены ошибочные сценарии.

---

[← Вернуться на Главную](index.html)
