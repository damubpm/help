[← Главная](index.html)

# DamuBPM Lua API — дополнительные модули


## Содержание

- [pkg/sftp](#pkg-sftp)
- [pkg/json](#pkg-json)
- [pkg/lock](#pkg-lock)
- [pkg/net](#pkg-net)
- [pkg/db](#pkg-db)
- [pkg/strconv](#pkg-strconv)
- [pkg/http](#pkg-http)
- [pkg/jsonpath](#pkg-jsonpath)
- [pkg/mxj](#pkg-mxj)
- [pkg/runtime](#pkg-runtime)
- [pkg/smb2](#pkg-smb2)
- [pkg/syscall](#pkg-syscall)
- [pkg/crypto](#pkg-crypto)
- [pkg/gokalkan](#pkg-gokalkan)
- [pkg/xml](#pkg-xml)
- [pkg/mongodb](#pkg-mongodb)
- [pkg/redis](#pkg-redis)
- [pkg/strings](#pkg-strings)
- [pkg/fmt](#pkg-fmt)
- [pkg/path/filepath](#pkg-path-filepath)



Справочник сформирован по предоставленным исходникам. Для каждой активной Lua-функции явно указаны **входные параметры**, **результирующие параметры в фактическом порядке возврата** и 2–3 примера вызова. В примерах все переменные результата выводятся через стандартный `print` с именем переменной. Инициализация модуля: `local pkg = require("pkg/...")`.

**20 модулей · 207 активных функций · 2–3 примера на функцию**


## pkg/sftp

Работа с SFTP: подключение, навигация, загрузка/выгрузка, удаление и права файлов.

8 функций

**Инициализация:** `local pkg = require("pkg/sftp")`

### Connect

Открывает SSH/SFTP-соединение и возвращает идентификатор подключения.


connectionId, err, code = pkg.Connect(addr, user, password)

#### Входные параметры

| Параметр | Тип    | Описание                                               |
|----------|--------|--------------------------------------------------------|
| addr     | string | адрес host:port                                        |
| user     | string | SSH-пользователь                                       |
| password | string | пароль; если пусто, может использоваться SSH_AUTH_SOCK |

#### Результирующие параметры

| №   | Значение     | Тип     | Описание                                |
|-----|--------------|---------|-----------------------------------------|
| 1   | connectionId | string  | id соединения; пустая строка при ошибке |
| 2   | err          | string  | сообщение ошибки или пустая строка      |
| 3   | code         | integer | 0 = успех                               |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local id, err, code = pkg.Connect("sftp.example.kz:22", "user1", "secret")
    print("id =", id)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local id, err, code = pkg.Connect("10.0.0.12:22", "deploy", "")
    print("id =", id)
    print("err =", err)
    print("code =", code)
    print("connection:", id, "code:", code, "err:", err)

### Download

Скачивает удалённый файл SFTP в локальный файл.


err, code = pkg.Download(connectionId, remoteFile, localFile)

#### Входные параметры

| Параметр     | Тип    | Описание       |
|--------------|--------|----------------|
| connectionId | string | id соединения  |
| remoteFile   | string | удалённый путь |
| localFile    | string | локальный путь |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.Download(sftpId, "/export/report.csv", "/tmp/report.csv")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.Download(sftpId, "/in/docs/a.pdf", "/var/tmp/a.pdf")
    print("err =", err)
    print("code =", code)
    print("download:", code, err)

### Upload

Загружает локальный файл на SFTP-сервер.


err, code = pkg.Upload(connectionId, localFile, remoteFile)

#### Входные параметры

| Параметр     | Тип    | Описание       |
|--------------|--------|----------------|
| connectionId | string | id соединения  |
| localFile    | string | локальный путь |
| remoteFile   | string | удалённый путь |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.Upload(sftpId, "/tmp/result.json", "/out/result.json")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.Upload(sftpId, "/var/data/archive.zip", "/backup/archive.zip")
    print("err =", err)
    print("code =", code)
    print("upload:", code, err)

### Getwd

Возвращает текущий рабочий каталог SFTP-сессии.


cwd, err, code = pkg.Getwd(connectionId)

#### Входные параметры

| Параметр     | Тип    | Описание      |
|--------------|--------|---------------|
| connectionId | string | id соединения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | cwd      | string  | текущий каталог          |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local cwd, err, code = pkg.Getwd(sftpId)
    print("cwd =", cwd)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local cwd, err, code = pkg.Getwd(sftpId)
    print("cwd =", cwd)
    print("err =", err)
    print("code =", code)
    if code == 0 then print("SFTP cwd:", cwd) else print(err) end

### Close

Закрывает SFTP и SSH-соединение.


err, code = pkg.Close(connectionId)

#### Входные параметры

| Параметр     | Тип    | Описание      |
|--------------|--------|---------------|
| connectionId | string | id соединения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.Close(sftpId)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.Close(sftpId)
    print("err =", err)
    print("code =", code)
    if code ~= 0 then print("close error:", err) end

### ReadDir

Читает содержимое удалённого каталога и возвращает метаданные файлов.


items, err, code = pkg.ReadDir(connectionId, dir)

#### Входные параметры

| Параметр     | Тип    | Описание          |
|--------------|--------|-------------------|
| connectionId | string | id соединения     |
| dir          | string | удалённый каталог |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                                  |
|-----|----------|------------|-------------------------------------------|
| 1   | items    | table\|nil | массив {Name, Size, ModTime, Mode, IsDir} |
| 2   | err      | string     | ошибка или пустая строка                  |
| 3   | code     | integer    | 0 = успех                                 |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local items, err, code = pkg.ReadDir(sftpId, "/in")
    print("items =", items)
    print("err =", err)
    print("code =", code)
    if items then for _, f in ipairs(items) do print(f.Name, f.Size, f.IsDir) end end

**Пример 2**


    local items, err, code = pkg.ReadDir(sftpId, ".")
    print("items =", items)
    print("err =", err)
    print("code =", code)
    print("count:", items and #items or 0, "code:", code, err)

### Remove

Удаляет удалённый файл или путь через SFTP.


err, code = pkg.Remove(connectionId, remoteFile)

#### Входные параметры

| Параметр     | Тип    | Описание       |
|--------------|--------|----------------|
| connectionId | string | id соединения  |
| remoteFile   | string | удалённый путь |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.Remove(sftpId, "/tmp/old.txt")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.Remove(sftpId, "/out/processed.csv")
    print("err =", err)
    print("code =", code)
    print("remove:", code, err)

### Chmod

Изменяет права удалённого файла; режим передаётся строкой в восьмеричном виде.


err, code = pkg.Chmod(connectionId, remoteFile, fileMode)

#### Входные параметры

| Параметр     | Тип    | Описание                            |
|--------------|--------|-------------------------------------|
| connectionId | string | id соединения                       |
| remoteFile   | string | удалённый путь                      |
| fileMode     | string | восьмеричный режим, например "0644" |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.Chmod(sftpId, "/scripts/run.sh", "0755")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.Chmod(sftpId, "/data/report.csv", "0640")
    print("err =", err)
    print("code =", code)
    print("chmod:", code, err)


## pkg/json

Кодирование Lua-таблиц в JSON и разбор JSON обратно в Lua-значения.

3 функций

**Инициализация:** `local pkg = require("pkg/json")`

### marshal

Сериализует Lua-таблицу в компактный JSON.


json = pkg.marshal(value)

#### Входные параметры

| Параметр | Тип        | Описание            |
|----------|------------|---------------------|
| value    | table\|nil | Lua-таблица или nil |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                              |
|-----|----------|--------|---------------------------------------|
| 1   | json     | string | JSON; при ошибке вызывается Lua error |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.marshal({id=501, state="NEW"})
    print("s =", s)

**Пример 2**


    local s = pkg.marshal({items={{sku="A1", qty=2},{sku="B2", qty=1}}})
    print("s =", s)

### marshalIndent

Сериализует Lua-таблицу в форматированный JSON с указанным отступом.


json = pkg.marshalIndent(value, indent)

#### Входные параметры

| Параметр | Тип        | Описание                     |
|----------|------------|------------------------------|
| value    | table\|nil | Lua-таблица или nil          |
| indent   | string     | строка отступа, например " " |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                                   |
|-----|----------|--------|--------------------------------------------|
| 1   | json     | string | форматированный JSON; при ошибке Lua error |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.marshalIndent({id=501, active=true}, "  ")
    print("s =", s)

**Пример 2**


    local s = pkg.marshalIndent({user={name="Ayan", roles={"admin","user"}}}, "    ")
    print("s =", s)

### unmarshal

Разбирает JSON-строку в Lua-таблицы/скаляры.


value = pkg.unmarshal(payload)

#### Входные параметры

| Параметр | Тип    | Описание    |
|----------|--------|-------------|
| payload  | string | JSON-строка |

#### Результирующие параметры

| №   | Значение | Тип | Описание                           |
|-----|----------|-----|------------------------------------|
| 1   | value    | any | Lua-значение; при ошибке Lua error |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local v = pkg.unmarshal('{"id":501,"state":"NEW"}')
    print("v =", v)
    print(v.id, v.state)

**Пример 2**


    local v = pkg.unmarshal('[1,2,3]')
    print("v =", v)
    for i, x in ipairs(v) do print(i, x) end


## pkg/lock

Именованные блокировки с идентификатором владельца.

2 функций

**Инициализация:** `local pkg = require("pkg/lock")`

### Acquire

Пытается захватить именованную блокировку и возвращает id владельца и код результата.


id, code = pkg.Acquire(key)

#### Входные параметры

| Параметр | Тип    | Описание       |
|----------|--------|----------------|
| key      | string | имя блокировки |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                                   |
|-----|----------|---------|--------------------------------------------|
| 1   | id       | integer | id владельца блокировки                    |
| 2   | code     | integer | 0 = блокировка захвачена, 1 = не захвачена |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local id, code = pkg.Acquire("order:501")
    print("id =", id)
    print("code =", code)

**Пример 2**


    local id, code = pkg.Acquire("nightly-import")
    print("id =", id)
    print("code =", code)
    if code == 0 then print("locked", id) else print("busy") end

### Release

Освобождает именованную блокировку по ключу и id владельца.


code = pkg.Release(key, id)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | имя блокировки         |
| id       | integer | id, полученный Acquire |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                            |
|-----|----------|---------|-------------------------------------|
| 1   | code     | integer | 0 = освобождена, 1 = не освобождена |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code = pkg.Release("order:501", lockId)
    print("code =", code)

**Пример 2**


    local code = pkg.Release("nightly-import", lockId)
    print("code =", code)
    print(code == 0 and "released" or "not owner")


## pkg/net

Получение IPv4-адресов локальных сетевых интерфейсов.

1 функций

**Инициализация:** `local pkg = require("pkg/net")`

### Interfaces

Возвращает IPv4-адреса локальных сетевых интерфейсов.


addresses, err, code = pkg.Interfaces()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение  | Тип        | Описание                                |
|-----|-----------|------------|-----------------------------------------|
| 1   | addresses | table\|nil | массив IPv4                             |
| 2   | err       | string     | ошибка или пустая строка                |
| 3   | code      | integer    | в текущем коде на успехе возвращается 9 |

⚠ На успешной ветке текущая реализация возвращает code = 9, а не 0.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ips, err, code = pkg.Interfaces()
    print("ips =", ips)
    print("err =", err)
    print("code =", code)
    if ips then for _, ip in ipairs(ips) do print(ip) end end

**Пример 2**


    local ips, err, code = pkg.Interfaces()
    print("ips =", ips)
    print("err =", err)
    print("code =", code)
    print("IPv4 count:", ips and #ips or 0, "code:", code, err)


## pkg/db

Подключение к внешней SQL-БД и выполнение SELECT-подобных запросов.

3 функций

**Инициализация:** `local pkg = require("pkg/db")`

### connect

Открывает соединение с внешней SQL-БД указанного драйвера.


connectionId, err, code = pkg.connect(dbtype, connstr)

#### Входные параметры

| Параметр | Тип    | Описание                  |
|----------|--------|---------------------------|
| dbtype   | string | имя драйвера database/sql |
| connstr  | string | строка подключения        |

#### Результирующие параметры

| №   | Значение     | Тип         | Описание                 |
|-----|--------------|-------------|--------------------------|
| 1   | connectionId | string\|nil | id соединения            |
| 2   | err          | string      | ошибка или пустая строка |
| 3   | code         | integer     | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local db, err, code = pkg.connect("postgres", "postgres://user:pass@db:5432/app?sslmode=disable")
    print("db =", db)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local db, err, code = pkg.connect("mysql", "user:pass@tcp(10.0.0.5:3306)/app")
    print("db =", db)
    print("err =", err)
    print("code =", code)
    print("db id:", db, code, err)

### query

Выполняет SQL-запрос с переменным числом параметров и возвращает строки результата.


rows, err, code = pkg.query(connectionId, sql, ...params)

#### Входные параметры

| Параметр     | Тип    | Описание                                                                                         |
|--------------|--------|--------------------------------------------------------------------------------------------------|
| connectionId | string | id, возвращённый connect                                                                         |
| sql          | string | SQL с ? placeholders                                                                             |
| ...params    | any... | по одному значению на каждый ?; Lua-таблица дополнительно разворачивается в несколько параметров |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                 |
|-----|----------|------------|--------------------------|
| 1   | rows     | table\|nil | строки результата        |
| 2   | err      | string     | ошибка или пустая строка |
| 3   | code     | integer    | 0 = успех                |

⚠ Количество значений после SQL должно соответствовать количеству \`?\` placeholders. Таблица, переданная как аргумент, разворачивается в несколько параметров.

⚠ Параметры перед выполнением приводятся текущей реализацией к строкам.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local rows, err, code = pkg.query(db, "select * from orders where customer_id = ?", 501)
    print("rows =", rows)
    print("err =", err)
    print("code =", code)
    if rows then for _, row in ipairs(rows) do print(row.id, row.state) end end

**Пример 2**


    local rows, err, code = pkg.query(db, "select * from orders where customer_id = ? and created_at >= ? and state = ?", 501, "2026-01-01", "NEW")
    print("rows =", rows)
    print("err =", err)
    print("code =", code)
    print(rows and #rows or 0, err, code)

**Пример 3**


    local rows, err, code = pkg.query(db, "select * from users where id in (?, ?, ?)", {101, 102, 103})
    print("rows =", rows)
    print("err =", err)
    print("code =", code)
    print(rows and #rows or 0, err, code)

### close

Закрывает внешнее SQL-соединение.


err, code = pkg.close(connectionId)

#### Входные параметры

| Параметр     | Тип    | Описание      |
|--------------|--------|---------------|
| connectionId | string | id соединения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.close(db)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.close(db)
    print("err =", err)
    print("code =", code)
    if code ~= 0 then print("close error:", err) end


## pkg/strconv

Преобразование строк, целых, чисел с плавающей точкой, bool и complex.

10 функций

**Инициализация:** `local pkg = require("pkg/strconv")`

### ParseFloat

Преобразует строку в число с плавающей точкой.


value, err, code = pkg.ParseFloat(input, digits)

#### Входные параметры

| Параметр | Тип     | Описание                                 |
|----------|---------|------------------------------------------|
| input    | string  | входное значение                         |
| digits   | integer | bitSize для ParseFloat: обычно 32 или 64 |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | number  | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.ParseFloat("123.45", 64)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.ParseFloat("3.14159", 32)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### ParseInt

Преобразует строку в знаковое целое с указанным основанием и размером.


value, err, code = pkg.ParseInt(input, base, bitSize)

#### Входные параметры

| Параметр | Тип     | Описание                               |
|----------|---------|----------------------------------------|
| input    | string  | входное значение                       |
| base     | integer | основание системы счисления (0, 2..36) |
| bitSize  | integer | размер: 0/8/16/32/64 согласно операции |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | integer | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.ParseInt("FF", 16, 64)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.ParseInt("101101", 2, 32)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### Atoi

Преобразует десятичную строку в integer.


value, err, code = pkg.Atoi(input)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| input    | string | входное значение |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | integer | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.Atoi("501")
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.Atoi("-42")
    print("value =", value)
    print("err =", err)
    print("code =", code)

### Itoa

Преобразует integer в десятичную строку.


value, err, code = pkg.Itoa(input)

#### Входные параметры

| Параметр | Тип     | Описание         |
|----------|---------|------------------|
| input    | integer | входное значение |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | string  | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.Itoa(501)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.Itoa(-42)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### ParseBool

Преобразует строковое представление bool в boolean.


value, err, code = pkg.ParseBool(input)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| input    | string | входное значение |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | boolean | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.ParseBool("true")
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.ParseBool("0")
    print("value =", value)
    print("err =", err)
    print("code =", code)

### FormatFloat

Форматирует число с плавающей точкой.


value, err, code = pkg.FormatFloat(input, format, prec, bitSize)

#### Входные параметры

| Параметр | Тип     | Описание                                |
|----------|---------|-----------------------------------------|
| input    | number  | входное значение                        |
| format   | string  | форматирующая строка или символ формата |
| prec     | integer | точность                                |
| bitSize  | integer | размер: 0/8/16/32/64 согласно операции  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | string  | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.FormatFloat(123.4567, "f", 2, 64)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.FormatFloat(12345.0, "e", 3, 64)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### ParseUint

Преобразует строку в беззнаковое целое.


value, err, code = pkg.ParseUint(input, base, bitSize)

#### Входные параметры

| Параметр | Тип     | Описание                               |
|----------|---------|----------------------------------------|
| input    | string  | входное значение                       |
| base     | integer | основание системы счисления (0, 2..36) |
| bitSize  | integer | размер: 0/8/16/32/64 согласно операции |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | integer | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.ParseUint("FF", 16, 64)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.ParseUint("755", 8, 32)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### FormatInt

Форматирует знаковое целое в указанной системе счисления.


value, err, code = pkg.FormatInt(input, base)

#### Входные параметры

| Параметр | Тип     | Описание                               |
|----------|---------|----------------------------------------|
| input    | integer | входное значение                       |
| base     | integer | основание системы счисления (0, 2..36) |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | string  | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.FormatInt(255, 16)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.FormatInt(10, 2)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### FormatUint

Форматирует беззнаковое целое в указанной системе счисления.


value, err, code = pkg.FormatUint(input, base)

#### Входные параметры

| Параметр | Тип     | Описание                               |
|----------|---------|----------------------------------------|
| input    | integer | входное значение                       |
| base     | integer | основание системы счисления (0, 2..36) |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | string  | результат                |
| 2   | err      | string  | ошибка или пустая строка |
| 3   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.FormatUint(255, 16)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.FormatUint(64, 8)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### ParseComplex

Разбирает комплексное число и возвращает действительную и мнимую части.


real, imag, err, code = pkg.ParseComplex(input, bitSize)

#### Входные параметры

| Параметр | Тип     | Описание                               |
|----------|---------|----------------------------------------|
| input    | string  | входное значение                       |
| bitSize  | integer | размер: 0/8/16/32/64 согласно операции |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | real     | number  | действительная часть     |
| 2   | imag     | number  | мнимая часть             |
| 3   | err      | string  | ошибка или пустая строка |
| 4   | code     | integer | 0 = успех                |

⚠ На успехе возвращаются 4 значения. В error-ветке исходника помещаются только 3 новых значения при \`return 4\`; это потенциальная несогласованность реализации.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local re, im, err, code = pkg.ParseComplex("3+4i", 128)
    print("re =", re)
    print("im =", im)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local re, im, err, code = pkg.ParseComplex("1.5-2.25i", 128)
    print("re =", re)
    print("im =", im)
    print("err =", err)
    print("code =", code)
    print("real", re, "imag", im, err, code)


## pkg/http

HTTP-клиент GET/POST/PUT/DELETE с заголовками и таймаутом.

4 функций

**Инициализация:** `local pkg = require("pkg/http")`

### post

Выполняет HTTP POST.


body, err, code = pkg.post(url, body, headers, timeoutSeconds)

или

headers, body, err, code = pkg.post(url, body, headers, timeoutSeconds, returnHeadersTrigger)

#### Входные параметры

| Параметр             | Тип                    | Описание                                                                                                        |
|----------------------|------------------------|-----------------------------------------------------------------------------------------------------------------|
| url                  | string                 | URL                                                                                                             |
| body                 | string                 | тело запроса                                                                                                    |
| headers              | table\<string,string\> | HTTP-заголовки                                                                                                  |
| timeoutSeconds       | integer                | таймаут, по умолчанию 60                                                                                        |
| returnHeadersTrigger | any, optional          | если 5-й аргумент присутствует, функция возвращает 4 значения; текущий код берёт boolean-флаг из 4-го аргумента |

#### Результирующие параметры

| Вариант   | №   | Значение | Тип         | Описание                                                         |
|-----------|-----|----------|-------------|------------------------------------------------------------------|
| обычно    | 1   | body     | string\|nil | тело HTTP-ответа; nil при сетевой/внутренней ошибке              |
| обычно    | 2   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| обычно    | 3   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |
| с headers | 1   | headers  | table\|nil  | response headers                                                 |
| с headers | 2   | body     | string\|nil | тело HTTP-ответа                                                 |
| с headers | 3   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| с headers | 4   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |

⚠ TLS-проверка сертификата отключена (\`InsecureSkipVerify\`).

⚠ Особенность текущего кода: наличие 5-го аргумента включает возврат headers, но boolean читается из 4-го аргумента (timeout).

#### Примеры вызова и вывод значений результата

**Пример 1**


    local body, err, code = pkg.post("https://api.example.kz/v1/orders", '{"id":501}', {["Content-Type"]="application/json"}, 30)
    print("body =", body)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local headers, body, err, code = pkg.post("https://api.example.kz/v1/orders", '{"state":"NEW"}', {Authorization="Bearer TOKEN", ["Content-Type"]="application/json"}, 30, true)
    print("headers =", headers)
    print("body =", body)
    print("err =", err)
    print("code =", code)

### put

Выполняет HTTP PUT.


body, err, code = pkg.put(url, body, headers, timeoutSeconds)

или

headers, body, err, code = pkg.put(url, body, headers, timeoutSeconds, returnHeadersTrigger)

#### Входные параметры

| Параметр             | Тип                    | Описание                                                                                                        |
|----------------------|------------------------|-----------------------------------------------------------------------------------------------------------------|
| url                  | string                 | URL                                                                                                             |
| body                 | string                 | тело запроса                                                                                                    |
| headers              | table\<string,string\> | HTTP-заголовки                                                                                                  |
| timeoutSeconds       | integer                | таймаут, по умолчанию 60                                                                                        |
| returnHeadersTrigger | any, optional          | если 5-й аргумент присутствует, функция возвращает 4 значения; текущий код берёт boolean-флаг из 4-го аргумента |

#### Результирующие параметры

| Вариант   | №   | Значение | Тип         | Описание                                                         |
|-----------|-----|----------|-------------|------------------------------------------------------------------|
| обычно    | 1   | body     | string\|nil | тело HTTP-ответа; nil при сетевой/внутренней ошибке              |
| обычно    | 2   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| обычно    | 3   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |
| с headers | 1   | headers  | table\|nil  | response headers                                                 |
| с headers | 2   | body     | string\|nil | тело HTTP-ответа                                                 |
| с headers | 3   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| с headers | 4   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |

⚠ TLS-проверка сертификата отключена (\`InsecureSkipVerify\`).

⚠ Особенность текущего кода: наличие 5-го аргумента включает возврат headers, но boolean читается из 4-го аргумента (timeout).

#### Примеры вызова и вывод значений результата

**Пример 1**


    local body, err, code = pkg.put("https://api.example.kz/v1/orders", '{"id":501}', {["Content-Type"]="application/json"}, 30)
    print("body =", body)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local headers, body, err, code = pkg.put("https://api.example.kz/v1/orders", '{"state":"NEW"}', {Authorization="Bearer TOKEN", ["Content-Type"]="application/json"}, 30, true)
    print("headers =", headers)
    print("body =", body)
    print("err =", err)
    print("code =", code)

### get

Выполняет HTTP GET.


body, err, code = pkg.get(url, headers, timeoutSeconds)

или

headers, body, err, code = pkg.get(url, headers, timeoutSeconds, true)

#### Входные параметры

| Параметр       | Тип                    | Описание                                         |
|----------------|------------------------|--------------------------------------------------|
| url            | string                 | URL                                              |
| headers        | table\<string,string\> | HTTP-заголовки                                   |
| timeoutSeconds | integer                | таймаут, по умолчанию 60                         |
| getHeaders     | boolean, optional      | true — вернуть response headers первым значением |

#### Результирующие параметры

| Вариант   | №   | Значение | Тип         | Описание                                                         |
|-----------|-----|----------|-------------|------------------------------------------------------------------|
| обычно    | 1   | body     | string\|nil | тело HTTP-ответа; nil при сетевой/внутренней ошибке              |
| обычно    | 2   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| обычно    | 3   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |
| с headers | 1   | headers  | table\|nil  | response headers; используется при 4-м аргументе true            |
| с headers | 2   | body     | string\|nil | тело HTTP-ответа                                                 |
| с headers | 3   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| с headers | 4   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |

⚠ TLS-проверка сертификата отключена (\`InsecureSkipVerify\`).

⚠ HTTP status != 200 возвращается как \`err = resp.Status\`, \`code = HTTP status code\`.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local body, err, code = pkg.get("https://api.example.kz/v1/orders/501", {Authorization="Bearer TOKEN"}, 20)
    print("body =", body)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local headers, body, err, code = pkg.get("https://api.example.kz/v1/orders/501", {Accept="application/json"}, 20, true)
    print("headers =", headers)
    print("body =", body)
    print("err =", err)
    print("code =", code)

### delete

Выполняет HTTP DELETE.


body, err, code = pkg.delete(url, headers, timeoutSeconds)

или

headers, body, err, code = pkg.delete(url, headers, timeoutSeconds, true)

#### Входные параметры

| Параметр       | Тип                    | Описание                                         |
|----------------|------------------------|--------------------------------------------------|
| url            | string                 | URL                                              |
| headers        | table\<string,string\> | HTTP-заголовки                                   |
| timeoutSeconds | integer                | таймаут, по умолчанию 60                         |
| getHeaders     | boolean, optional      | true — вернуть response headers первым значением |

#### Результирующие параметры

| Вариант   | №   | Значение | Тип         | Описание                                                         |
|-----------|-----|----------|-------------|------------------------------------------------------------------|
| обычно    | 1   | body     | string\|nil | тело HTTP-ответа; nil при сетевой/внутренней ошибке              |
| обычно    | 2   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| обычно    | 3   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |
| с headers | 1   | headers  | table\|nil  | response headers                                                 |
| с headers | 2   | body     | string\|nil | тело HTTP-ответа                                                 |
| с headers | 3   | err      | string      | пустая строка при HTTP 200; иначе ошибка или HTTP status         |
| с headers | 4   | code     | integer     | 0 при HTTP 200; иначе внутренний код ошибки или HTTP status code |

⚠ TLS-проверка сертификата отключена (\`InsecureSkipVerify\`).

⚠ HTTP status != 200 возвращается как \`err = resp.Status\`, \`code = HTTP status code\`.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local body, err, code = pkg.delete("https://api.example.kz/v1/orders/501", {Authorization="Bearer TOKEN"}, 20)
    print("body =", body)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local headers, body, err, code = pkg.delete("https://api.example.kz/v1/orders/501", {Accept="application/json"}, 20, true)
    print("headers =", headers)
    print("body =", body)
    print("err =", err)
    print("code =", code)


## pkg/jsonpath

Чтение значений из Lua-таблицы по JSONPath.

1 функций

**Инициализация:** `local pkg = require("pkg/jsonpath")`

### Read

Выполняет JSONPath-запрос по Lua-таблице; скалярный результат оборачивается в таблицу из одного элемента.


values, err, code = pkg.Read(value, path)

#### Входные параметры

| Параметр | Тип    | Описание                              |
|----------|--------|---------------------------------------|
| value    | table  | Lua-таблица                           |
| path     | string | JSONPath, например \$.orders\[\*\].id |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                                      |
|-----|----------|-------------|-----------------------------------------------|
| 1   | values   | table\|nil  | результаты JSONPath; скаляр обёрнут в таблицу |
| 2   | err      | string\|nil | nil на успехе                                 |
| 3   | code     | integer     | 0 = успех                                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result, err, code = pkg.Read({orders={{id=1,state="NEW"},{id=2,state="DONE"}}}, "$.orders[*].id")
    print("result =", result)
    print("err =", err)
    print("code =", code)
    for _, v in ipairs(result or {}) do print(v) end

**Пример 2**


    local result, err, code = pkg.Read({user={name="Ayan"}}, "$.user.name")
    print("result =", result)
    print("err =", err)
    print("code =", code)
    print(result and result[1], err, code)


## pkg/mxj

Преобразование Lua-таблиц/JSON-подобных структур в XML и XML обратно в таблицу.

2 функций

**Инициализация:** `local pkg = require("pkg/mxj")`

### JsonToXml

Преобразует Lua-таблицу в XML.


xml, err, code = pkg.JsonToXml(value)

#### Входные параметры

| Параметр | Тип   | Описание    |
|----------|-------|-------------|
| value    | table | Lua-таблица |

#### Результирующие параметры

| №   | Значение | Тип         | Описание      |
|-----|----------|-------------|---------------|
| 1   | xml      | string\|nil | XML           |
| 2   | err      | string\|nil | nil на успехе |
| 3   | code     | integer     | 0 = успех     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local xml, err, code = pkg.JsonToXml({order={id=501,state="NEW"}})
    print("xml =", xml)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local xml, err, code = pkg.JsonToXml({root={item={{id=1},{id=2}}}})
    print("xml =", xml)
    print("err =", err)
    print("code =", code)

### XmlToJson

Разбирает XML в Lua-таблицу.


value, err, code = pkg.XmlToJson(xml)

#### Входные параметры

| Параметр | Тип    | Описание   |
|----------|--------|------------|
| xml      | string | XML-строка |

#### Результирующие параметры

| №   | Значение | Тип         | Описание      |
|-----|----------|-------------|---------------|
| 1   | value    | table\|nil  | Lua-таблица   |
| 2   | err      | string\|nil | nil на успехе |
| 3   | code     | integer     | 0 = успех     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local t, err, code = pkg.XmlToJson("<order><id>501</id><state>NEW</state></order>")
    print("t =", t)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local t, err, code = pkg.XmlToJson("<root><item>A</item><item>B</item></root>")
    print("t =", t)
    print("err =", err)
    print("code =", code)
    print(t and t.root, err, code)


## pkg/runtime

Информация о Go runtime и операции GC/sleep/caller.

10 функций

**Инициализация:** `local pkg = require("pkg/runtime")`

### MemStats

Возвращает выбранные счётчики памяти Go runtime.


stats, err, code = pkg.MemStats()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание                                                           |
|-----|----------|---------|--------------------------------------------------------------------|
| 1   | stats    | table   | Alloc, TotalAlloc, Sys, NumGC, Frees, HeapAlloc, HeapSys, HeapIdle |
| 2   | err      | string  | пустая строка                                                      |
| 3   | code     | integer | в текущей реализации всегда 3                                      |

⚠ На успешной ветке текущая реализация возвращает code = 3.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s, err, code = pkg.MemStats()
    print("s =", s)
    print("err =", err)
    print("code =", code)
    print(s.Alloc, s.HeapAlloc, s.NumGC, err, code)

**Пример 2**


    local s, err, code = pkg.MemStats()
    print("s =", s)
    print("err =", err)
    print("code =", code)
    print("heap MB:", math.floor((s.HeapAlloc or 0)/1024/1024), err, code)

### GoroutineCount

luaGoroutineCount возвращает количество активных горутин.


value = pkg.GoroutineCount()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | value    | integer | число активных goroutine |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n = pkg.GoroutineCount()
    print("n =", n)

**Пример 2**


    local value = pkg.GoroutineCount()
    print("value =", value)

### NumCPU

luaNumCPU возвращает количество логических процессоров, доступных планировщику.


value = pkg.NumCPU()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание             |
|-----|----------|---------|----------------------|
| 1   | value    | integer | число логических CPU |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n = pkg.NumCPU()
    print("n =", n)

**Пример 2**


    local value = pkg.NumCPU()
    print("value =", value)

### Version

luaVersion возвращает версию Go в виде строки.


value = pkg.Version()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | value    | string | версия Go |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local v = pkg.Version()
    print("v =", v)

**Пример 2**


    local value = pkg.Version()
    print("value =", value)

### Compiler

luaCompiler возвращает имя компилятора Go.


value = pkg.Compiler()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип    | Описание        |
|-----|----------|--------|-----------------|
| 1   | value    | string | имя компилятора |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local c = pkg.Compiler()
    print("c =", c)

**Пример 2**


    local value = pkg.Compiler()
    print("value =", value)

### NumCgoCall

luaNumCgoCall возвращает количество вызовов Cgo.


value = pkg.NumCgoCall()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание          |
|-----|----------|---------|-------------------|
| 1   | value    | integer | число вызовов cgo |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n = pkg.NumCgoCall()
    print("n =", n)

**Пример 2**


    local value = pkg.NumCgoCall()
    print("value =", value)

### GC

luaGC запускает сборку мусора.


pkg.GC()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

Нет результирующих параметров.

#### Примеры вызова и вывод значений результата

**Пример 1**


    pkg.GC()
    print("GC completed")

**Пример 2**


    print("before", collectgarbage("count"))
    pkg.GC()
    print("runtime GC requested")

### Goexit

luaGoexit завершает выполнение текущей горутины.


pkg.Goexit()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

Нет результирующих параметров.

⚠ Завершает текущую Go goroutine. Используйте только если это ожидаемое поведение хоста Lua.

#### Примеры вызова и вывод значений результата

**Пример 1**


    print("before Goexit")
    pkg.Goexit()
    print("this line normally will not run")

**Пример 2**


    local function finishCurrentTask()
      pkg.Goexit()
    end
    print("Goexit terminates the current Go goroutine")

### Caller

luaCaller возвращает информацию о вызывающей функции.


value = pkg.Caller(depth)

#### Входные параметры

| Параметр | Тип     | Описание      |
|----------|---------|---------------|
| depth    | integer | глубина стека |

#### Результирующие параметры

| №   | Значение | Тип        | Описание               |
|-----|----------|------------|------------------------|
| 1   | value    | table\|nil | {pc,file,line} или nil |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local info = pkg.Caller(0)
    print("info =", info)
    if info then print(info.file, info.line, info.pc) end

**Пример 2**


    local info = pkg.Caller(1)
    print("info =", info)
    print(info and info.file, info and info.line)

### Sleep

luaSleep приостанавливает выполнение на определенное количество времени.


pkg.Sleep(milliseconds)

#### Входные параметры

| Параметр     | Тип     | Описание              |
|--------------|---------|-----------------------|
| milliseconds | integer | пауза в миллисекундах |

#### Результирующие параметры

Нет результирующих параметров.

#### Примеры вызова и вывод значений результата

**Пример 1**


    pkg.Sleep(500)
    print("slept 500 ms")

**Пример 2**


    print("start")
    pkg.Sleep(2000)
    print("after 2 seconds")


## pkg/smb2

SMB2-клиент: подключение, шары, файлы и каталоги.

9 функций

**Инициализация:** `local pkg = require("pkg/smb2")`

ℹ Соединение/сессия/шара хранятся в одном глобальном контексте модуля; новое подключение заменяет предыдущее.

### OpenConnection

функция для открытия соединения и сессии.


code, err = pkg.OpenConnection(host, login, password)

#### Входные параметры

| Параметр | Тип    | Описание               |
|----------|--------|------------------------|
| host     | string | host:port, обычно :445 |
| login    | string | пользователь           |
| password | string | пароль                 |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | code     | integer | 0 = успех                |
| 2   | err      | string  | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.OpenConnection("10.0.0.20:445", "DOMAIN\\user", "secret")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.OpenConnection("fileserver.local:445", "svc_user", "secret")
    print("code =", code)
    print("err =", err)
    print(code == 0 and "connected" or err)

### CloseConnection

функция для закрытия соединения и завершения сессии.


code, err = pkg.CloseConnection()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание      |
|-----|----------|---------|---------------|
| 1   | code     | integer | 0 = успех     |
| 2   | err      | string  | пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.CloseConnection()
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.CloseConnection()
    print("code =", code)
    print("err =", err)
    if code ~= 0 then print(err) end

### MountShare

функция для монтирования шары.


code, err = pkg.MountShare(shareName)

#### Входные параметры

| Параметр  | Тип    | Описание |
|-----------|--------|----------|
| shareName | string | имя шары |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | code     | integer | 0 = успех                |
| 2   | err      | string  | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.MountShare("Documents")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.MountShare("Archive$")
    print("code =", code)
    print("err =", err)
    print(code == 0 and "mounted" or err)

### UnmountShare

функция для отмонтирования шары.


code, err = pkg.UnmountShare()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание      |
|-----|----------|---------|---------------|
| 1   | code     | integer | 0 = успех     |
| 2   | err      | string  | пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.UnmountShare()
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.UnmountShare()
    print("code =", code)
    print("err =", err)
    print("unmount:", code, err)

### ListSharenames

функция для получения списка шар на сервере.


shares, code, err = pkg.ListSharenames()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип        | Описание                 |
|-----|----------|------------|--------------------------|
| 1   | shares   | table\|nil | массив имён шар          |
| 2   | code     | integer    | 0 = успех                |
| 3   | err      | string     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local shares, code, err = pkg.ListSharenames()
    print("shares =", shares)
    print("code =", code)
    print("err =", err)
    if shares then for _, s in ipairs(shares) do print(s) end end

**Пример 2**


    local shares, code, err = pkg.ListSharenames()
    print("shares =", shares)
    print("code =", code)
    print("err =", err)
    print("shares:", shares and #shares or 0, code, err)

### ListFiles

функция для получения списка файлов в текущей монтированной шаре.


files, code, err = pkg.ListFiles(dir)

#### Входные параметры

| Параметр | Тип    | Описание            |
|----------|--------|---------------------|
| dir      | string | каталог внутри шары |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                 |
|-----|----------|------------|--------------------------|
| 1   | files    | table\|nil | массив имён файлов       |
| 2   | code     | integer    | 0 = успех                |
| 3   | err      | string     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local files, code, err = pkg.ListFiles("\\reports")
    print("files =", files)
    print("code =", code)
    print("err =", err)
    if files then for _, f in ipairs(files) do print(f) end end

**Пример 2**


    local files, code, err = pkg.ListFiles(".")
    print("files =", files)
    print("code =", code)
    print("err =", err)
    print(files and #files or 0, code, err)

### ReadFile

функция для чтения файла на сервере.


content, code, err = pkg.ReadFile(path)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| path     | string | путь внутри шары |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | content  | string  | содержимое               |
| 2   | code     | integer | 0 = успех                |
| 3   | err      | string  | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local content, code, err = pkg.ReadFile("reports\\today.txt")
    print("content =", content)
    print("code =", code)
    print("err =", err)

**Пример 2**


    local content, code, err = pkg.ReadFile("config.json")
    print("content =", content)
    print("code =", code)
    print("err =", err)
    if code == 0 then print(#content) else print(err) end

### WriteFile

функция для записи данных в файл на сервере.


code, err = pkg.WriteFile(path, data)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| path     | string | путь внутри шары |
| data     | string | содержимое       |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | code     | integer | 0 = успех                |
| 2   | err      | string  | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.WriteFile("out\\result.txt", "hello from Lua")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.WriteFile("data.json", '{"ok":true}')
    print("code =", code)
    print("err =", err)
    print(code == 0 and "written" or err)

### DeleteFile

функция для удаления файла на сервере.


code, err = pkg.DeleteFile(path)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| path     | string | путь внутри шары |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | code     | integer | 0 = успех                |
| 2   | err      | string  | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.DeleteFile("tmp\\old.txt")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.DeleteFile("out\\processed.csv")
    print("code =", code)
    print("err =", err)
    print(code == 0 and "deleted" or err)


## pkg/syscall

Обёртка системных вызовов. В предоставленном исходнике активные Lua-функции отсутствуют.

0 функций

**Инициализация:** `local pkg = require("pkg/syscall")`

ℹ \`Statfs\` присутствует только в комментарии и не зарегистрирован в Lua-библиотеке, поэтому в список функций не включён.

В предоставленном исходнике нет активных Lua-функций.


## pkg/crypto

Криптографические операции Kalkan: ключи, подписи, XML/CMS, сертификаты.

15 функций

**Инициализация:** `local pkg = require("pkg/crypto")`

ℹ Модуль доступен только в Linux-сборке согласно build tag исходника.

### LoadKey

Загружает ключевой контейнер Kalkan.


err, code = pkg.LoadKey(container, password)

#### Входные параметры

| Параметр  | Тип    | Описание        |
|-----------|--------|-----------------|
| container | string | контейнер ключа |
| password  | string | пароль          |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.LoadKey("/keys/company.p12", "secret")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.LoadKey("/keys/auth.p12", os.getenv and os.getenv("KEY_PASS") or "secret")
    print("err =", err)
    print("code =", code)

### LoadKey2

Загружает ключевой контейнер через альтернативный вариант LoadKey2.


err, code = pkg.LoadKey2(container, password)

#### Входные параметры

| Параметр  | Тип    | Описание        |
|-----------|--------|-----------------|
| container | string | контейнер ключа |
| password  | string | пароль          |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.LoadKey2("/keys/company.p12", "secret")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.LoadKey2("/keys/auth.p12", "secret")
    print("err =", err)
    print("code =", code)

### LoadKey3

Загружает ключевой контейнер через альтернативный вариант LoadKey3.


err, code = pkg.LoadKey3(container, password)

#### Входные параметры

| Параметр  | Тип    | Описание        |
|-----------|--------|-----------------|
| container | string | контейнер ключа |
| password  | string | пароль          |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.LoadKey3("/keys/company.p12", "secret")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.LoadKey3("/keys/auth.p12", "secret")
    print("err =", err)
    print("code =", code)

### SignXml

Подписывает XML-узел по XPath.


result, err, code = pkg.SignXml(xml, signNodeXpath, nodeId)

#### Входные параметры

| Параметр      | Тип             | Описание                  |
|---------------|-----------------|---------------------------|
| xml           | string          | XML                       |
| signNodeXpath | string          | XPath узла                |
| nodeId        | string optional | id узла или пустая строка |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local out, err, code = pkg.SignXml(xml, "//*[local-name()='Document']", "doc-1")
    print("out =", out)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local out, err, code = pkg.SignXml(xml, "/*", "")
    print("out =", out)
    print("err =", err)
    print("code =", code)
    if code == 0 then print(out) end

### SignWSSE

Формирует WS-Security подпись для XML.


result, err, code = pkg.SignWSSE(xml, signNodeXpath, nodeId)

#### Входные параметры

| Параметр      | Тип             | Описание                  |
|---------------|-----------------|---------------------------|
| xml           | string          | XML                       |
| signNodeXpath | string          | XPath узла                |
| nodeId        | string optional | id узла или пустая строка |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local out, err, code = pkg.SignWSSE(xml, "//*[local-name()='Document']", "doc-1")
    print("out =", out)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local out, err, code = pkg.SignWSSE(xml, "/*", "")
    print("out =", out)
    print("err =", err)
    print("code =", code)
    if code == 0 then print(out) end

### SignData

Подписывает произвольные данные с указанными флагами.


result, err, code = pkg.SignData(data, flags)

#### Входные параметры

| Параметр | Тип     | Описание     |
|----------|---------|--------------|
| data     | string  | данные       |
| flags    | integer | флаги Kalkan |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

⚠ Смысл \`flags\` определяется Kalkan API; константы в этом файле не перечислены.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local sign, err, code = pkg.SignData("payload", 0)
    print("sign =", sign)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local sign, err, code = pkg.SignData(jsonBody, 1)
    print("sign =", sign)
    print("err =", err)
    print("code =", code)

### VerifyXml

Проверяет XML-подпись.


err, code = pkg.VerifyXml(xml)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| xml      | string | подписанный XML |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.VerifyXml(signedXml)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.VerifyXml("<root>...</root>")
    print("err =", err)
    print("code =", code)

### VerifyData

Проверяет подпись данных.


err, code = pkg.VerifyData(data, sign)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| data     | string | исходные данные |
| sign     | string | подпись         |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.VerifyData("payload", signature)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.VerifyData(jsonBody, cmsSignature)
    print("err =", err)
    print("code =", code)

### TSASetUrl

Устанавливает URL TSA-сервиса отметки времени.


err, code = pkg.TSASetUrl(url)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| url      | string | URL TSA  |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.TSASetUrl("http://tsp.pki.gov.kz")
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.TSASetUrl("https://tsa.example.kz")
    print("err =", err)
    print("code =", code)

### GetCertFromXml

Извлекает сертификат из подписанного XML.


result, err, code = pkg.GetCertFromXml(xml)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| xml      | string | подписанный XML |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local cert, err, code = pkg.GetCertFromXml(signedXml)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local cert, err, code = pkg.GetCertFromXml(signedXml)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)
    if code == 0 then print(#cert) else print(err) end

### GetCertFromCMS

Извлекает сертификат из CMS-контейнера.


result, err, code = pkg.GetCertFromCMS(cms)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| cms      | string | CMS      |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local cert, err, code = pkg.GetCertFromCMS(cms)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local cert, err, code = pkg.GetCertFromCMS(cms)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)
    if code == 0 then print(#cert) else print(err) end

### GetCertFromCMS2

Извлекает сертификат указанной подписи из CMS-контейнера.


result, err, code = pkg.GetCertFromCMS2(cms, signNum)

#### Входные параметры

| Параметр | Тип     | Описание      |
|----------|---------|---------------|
| cms      | string  | CMS           |
| signNum  | integer | номер подписи |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local cert, err, code = pkg.GetCertFromCMS2(cms, 0)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local cert, err, code = pkg.GetCertFromCMS2(cms, 1)
    print("cert =", cert)
    print("err =", err)
    print("code =", code)

### LoadCertificateFromFile

Загружает сертификат из файла.


err, code = pkg.LoadCertificateFromFile(filename, certType)

#### Входные параметры

| Параметр | Тип     | Описание           |
|----------|---------|--------------------|
| filename | string  | путь к сертификату |
| certType | integer | тип сертификата    |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.LoadCertificateFromFile("/certs/root.cer", 1)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.LoadCertificateFromFile("/certs/intermediate.cer", 2)
    print("err =", err)
    print("code =", code)

### CertificateGetInfo

Получает свойство сертификата по числовому идентификатору.


result, err, code = pkg.CertificateGetInfo(certificate, propId)

#### Входные параметры

| Параметр    | Тип     | Описание    |
|-------------|---------|-------------|
| certificate | string  | сертификат  |
| propId      | integer | id свойства |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | result   | string\|nil | результат операции |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

⚠ Допустимые \`propId\` в предоставленном модуле не перечислены; они определяются Kalkan API.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.CertificateGetInfo(cert, 1)
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.CertificateGetInfo(cert, 2)
    print("value =", value)
    print("err =", err)
    print("code =", code)

### RSAValidateXml

Проверяет XML Digital Signature через RSA/XMLDSig валидатор.


err, code = pkg.RSAValidateXml(xml)

#### Входные параметры

| Параметр | Тип    | Описание      |
|----------|--------|---------------|
| xml      | string | XML с XMLDSig |

#### Результирующие параметры

| №   | Значение | Тип         | Описание            |
|-----|----------|-------------|---------------------|
| 1   | err      | string\|nil | nil/пусто на успехе |
| 2   | code     | integer     | 0 = успех           |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.RSAValidateXml(signedXml)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.RSAValidateXml("<doc>...</doc>")
    print("err =", err)
    print("code =", code)


## pkg/gokalkan

Подписание XML через отдельный клиент gokalkan.

1 функций

**Инициализация:** `local pkg = require("pkg/gokalkan")`

ℹ Модуль доступен только в Linux-сборке согласно build tag исходника.

### signXml

Загружает хранилище ключей, подписывает XML и закрывает клиент после операции.


signedXml, err, code = pkg.signXml(certPath, certPassword, xml, alias, flag, signNodeID)

#### Входные параметры

| Параметр     | Тип     | Описание                |
|--------------|---------|-------------------------|
| certPath     | string  | путь к хранилищу ключей |
| certPassword | string  | пароль                  |
| xml          | string  | XML                     |
| alias        | string  | alias ключа             |
| flag         | integer | флаг подписи            |
| signNodeID   | string  | id подписываемого узла  |

#### Результирующие параметры

| №   | Значение  | Тип     | Описание                 |
|-----|-----------|---------|--------------------------|
| 1   | signedXml | string  | подписанный XML          |
| 2   | err       | string  | ошибка или пустая строка |
| 3   | code      | integer | 0 = успех                |

⚠ Используются production options gokalkan; клиент создаётся и закрывается на каждый вызов.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local signed, err, code = pkg.signXml("/keys/company.p12", "secret", xml, "SIGN", 0, "doc-1")
    print("signed =", signed)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local signed, err, code = pkg.signXml("/keys/company.p12", "secret", xml, "AUTH", 0, "")
    print("signed =", signed)
    print("err =", err)
    print("code =", code)
    if code == 0 then print(signed) end


## pkg/xml

XML/XPath/XSD: извлечение/вставка XML, атрибуты и проверка по XSD.

5 функций

**Инициализация:** `local pkg = require("pkg/xml")`

ℹ Модуль представлен Linux-реализацией в предоставленном исходнике.

### ParseSchema

Компилирует XSD и возвращает объект с методами Validate и Free.


schema, err, code = pkg.ParseSchema(schemaText)

#### Входные параметры

| Параметр   | Тип    | Описание  |
|------------|--------|-----------|
| schemaText | string | XSD-схема |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                                     |
|-----|----------|------------|----------------------------------------------|
| 1   | schema   | table\|nil | объект с методами Validate(xmlText) и Free() |
| 2   | err      | string     | ошибка или пустая строка                     |
| 3   | code     | integer    | 0 = успех                                    |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local schema, err, code = pkg.ParseSchema(xsdText)
    print("schema =", schema)
    print("err =", err)
    print("code =", code)
    if code == 0 then local errors, vcode = schema.Validate(xmlText); print(errors, vcode); schema.Free() end

**Пример 2**


    local schema, err, code = pkg.ParseSchema("<xs:schema xmlns:xs=\"http://www.w3.org/2001/XMLSchema\"></xs:schema>")
    print("schema =", schema)
    print("err =", err)
    print("code =", code)
    if schema then schema.Free() end

### ExtractXml

Находит XML-узел по XPath, удаляет его из документа и возвращает найденный узел и оставшийся XML.


foundXml, containerXml, err, code = pkg.ExtractXml(xml, namespaces, xpath)

#### Входные параметры

| Параметр   | Тип                    | Описание       |
|------------|------------------------|----------------|
| xml        | string                 | XML            |
| namespaces | table\<string,string\> | prefix -\> URI |
| xpath      | string                 | XPath          |

#### Результирующие параметры

| №   | Значение     | Тип         | Описание                              |
|-----|--------------|-------------|---------------------------------------|
| 1   | foundXml     | string      | найденный XML-узел                    |
| 2   | containerXml | string      | исходный документ без найденного узла |
| 3   | err          | string\|nil | nil на успехе                         |
| 4   | code         | integer     | 0 = успех                             |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local found, rest, err, code = pkg.ExtractXml(xml, {ds="http://www.w3.org/2000/09/xmldsig#"}, "//ds:Signature")
    print("found =", found)
    print("rest =", rest)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local found, rest, err, code = pkg.ExtractXml(xml, {}, "//Item[1]")
    print("found =", found)
    print("rest =", rest)
    print("err =", err)
    print("code =", code)

### InsertXml

Вставляет дочерний XML в узел, найденный по XPath.


xml, err, code = pkg.InsertXml(xml, namespaces, xpath, childXml)

#### Входные параметры

| Параметр   | Тип                    | Описание                            |
|------------|------------------------|-------------------------------------|
| xml        | string                 | XML-контейнер                       |
| namespaces | table\<string,string\> | prefix -\> URI                      |
| xpath      | string                 | XPath родителя                      |
| childXml   | string                 | XML вставляемого дочернего элемента |

#### Результирующие параметры

| №   | Значение | Тип         | Описание           |
|-----|----------|-------------|--------------------|
| 1   | xml      | string      | результирующий XML |
| 2   | err      | string\|nil | nil на успехе      |
| 3   | code     | integer     | 0 = успех          |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local out, err, code = pkg.InsertXml("<root></root>", {}, "/root", "<item id='1'>A</item>")
    print("out =", out)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local out, err, code = pkg.InsertXml(xml, {x="urn:test"}, "//x:items", "<item>new</item>")
    print("out =", out)
    print("err =", err)
    print("code =", code)

### GetAttr

Читает атрибут первого XML-элемента, найденного по XPath.


value, err, code = pkg.GetAttr(xml, namespaces, xpath, attrName)

#### Входные параметры

| Параметр   | Тип                    | Описание       |
|------------|------------------------|----------------|
| xml        | string                 | XML            |
| namespaces | table\<string,string\> | prefix -\> URI |
| xpath      | string                 | XPath элемента |
| attrName   | string                 | имя атрибута   |

#### Результирующие параметры

| №   | Значение | Тип         | Описание          |
|-----|----------|-------------|-------------------|
| 1   | value    | string      | значение атрибута |
| 2   | err      | string\|nil | nil на успехе     |
| 3   | code     | integer     | 0 = успех         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.GetAttr("<item id='501'/>", {}, "/item", "id")
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.GetAttr(xml, {x="urn:test"}, "//x:item", "status")
    print("value =", value)
    print("err =", err)
    print("code =", code)

### SetAttr

Устанавливает атрибут первого XML-элемента, найденного по XPath.


xml, err, code = pkg.SetAttr(xml, namespaces, xpath, attrName, value)

#### Входные параметры

| Параметр   | Тип                    | Описание       |
|------------|------------------------|----------------|
| xml        | string                 | XML            |
| namespaces | table\<string,string\> | prefix -\> URI |
| xpath      | string                 | XPath элемента |
| attrName   | string                 | имя атрибута   |
| value      | string                 | новое значение |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                   |
|-----|----------|-------------|----------------------------|
| 1   | xml      | string      | XML с изменённым атрибутом |
| 2   | err      | string\|nil | nil на успехе              |
| 3   | code     | integer     | 0 = успех                  |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local out, err, code = pkg.SetAttr("<item id='1'/>", {}, "/item", "id", "501")
    print("out =", out)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local out, err, code = pkg.SetAttr(xml, {x="urn:test"}, "//x:item", "status", "NEW")
    print("out =", out)
    print("err =", err)
    print("code =", code)


## pkg/mongodb

MongoDB: подключение, поиск, агрегации и CRUD через Extended JSON.

13 функций

**Инициализация:** `local pkg = require("pkg/mongodb")`

ℹ Фильтры, документы и pipeline передаются строками Extended JSON.

### connect

Подключается к MongoDB по URI и возвращает id соединения.


connectionId, err, code = pkg.connect(uri)

#### Входные параметры

| Параметр | Тип    | Описание    |
|----------|--------|-------------|
| uri      | string | MongoDB URI |

#### Результирующие параметры

| №   | Значение     | Тип         | Описание                 |
|-----|--------------|-------------|--------------------------|
| 1   | connectionId | string\|nil | id соединения            |
| 2   | err          | string      | ошибка или пустая строка |
| 3   | code         | integer     | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local db, err, code = pkg.connect("mongodb://user:pass@mongo:27017/?authSource=admin")
    print("db =", db)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local db, err, code = pkg.connect("mongodb://127.0.0.1:27017")
    print("db =", db)
    print("err =", err)
    print("code =", code)
    print("mongo id:", db, code, err)

### find

Возвращает все документы по Extended JSON фильтру.


result, err, code = pkg.find(connectionId, database, collection, filter)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                     |
|-----|----------|------------|------------------------------|
| 1   | result   | table\|nil | массив документов/метаданных |
| 2   | err      | string     | ошибка или пустая строка     |
| 3   | code     | integer    | 0 = успех                    |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local docs, err, code = pkg.find(db, "app", "orders", '{"state":"NEW"}')
    print("docs =", docs)
    print("err =", err)
    print("code =", code)
    if docs then for _, d in ipairs(docs) do print(d.state) end end

**Пример 2**


    local docs, err, code = pkg.find(db, "app", "orders", '{"amount":{"$gte":1000}}')
    print("docs =", docs)
    print("err =", err)
    print("code =", code)
    print(docs and #docs or 0, err, code)

### findOne

Возвращает один документ по Extended JSON фильтру.


document, err, code = pkg.findOne(connectionId, database, collection, filter)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                 |
|-----|----------|-------------|--------------------------|
| 1   | document | string\|nil | документ в Extended JSON |
| 2   | err      | string      | ошибка или пустая строка |
| 3   | code     | integer     | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local doc, err, code = pkg.findOne(db, "app", "orders", '{"number":"A-501"}')
    print("doc =", doc)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local doc, err, code = pkg.findOne(db, "app", "users", '{"login":"eldar"}')
    print("doc =", doc)
    print("err =", err)
    print("code =", code)

### count

Считает документы по фильтру.


result, err, code = pkg.count(connectionId, database, collection, filter)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local count, err, code = pkg.count(db, "app", "orders", '{"state":"NEW"}')
    print("count =", count)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local count, err, code = pkg.count(db, "app", "orders", '{}')
    print("count =", count)
    print("err =", err)
    print("code =", code)
    print("all:", count, code, err)

### aggregate

Выполняет pipeline агрегации.


result, err, code = pkg.aggregate(connectionId, database, collection, pipeline)

#### Входные параметры

| Параметр     | Тип    | Описание                    |
|--------------|--------|-----------------------------|
| connectionId | string | id соединения               |
| database     | string | база                        |
| collection   | string | коллекция                   |
| pipeline     | string | Extended JSON массив стадий |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                     |
|-----|----------|------------|------------------------------|
| 1   | result   | table\|nil | массив документов/метаданных |
| 2   | err      | string     | ошибка или пустая строка     |
| 3   | code     | integer    | 0 = успех                    |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local rows, err, code = pkg.aggregate(db, "app", "orders", '[{"$match":{"state":"NEW"}},{"$group":{"_id":"$customerId","total":{"$sum":"$amount"}}}]')
    print("rows =", rows)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local rows, err, code = pkg.aggregate(db, "app", "orders", '[{"$sort":{"createdAt":-1}},{"$limit":10}]')
    print("rows =", rows)
    print("err =", err)
    print("code =", code)
    print(rows and #rows or 0, err, code)

### insert

Вставляет один документ.


result, err, code = pkg.insert(connectionId, database, collection, document)

#### Входные параметры

| Параметр     | Тип    | Описание               |
|--------------|--------|------------------------|
| connectionId | string | id соединения          |
| database     | string | база                   |
| collection   | string | коллекция              |
| document     | string | Extended JSON документ |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local id, err, code = pkg.insert(db, "app", "orders", '{"number":"A-501","state":"NEW"}')
    print("id =", id)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local id, err, code = pkg.insert(db, "app", "audit", '{"event":"LOGIN"}')
    print("id =", id)
    print("err =", err)
    print("code =", code)

### update

Обновляет один документ.


result, err, code = pkg.update(connectionId, database, collection, filter, update)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |
| update       | string | Extended JSON update |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local modified, err, code = pkg.update(db, "app", "orders", '{"number":"A-501"}', '{"$set":{"state":"DONE"}}')
    print("modified =", modified)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local modified, err, code = pkg.update(db, "app", "users", '{"login":"eldar"}', '{"$inc":{"loginCount":1}}')
    print("modified =", modified)
    print("err =", err)
    print("code =", code)

### delete

Удаляет один документ.


result, err, code = pkg.delete(connectionId, database, collection, filter)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local deleted, err, code = pkg.delete(db, "app", "orders", '{"number":"A-501"}')
    print("deleted =", deleted)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local deleted, err, code = pkg.delete(db, "app", "sessions", '{"expired":true}')
    print("deleted =", deleted)
    print("err =", err)
    print("code =", code)

### updateMany

Обновляет несколько документов.


result, err, code = pkg.updateMany(connectionId, database, collection, filter, update)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |
| update       | string | Extended JSON update |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local modified, err, code = pkg.updateMany(db, "app", "orders", '{"state":"NEW"}', '{"$set":{"checked":true}}')
    print("modified =", modified)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local modified, err, code = pkg.updateMany(db, "app", "users", '{"active":true}', '{"$inc":{"version":1}}')
    print("modified =", modified)
    print("err =", err)
    print("code =", code)

### deleteMany

Удаляет несколько документов.


result, err, code = pkg.deleteMany(connectionId, database, collection, filter)

#### Входные параметры

| Параметр     | Тип    | Описание             |
|--------------|--------|----------------------|
| connectionId | string | id соединения        |
| database     | string | база                 |
| collection   | string | коллекция            |
| filter       | string | Extended JSON фильтр |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local deleted, err, code = pkg.deleteMany(db, "app", "sessions", '{"expired":true}')
    print("deleted =", deleted)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local deleted, err, code = pkg.deleteMany(db, "app", "tmp", '{}')
    print("deleted =", deleted)
    print("err =", err)
    print("code =", code)

### insertMany

Вставляет несколько документов.


result, err, code = pkg.insertMany(connectionId, database, collection, documents)

#### Входные параметры

| Параметр     | Тип    | Описание                        |
|--------------|--------|---------------------------------|
| connectionId | string | id соединения                   |
| database     | string | база                            |
| collection   | string | коллекция                       |
| documents    | string | Extended JSON массив документов |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                      |
|-----|----------|-------------|-------------------------------|
| 1   | result   | string\|nil | count/id/список id как строка |
| 2   | err      | string      | ошибка или пустая строка      |
| 3   | code     | integer     | 0 = успех                     |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ids, err, code = pkg.insertMany(db, "app", "orders", '[{"number":"A-1"},{"number":"A-2"}]')
    print("ids =", ids)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local ids, err, code = pkg.insertMany(db, "app", "audit", '[{"event":"A"},{"event":"B"}]')
    print("ids =", ids)
    print("err =", err)
    print("code =", code)

### listCollections

Возвращает метаданные коллекций базы.


result, err, code = pkg.listCollections(connectionId, database)

#### Входные параметры

| Параметр     | Тип    | Описание      |
|--------------|--------|---------------|
| connectionId | string | id соединения |
| database     | string | база          |

#### Результирующие параметры

| №   | Значение | Тип        | Описание                     |
|-----|----------|------------|------------------------------|
| 1   | result   | table\|nil | массив документов/метаданных |
| 2   | err      | string     | ошибка или пустая строка     |
| 3   | code     | integer    | 0 = успех                    |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local cols, err, code = pkg.listCollections(db, "app")
    print("cols =", cols)
    print("err =", err)
    print("code =", code)
    if cols then for _, c in ipairs(cols) do print(c.name) end end

**Пример 2**


    local cols, err, code = pkg.listCollections(db, "admin")
    print("cols =", cols)
    print("err =", err)
    print("code =", code)
    print(cols and #cols or 0, err, code)

### close

Закрывает MongoDB-соединение.


err, code = pkg.close(connectionId)

#### Входные параметры

| Параметр     | Тип    | Описание      |
|--------------|--------|---------------|
| connectionId | string | id соединения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | err      | string  | ошибка или пустая строка |
| 2   | code     | integer | 0 = успех                |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err, code = pkg.close(db)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local err, code = pkg.close(db)
    print("err =", err)
    print("code =", code)
    if code ~= 0 then print(err) end


## pkg/redis

Redis-команды для строк, ключей, hash/list/set/zset, Pub/Sub и служебных операций.

62 функций

**Инициализация:** `local pkg = require("pkg/redis")`

ℹ Для работы должны быть заданы \`DAMU_REDIS_ADDR\` и непустой \`DAMU_REDIS_PREFIX\`; префикс \`\_\` запрещён. Пароль берётся из \`DAMU_REDIS_PASSWORD\`.

ℹ Модуль автоматически добавляет \`DAMU_REDIS_PREFIX\` к ключам.

### Set

Устанавливает .


code, errMsg = pkg.Set(key, value, ttlSeconds)

#### Входные параметры

| Параметр   | Тип     | Описание       |
|------------|---------|----------------|
| key        | string  | ключ           |
| value      | string  | значение       |
| ttlSeconds | integer | TTL в секундах |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.Set("session:501", "active")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.Set("otp:501", "783211", 120)
    print("code =", code)
    print("err =", err)

### Get

Получает .


value, errMsg, code = pkg.Get(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                  |
|-----|----------|---------|---------------------------|
| 1   | value    | string  | значение                  |
| 2   | errMsg   | string  | ошибка или пустая строка  |
| 3   | code     | integer | 0 на успехе; при ошибке 1 |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err, code = pkg.Get("session:501")
    print("value =", value)
    print("err =", err)
    print("code =", code)

**Пример 2**


    local value, err, code = pkg.Get("missing-key")
    print("value =", value)
    print("err =", err)
    print("code =", code)

### SetNX

Устанавливает NX.


set, errMsg = pkg.SetNX(key, value, ttlSeconds)

#### Входные параметры

| Параметр   | Тип     | Описание       |
|------------|---------|----------------|
| key        | string  | ключ           |
| value      | string  | значение       |
| ttlSeconds | integer | TTL в секундах |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | set      | boolean | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ok, err = pkg.SetNX("lock:order:501", "worker-1", 30)
    print("ok =", ok)
    print("err =", err)

**Пример 2**


    local ok, err = pkg.SetNX("once:migrate", "1")
    print("ok =", ok)
    print("err =", err)
    print(ok and "created" or "already exists", err)

### SetEX

Устанавливает EX.


code, errMsg = pkg.SetEX(key, value, ttlSeconds)

#### Входные параметры

| Параметр   | Тип     | Описание       |
|------------|---------|----------------|
| key        | string  | ключ           |
| value      | string  | значение       |
| ttlSeconds | integer | TTL в секундах |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.SetEX("token:501", "abc", 3600)
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.SetEX("cache:user:1", '{"name":"Ayan"}', 60)
    print("code =", code)
    print("err =", err)

### MSet

Выполняет операцию MSet.


code, errMsg = pkg.MSet(key1, val1, ...)

#### Входные параметры

| Параметр | Тип    | Описание                                                           |
|----------|--------|--------------------------------------------------------------------|
| key1     | string | ключ                                                               |
| val1     | string | значение                                                           |
| ...      | pairs  | дополнительные пары key,value; число аргументов должно быть чётным |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.MSet("a", "1", "b", "2")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.MSet("user:1:name", "Ayan", "user:1:state", "ACTIVE")
    print("code =", code)
    print("err =", err)

### MGet

Выполняет операцию MGet.


table_of_values, errMsg = pkg.MGet(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение        | Тип | Описание                 |
|-----|-----------------|-----|--------------------------|
| 1   | table_of_values | any | результат команды        |
| 2   | errMsg          | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local values, err = pkg.MGet("a", "b", "c")
    print("values =", values)
    print("err =", err)
    for i,v in ipairs(values or {}) do print(i,v) end

**Пример 2**


    local values, err = pkg.MGet("user:1:name", "user:1:state")
    print("values =", values)
    print("err =", err)
    print(values and values[1], values and values[2], err)

### Incr

Выполняет операцию Incr.


newValue, errMsg = pkg.Incr(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | newValue | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Incr("counter:orders")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Incr("rate:user:501")
    print("n =", n)
    print("err =", err)
    print("new value:", n, err)

### IncrBy

Выполняет операцию IncrBy.


newValue, errMsg = pkg.IncrBy(key, amount)

#### Входные параметры

| Параметр | Тип     | Описание        |
|----------|---------|-----------------|
| key      | string  | ключ            |
| amount   | integer | число изменения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | newValue | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.IncrBy("balance:points", 10)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.IncrBy("counter:bytes", 1024)
    print("n =", n)
    print("err =", err)

### Decr

Выполняет операцию Decr.


newValue, errMsg = pkg.Decr(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | newValue | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Decr("stock:sku-1")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Decr("attempts:501")
    print("n =", n)
    print("err =", err)

### DecrBy

Выполняет операцию DecrBy.


newValue, errMsg = pkg.DecrBy(key, amount)

#### Входные параметры

| Параметр | Тип     | Описание        |
|----------|---------|-----------------|
| key      | string  | ключ            |
| amount   | integer | число изменения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | newValue | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.DecrBy("stock:sku-1", 5)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.DecrBy("quota:501", 100)
    print("n =", n)
    print("err =", err)

### Append

Выполняет операцию Append.


newLength, errMsg = pkg.Append(key, value)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| value    | string | значение |

#### Результирующие параметры

| №   | Значение  | Тип     | Описание                 |
|-----|-----------|---------|--------------------------|
| 1   | newLength | integer | результат команды        |
| 2   | errMsg    | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Append("log:501", ";DONE")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Append("buffer", " world")
    print("n =", n)
    print("err =", err)
    print("length:", n, err)

### GetSet

Получает Set.


oldValue, errMsg = pkg.GetSet(key, newValue)

#### Входные параметры

| Параметр | Тип    | Описание               |
|----------|--------|------------------------|
| key      | string | ключ                   |
| newValue | string | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | oldValue | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local old, err = pkg.GetSet("current:leader", "worker-2")
    print("old =", old)
    print("err =", err)

**Пример 2**


    local old, err = pkg.GetSet("config:version", "43")
    print("old =", old)
    print("err =", err)
    print("old:", old, err)

### Del

Выполняет операцию Del.


deletedCount, errMsg = pkg.Del(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение     | Тип     | Описание                 |
|-----|--------------|---------|--------------------------|
| 1   | deletedCount | integer | результат команды        |
| 2   | errMsg       | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Del("a", "b", "c")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Del("session:501")
    print("n =", n)
    print("err =", err)
    print("deleted:", n, err)

### Exists

Выполняет операцию Exists.


count, errMsg = pkg.Exists(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | count    | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Exists("a", "b")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Exists("session:501")
    print("n =", n)
    print("err =", err)
    print(n == 1, err)

### Expire

Выполняет операцию Expire.


set, errMsg = pkg.Expire(key, ttlSeconds)

#### Входные параметры

| Параметр   | Тип     | Описание       |
|------------|---------|----------------|
| key        | string  | ключ           |
| ttlSeconds | integer | TTL в секундах |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | set      | boolean | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ok, err = pkg.Expire("session:501", 1800)
    print("ok =", ok)
    print("err =", err)

**Пример 2**


    local ok, err = pkg.Expire("cache:report", 60)
    print("ok =", ok)
    print("err =", err)
    print(ok and "TTL set" or "missing", err)

### TTL

Выполняет операцию TTL.


ttlSeconds, errMsg = pkg.TTL(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение   | Тип     | Описание                 |
|-----|------------|---------|--------------------------|
| 1   | ttlSeconds | integer | результат команды        |
| 2   | errMsg     | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ttl, err = pkg.TTL("session:501")
    print("ttl =", ttl)
    print("err =", err)

**Пример 2**


    local ttl, err = pkg.TTL("persistent:key")
    print("ttl =", ttl)
    print("err =", err)
    print("ttl:", ttl, err)

### Persist

Выполняет операцию Persist.


removed, errMsg = pkg.Persist(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | removed  | boolean | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ok, err = pkg.Persist("session:501")
    print("ok =", ok)
    print("err =", err)

**Пример 2**


    local ok, err = pkg.Persist("cache:report")
    print("ok =", ok)
    print("err =", err)
    print(ok and "TTL removed" or "unchanged", err)

### Rename

Выполняет операцию Rename.


code, errMsg = pkg.Rename(oldKey, newKey)

#### Входные параметры

| Параметр | Тип    | Описание               |
|----------|--------|------------------------|
| oldKey   | string | аргумент команды Redis |
| newKey   | string | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.Rename("old:key", "new:key")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.Rename("tmp:501", "order:501")
    print("code =", code)
    print("err =", err)

### Type

Выполняет операцию Type.


typeStr, errMsg = pkg.Type(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | typeStr  | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local typ, err = pkg.Type("session:501")
    print("typ =", typ)
    print("err =", err)

**Пример 2**


    local typ, err = pkg.Type("orders:list")
    print("typ =", typ)
    print("err =", err)
    print("redis type:", typ, err)

### Keys

Выполняет операцию Keys.


table_of_keys, errMsg = pkg.Keys(pattern)

#### Входные параметры

| Параметр | Тип    | Описание               |
|----------|--------|------------------------|
| pattern  | string | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение      | Тип | Описание                 |
|-----|---------------|-----|--------------------------|
| 1   | table_of_keys | any | результат команды        |
| 2   | errMsg        | any | ошибка или пустая строка |

⚠ Префикс \`DAMU_REDIS_PREFIX\` добавляется к pattern и удаляется из возвращаемых ключей.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local keys, err = pkg.Keys("session:*")
    print("keys =", keys)
    print("err =", err)
    for _, k in ipairs(keys or {}) do print(k) end

**Пример 2**


    local keys, err = pkg.Keys("cache:user:*")
    print("keys =", keys)
    print("err =", err)
    print("count:", keys and #keys or 0, err)

### HSet

Выполняет операцию HSet.


code, errMsg = pkg.HSet(key, field, value, ...pairs)

#### Входные параметры

| Параметр | Тип       | Описание                        |
|----------|-----------|---------------------------------|
| key      | string    | ключ hash                       |
| field    | string    | поле                            |
| value    | string    | значение                        |
| ...pairs | string... | дополнительные пары field,value |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.HSet("user:501", "name", "Ayan", "state", "ACTIVE")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.HSet("order:501", "state", "NEW")
    print("code =", code)
    print("err =", err)

### HGet

Выполняет операцию HGet.


value, errMsg = pkg.HGet(key, field)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| field    | string | поле     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | value    | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local value, err = pkg.HGet("user:501", "name")
    print("value =", value)
    print("err =", err)

**Пример 2**


    local value, err = pkg.HGet("order:501", "state")
    print("value =", value)
    print("err =", err)

### HGetAll

Выполняет операцию HGetAll.


table, errMsg = pkg.HGetAll(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | table    | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local t, err = pkg.HGetAll("user:501")
    print("t =", t)
    print("err =", err)
    if t then for k,v in pairs(t) do print(k,v) end end

**Пример 2**


    local t, err = pkg.HGetAll("order:501")
    print("t =", t)
    print("err =", err)
    print(t and t.state, err)

### HDel

Выполняет операцию HDel.


deletedCount, errMsg = pkg.HDel(key, field1, ...fields)

#### Входные параметры

| Параметр  | Тип       | Описание            |
|-----------|-----------|---------------------|
| key       | string    | ключ hash           |
| field1    | string    | первое поле         |
| ...fields | string... | дополнительные поля |

#### Результирующие параметры

| №   | Значение     | Тип | Описание                 |
|-----|--------------|-----|--------------------------|
| 1   | deletedCount | any | результат команды        |
| 2   | errMsg       | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.HDel("user:501", "temp", "oldField")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.HDel("order:501", "debug")
    print("n =", n)
    print("err =", err)

### HExists

Выполняет операцию HExists.


exists, errMsg = pkg.HExists(key, field)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| field    | string | поле     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | exists   | boolean | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ok, err = pkg.HExists("user:501", "email")
    print("ok =", ok)
    print("err =", err)

**Пример 2**


    local ok, err = pkg.HExists("order:501", "state")
    print("ok =", ok)
    print("err =", err)
    print(ok and "has state" or "no state", err)

### HLen

Выполняет операцию HLen.


length, errMsg = pkg.HLen(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | length   | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.HLen("user:501")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.HLen("order:501")
    print("n =", n)
    print("err =", err)
    print("fields:", n, err)

### HIncrBy

Выполняет операцию HIncrBy.


newValue, errMsg = pkg.HIncrBy(key, field, amount)

#### Входные параметры

| Параметр | Тип     | Описание        |
|----------|---------|-----------------|
| key      | string  | ключ            |
| field    | string  | поле            |
| amount   | integer | число изменения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | newValue | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.HIncrBy("stats:501", "views", 1)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.HIncrBy("user:501", "points", 10)
    print("n =", n)
    print("err =", err)

### HKeys

Выполняет операцию HKeys.


table_of_fields, errMsg = pkg.HKeys(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение        | Тип | Описание                 |
|-----|-----------------|-----|--------------------------|
| 1   | table_of_fields | any | результат команды        |
| 2   | errMsg          | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local fields, err = pkg.HKeys("user:501")
    print("fields =", fields)
    print("err =", err)
    for _, f in ipairs(fields or {}) do print(f) end

**Пример 2**


    local fields, err = pkg.HKeys("order:501")
    print("fields =", fields)
    print("err =", err)
    print(fields and #fields or 0, err)

### HVals

Выполняет операцию HVals.


table_of_values, errMsg = pkg.HVals(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение        | Тип | Описание                 |
|-----|-----------------|-----|--------------------------|
| 1   | table_of_values | any | результат команды        |
| 2   | errMsg          | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local values, err = pkg.HVals("user:501")
    print("values =", values)
    print("err =", err)
    for _, v in ipairs(values or {}) do print(v) end

**Пример 2**


    local values, err = pkg.HVals("order:501")
    print("values =", values)
    print("err =", err)
    print(values and #values or 0, err)

### HMGet

Выполняет операцию HMGet.


table_of_values, errMsg = pkg.HMGet(key, field1, ...fields)

#### Входные параметры

| Параметр  | Тип       | Описание            |
|-----------|-----------|---------------------|
| key       | string    | ключ hash           |
| field1    | string    | первое поле         |
| ...fields | string... | дополнительные поля |

#### Результирующие параметры

| №   | Значение        | Тип | Описание                 |
|-----|-----------------|-----|--------------------------|
| 1   | table_of_values | any | результат команды        |
| 2   | errMsg          | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local values, err = pkg.HMGet("user:501", "name", "email")
    print("values =", values)
    print("err =", err)
    print(values and values[1], values and values[2], err)

**Пример 2**


    local values, err = pkg.HMGet("order:501", "state", "number")
    print("values =", values)
    print("err =", err)

### LPush

Выполняет операцию LPush.


length, errMsg = pkg.LPush(key, value1, ...values)

#### Входные параметры

| Параметр  | Тип       | Описание                |
|-----------|-----------|-------------------------|
| key       | string    | ключ списка             |
| value1    | string    | первое значение         |
| ...values | string... | дополнительные значения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | length   | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.LPush("queue:jobs", "job3", "job2", "job1")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.LPush("recent:501", "A")
    print("n =", n)
    print("err =", err)

### RPush

Выполняет операцию RPush.


length, errMsg = pkg.RPush(key, value1, ...values)

#### Входные параметры

| Параметр  | Тип       | Описание                |
|-----------|-----------|-------------------------|
| key       | string    | ключ списка             |
| value1    | string    | первое значение         |
| ...values | string... | дополнительные значения |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | length   | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.RPush("queue:jobs", "job1", "job2")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.RPush("events:501", "DONE")
    print("n =", n)
    print("err =", err)

### LPop

Выполняет операцию LPop.


value, errMsg = pkg.LPop(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | value    | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local v, err = pkg.LPop("queue:jobs")
    print("v =", v)
    print("err =", err)

**Пример 2**


    local v, err = pkg.LPop("recent:501")
    print("v =", v)
    print("err =", err)
    print(v or "empty", err)

### RPop

Выполняет операцию RPop.


value, errMsg = pkg.RPop(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | value    | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local v, err = pkg.RPop("queue:jobs")
    print("v =", v)
    print("err =", err)

**Пример 2**


    local v, err = pkg.RPop("events:501")
    print("v =", v)
    print("err =", err)
    print(v or "empty", err)

### LLen

Выполняет операцию LLen.


length, errMsg = pkg.LLen(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | length   | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.LLen("queue:jobs")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.LLen("recent:501")
    print("n =", n)
    print("err =", err)
    print("items:", n, err)

### LRange

Выполняет операцию LRange.


table_of_values, errMsg = pkg.LRange(key, start, stop)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| start    | integer | начальный индекс       |
| stop     | integer | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение        | Тип | Описание                 |
|-----|-----------------|-----|--------------------------|
| 1   | table_of_values | any | результат команды        |
| 2   | errMsg          | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local values, err = pkg.LRange("queue:jobs", 0, -1)
    print("values =", values)
    print("err =", err)
    for _,v in ipairs(values or {}) do print(v) end

**Пример 2**


    local values, err = pkg.LRange("recent:501", 0, 9)
    print("values =", values)
    print("err =", err)
    print(values and #values or 0, err)

### LIndex

Выполняет операцию LIndex.


value, errMsg = pkg.LIndex(key, index)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| index    | integer | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | value    | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local v, err = pkg.LIndex("queue:jobs", 0)
    print("v =", v)
    print("err =", err)

**Пример 2**


    local v, err = pkg.LIndex("recent:501", -1)
    print("v =", v)
    print("err =", err)

### LSet

Выполняет операцию LSet.


code, errMsg = pkg.LSet(key, index, value)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| index    | integer | аргумент команды Redis |
| value    | string  | значение               |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.LSet("queue:jobs", 0, "job-updated")
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.LSet("recent:501", 1, "B")
    print("code =", code)
    print("err =", err)

### LRem

Выполняет операцию LRem.


removedCount, errMsg = pkg.LRem(key, count, value)

#### Входные параметры

| Параметр | Тип     | Описание   |
|----------|---------|------------|
| key      | string  | ключ       |
| count    | integer | количество |
| value    | string  | значение   |

#### Результирующие параметры

| №   | Значение     | Тип     | Описание                 |
|-----|--------------|---------|--------------------------|
| 1   | removedCount | integer | результат команды        |
| 2   | errMsg       | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.LRem("queue:jobs", 0, "obsolete")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.LRem("recent:501", 1, "A")
    print("n =", n)
    print("err =", err)

### LTrim

Выполняет операцию LTrim.


code, errMsg = pkg.LTrim(key, start, stop)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| start    | integer | начальный индекс       |
| stop     | integer | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.LTrim("recent:501", 0, 99)
    print("code =", code)
    print("err =", err)

**Пример 2**


    local code, err = pkg.LTrim("queue:jobs", 0, 999)
    print("code =", code)
    print("err =", err)

### SAdd

Выполняет операцию SAdd.


addedCount, errMsg = pkg.SAdd(key, member1, ...members)

#### Входные параметры

| Параметр   | Тип       | Описание                |
|------------|-----------|-------------------------|
| key        | string    | ключ                    |
| member1    | string    | первый элемент          |
| ...members | string... | дополнительные элементы |

#### Результирующие параметры

| №   | Значение   | Тип     | Описание                 |
|-----|------------|---------|--------------------------|
| 1   | addedCount | integer | результат команды        |
| 2   | errMsg     | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.SAdd("roles:501", "admin", "editor")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.SAdd("online", "user501")
    print("n =", n)
    print("err =", err)

### SRem

Выполняет операцию SRem.


removedCount, errMsg = pkg.SRem(key, member1, ...members)

#### Входные параметры

| Параметр   | Тип       | Описание                |
|------------|-----------|-------------------------|
| key        | string    | ключ                    |
| member1    | string    | первый элемент          |
| ...members | string... | дополнительные элементы |

#### Результирующие параметры

| №   | Значение     | Тип     | Описание                 |
|-----|--------------|---------|--------------------------|
| 1   | removedCount | integer | результат команды        |
| 2   | errMsg       | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.SRem("roles:501", "editor")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.SRem("online", "user501")
    print("n =", n)
    print("err =", err)

### SIsMember

Выполняет операцию SIsMember.


isMember, errMsg = pkg.SIsMember(key, member)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| member   | string | элемент  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | isMember | boolean | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local ok, err = pkg.SIsMember("roles:501", "admin")
    print("ok =", ok)
    print("err =", err)

**Пример 2**


    local ok, err = pkg.SIsMember("online", "user501")
    print("ok =", ok)
    print("err =", err)
    print(ok and "online" or "offline", err)

### SMembers

Выполняет операцию SMembers.


table_of_members, errMsg = pkg.SMembers(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.SMembers("roles:501")
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.SMembers("online")
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### SCard

Выполняет операцию SCard.


count, errMsg = pkg.SCard(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | count    | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.SCard("roles:501")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.SCard("online")
    print("n =", n)
    print("err =", err)
    print("online users:", n, err)

### SPop

Выполняет операцию SPop.


member, errMsg = pkg.SPop(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | member   | any | результат команды        |
| 2   | errMsg   | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local m, err = pkg.SPop("pool:workers")
    print("m =", m)
    print("err =", err)

**Пример 2**


    local m, err = pkg.SPop("random:tokens")
    print("m =", m)
    print("err =", err)
    print(m or "empty", err)

### SUnion

Выполняет операцию SUnion.


table_of_members, errMsg = pkg.SUnion(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.SUnion("roles:501", "roles:502")
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.SUnion("set:a", "set:b", "set:c")
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### SInter

Выполняет операцию SInter.


table_of_members, errMsg = pkg.SInter(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.SInter("roles:501", "roles:502")
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.SInter("set:a", "set:b")
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### SDiff

Выполняет операцию SDiff.


table_of_members, errMsg = pkg.SDiff(key1, ...keys)

#### Входные параметры

| Параметр | Тип       | Описание             |
|----------|-----------|----------------------|
| key1     | string    | первый ключ          |
| ...keys  | string... | дополнительные ключи |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.SDiff("roles:501", "roles:502")
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.SDiff("set:a", "set:b", "set:c")
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### ZAdd

Выполняет операцию ZAdd.


addedCount, errMsg = pkg.ZAdd(key, score, member, ...pairs)

#### Входные параметры

| Параметр | Тип             | Описание                            |
|----------|-----------------|-------------------------------------|
| key      | string          | ключ sorted set                     |
| score    | number\|string  | score, в коде разбирается из строки |
| member   | string          | элемент                             |
| ...pairs | score,member... | дополнительные пары score/member    |

#### Результирующие параметры

| №   | Значение   | Тип     | Описание                 |
|-----|------------|---------|--------------------------|
| 1   | addedCount | integer | результат команды        |
| 2   | errMsg     | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.ZAdd("leaderboard", 100, "user1", 95, "user2")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.ZAdd("schedule", 1720000000, "job:501")
    print("n =", n)
    print("err =", err)

### ZScore

Выполняет операцию ZScore.


score, errMsg = pkg.ZScore(key, member)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| member   | string | элемент  |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                 |
|-----|----------|--------|--------------------------|
| 1   | score    | string | результат команды        |
| 2   | errMsg   | any    | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local score, err = pkg.ZScore("leaderboard", "user1")
    print("score =", score)
    print("err =", err)

**Пример 2**


    local score, err = pkg.ZScore("schedule", "job:501")
    print("score =", score)
    print("err =", err)

### ZRank

Выполняет операцию ZRank.


rank, errMsg = pkg.ZRank(key, member)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| member   | string | элемент  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | rank     | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local rank, err = pkg.ZRank("leaderboard", "user1")
    print("rank =", rank)
    print("err =", err)

**Пример 2**


    local rank, err = pkg.ZRank("schedule", "job:501")
    print("rank =", rank)
    print("err =", err)

### ZRevRank

Выполняет операцию ZRevRank.


rank, errMsg = pkg.ZRevRank(key, member)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |
| member   | string | элемент  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | rank     | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local rank, err = pkg.ZRevRank("leaderboard", "user1")
    print("rank =", rank)
    print("err =", err)

**Пример 2**


    local rank, err = pkg.ZRevRank("leaderboard", "user2")
    print("rank =", rank)
    print("err =", err)

### ZRange

Выполняет операцию ZRange.


table_of_members, errMsg = pkg.ZRange(key, start, stop)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| start    | integer | начальный индекс       |
| stop     | integer | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.ZRange("leaderboard", 0, 9)
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.ZRange("schedule", 0, -1)
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### ZRevRange

Выполняет операцию ZRevRange.


table_of_members, errMsg = pkg.ZRevRange(key, start, stop)

#### Входные параметры

| Параметр | Тип     | Описание               |
|----------|---------|------------------------|
| key      | string  | ключ                   |
| start    | integer | начальный индекс       |
| stop     | integer | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение         | Тип | Описание                 |
|-----|------------------|-----|--------------------------|
| 1   | table_of_members | any | результат команды        |
| 2   | errMsg           | any | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local members, err = pkg.ZRevRange("leaderboard", 0, 9)
    print("members =", members)
    print("err =", err)
    for _,m in ipairs(members or {}) do print(m) end

**Пример 2**


    local members, err = pkg.ZRevRange("leaderboard", 0, 2)
    print("members =", members)
    print("err =", err)
    print(members and #members or 0, err)

### ZRem

Выполняет операцию ZRem.


removedCount, errMsg = pkg.ZRem(key, member1, ...members)

#### Входные параметры

| Параметр   | Тип       | Описание                |
|------------|-----------|-------------------------|
| key        | string    | ключ                    |
| member1    | string    | первый элемент          |
| ...members | string... | дополнительные элементы |

#### Результирующие параметры

| №   | Значение     | Тип     | Описание                 |
|-----|--------------|---------|--------------------------|
| 1   | removedCount | integer | результат команды        |
| 2   | errMsg       | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.ZRem("leaderboard", "user1", "user2")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.ZRem("schedule", "job:501")
    print("n =", n)
    print("err =", err)

### ZCard

Выполняет операцию ZCard.


count, errMsg = pkg.ZCard(key)

#### Входные параметры

| Параметр | Тип    | Описание |
|----------|--------|----------|
| key      | string | ключ     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | count    | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.ZCard("leaderboard")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.ZCard("schedule")
    print("n =", n)
    print("err =", err)
    print("items:", n, err)

### ZIncrBy

Выполняет операцию ZIncrBy.


newScore, errMsg = pkg.ZIncrBy(key, increment, member)

#### Входные параметры

| Параметр  | Тип            | Описание               |
|-----------|----------------|------------------------|
| key       | string         | ключ                   |
| increment | number\|string | аргумент команды Redis |
| member    | string         | элемент                |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                 |
|-----|----------|--------|--------------------------|
| 1   | newScore | string | результат команды        |
| 2   | errMsg   | any    | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local score, err = pkg.ZIncrBy("leaderboard", 10, "user1")
    print("score =", score)
    print("err =", err)

**Пример 2**


    local score, err = pkg.ZIncrBy("leaderboard", -5.5, "user2")
    print("score =", score)
    print("err =", err)

### Publish

Выполняет операцию Publish.


receiversCount, errMsg = pkg.Publish(channel, message)

#### Входные параметры

| Параметр | Тип    | Описание               |
|----------|--------|------------------------|
| channel  | string | аргумент команды Redis |
| message  | string | аргумент команды Redis |

#### Результирующие параметры

| №   | Значение       | Тип     | Описание                 |
|-----|----------------|---------|--------------------------|
| 1   | receiversCount | integer | результат команды        |
| 2   | errMsg         | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Publish("events", '{"type":"ORDER_CREATED"}')
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Publish("notifications:user:501", "refresh")
    print("n =", n)
    print("err =", err)
    print("receivers:", n, err)

### Ping

Выполняет операцию Ping.


pong, errMsg = pkg.Ping()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип    | Описание                 |
|-----|----------|--------|--------------------------|
| 1   | pong     | string | результат команды        |
| 2   | errMsg   | any    | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local pong, err = pkg.Ping()
    print("pong =", pong)
    print("err =", err)

**Пример 2**


    local pong, err = pkg.Ping()
    print("pong =", pong)
    print("err =", err)
    print(err == "" and pong or err)

### FlushDB

Выполняет операцию FlushDB.


code, errMsg = pkg.FlushDB()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип | Описание                 |
|-----|----------|-----|--------------------------|
| 1   | code     | any | 0 = успех                |
| 2   | errMsg   | any | ошибка или пустая строка |

⚠ ОПАСНО: удаляет все ключи текущей Redis DB (DB 0 в конфигурации клиента).

#### Примеры вызова и вывод значений результата

**Пример 1**


    local code, err = pkg.FlushDB()
    print("code =", code)
    print("err =", err)

**Пример 2**


    -- ОПАСНО: удаляет все ключи текущей Redis DB
    local code, err = pkg.FlushDB()
    print("code =", code)
    print("err =", err)

### DBSize

Выполняет операцию DBSize.


keyCount, errMsg = pkg.DBSize()

#### Входные параметры

Нет параметров.

#### Результирующие параметры

| №   | Значение | Тип     | Описание                 |
|-----|----------|---------|--------------------------|
| 1   | keyCount | integer | результат команды        |
| 2   | errMsg   | any     | ошибка или пустая строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.DBSize()
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.DBSize()
    print("n =", n)
    print("err =", err)
    print("keys:", n, err)


## pkg/strings

Unicode- и byte-oriented операции над строками.

36 функций

**Инициализация:** `local pkg = require("pkg/strings")`

### SubString

Возвращает подстроку.


result = pkg.SubString(input, start, length)

#### Входные параметры

| Параметр | Тип     | Описание         |
|----------|---------|------------------|
| input    | string  | входное значение |
| start    | integer | начальный индекс |
| length   | integer | длина            |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.SubString("Привет мир", 0, 6)
    print("result =", result)

**Пример 2**


    local result = pkg.SubString("abcdef", 2, 3)
    print("result =", result)

### Length

Возвращает длину строки.


result = pkg.Length(input)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| input    | string | входное значение |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Length("Привет")
    print("result =", result)

**Пример 2**


    local result = pkg.Length("hello 🌍")
    print("result =", result)

### Contains

Проверяет, содержит ли строка подстроку.


result = pkg.Contains(s, substr)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| substr   | string | подстрока       |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Contains("hello world", "world")
    print("result =", result)

**Пример 2**


    local result = pkg.Contains("DamuBPM", "BPM")
    print("result =", result)

### Index

Ищет индекс подстроки в строке (байтовый индекс, -1 если не найдено).


result = pkg.Index(s, substr)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| substr   | string | подстрока       |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Index("hello world", "world")
    print("result =", result)

**Пример 2**


    local result = pkg.Index("abcabc", "bc")
    print("result =", result)

### ToUpper

Преобразует строку к верхнему регистру.


result = pkg.ToUpper(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ToUpper("Привет")
    print("result =", result)

**Пример 2**


    local result = pkg.ToUpper("damubpm")
    print("result =", result)

### ToLower

Преобразует строку к нижнему регистру.


result = pkg.ToLower(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ToLower("DAMUBPM")
    print("result =", result)

**Пример 2**


    local result = pkg.ToLower("ПрИвЕт")
    print("result =", result)

### Replace

Заменяет первые n вхождений old на new (-1 — заменить все).


result = pkg.Replace(s, old, new, n)

#### Входные параметры

| Параметр | Тип     | Описание           |
|----------|---------|--------------------|
| s        | string  | исходная строка    |
| old      | string  | исходная подстрока |
| new      | string  | новая подстрока    |
| n        | integer | входной параметр   |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Replace("a-b-c", "-", "/", 1)
    print("result =", result)

**Пример 2**


    local result = pkg.Replace("a-b-c", "-", "/", -1)
    print("result =", result)

### HasPrefix

Проверяет, начинается ли строка с префикса.


result = pkg.HasPrefix(s, prefix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| prefix   | string | префикс         |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.HasPrefix("order:501", "order:")
    print("result =", result)

**Пример 2**


    local result = pkg.HasPrefix("https://example.kz", "https://")
    print("result =", result)

### HasSuffix

Проверяет, заканчивается ли строка суффиксом.


result = pkg.HasSuffix(s, suffix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| suffix   | string | суффикс         |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.HasSuffix("report.pdf", ".pdf")
    print("result =", result)

**Пример 2**


    local result = pkg.HasSuffix("archive.tar.gz", ".gz")
    print("result =", result)

### Trim

Удаляет пробелы с начала и конца строки.


result = pkg.Trim(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Trim("  hello  ")
    print("result =", result)

**Пример 2**


    local result = pkg.Trim("\n value \t")
    print("result =", result)

### TrimCustom

Удаляет указанный набор символов с начала и конца строки.


result = pkg.TrimCustom(s, cutset)

#### Входные параметры

| Параметр | Тип    | Описание                 |
|----------|--------|--------------------------|
| s        | string | исходная строка          |
| cutset   | string | набор удаляемых символов |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.TrimCustom("---hello---", "-")
    print("result =", result)

**Пример 2**


    local result = pkg.TrimCustom("***value***", "*")
    print("result =", result)

### TrimLeft

Удаляет указанный набор символов с начала строки.


result = pkg.TrimLeft(s, cutset)

#### Входные параметры

| Параметр | Тип    | Описание                 |
|----------|--------|--------------------------|
| s        | string | исходная строка          |
| cutset   | string | набор удаляемых символов |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.TrimLeft("///path", "/")
    print("result =", result)

**Пример 2**


    local result = pkg.TrimLeft("000123", "0")
    print("result =", result)

### TrimRight

Удаляет указанный набор символов с конца строки.


result = pkg.TrimRight(s, cutset)

#### Входные параметры

| Параметр | Тип    | Описание                 |
|----------|--------|--------------------------|
| s        | string | исходная строка          |
| cutset   | string | набор удаляемых символов |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.TrimRight("name...", ".")
    print("result =", result)

**Пример 2**


    local result = pkg.TrimRight("100000", "0")
    print("result =", result)

### Split

Разделяет строку на подстроки по указанному разделителю.


parts = pkg.Split(s, sep)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| sep      | string | разделитель     |

#### Результирующие параметры

| №   | Значение | Тип             | Описание     |
|-----|----------|-----------------|--------------|
| 1   | parts    | table\<string\> | массив строк |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local parts = pkg.Split("a,b,c", ",")
    print("parts =", parts)
    for i,v in ipairs(parts) do print(i,v) end

**Пример 2**


    local parts = pkg.Split("2026-08-27", "-")
    print("parts =", parts)
    print("count:", #parts)
    for i,v in ipairs(parts) do print(i,v) end

### Join

Присоединяет подстроки с разделителем.


result = pkg.Join(parts, sep)

#### Входные параметры

| Параметр | Тип             | Описание     |
|----------|-----------------|--------------|
| parts    | table\<string\> | массив строк |
| sep      | string          | разделитель  |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.Join({"a","b","c"}, ",")
    print("s =", s)

**Пример 2**


    local s = pkg.Join({"var","log","app"}, "/")
    print("s =", s)

### Repeat

Повторяет строку указанное количество раз.


result = pkg.Repeat(s, count)

#### Входные параметры

| Параметр | Тип     | Описание        |
|----------|---------|-----------------|
| s        | string  | исходная строка |
| count    | integer | количество      |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Repeat("ab", 3)
    print("result =", result)

**Пример 2**


    local result = pkg.Repeat("-", 10)
    print("result =", result)

### Title

Заглавная буква строки.


result = pkg.Title(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Title("hello world")
    print("result =", result)

**Пример 2**


    local result = pkg.Title("damubpm api")
    print("result =", result)

### ContainsAny

Проверяет, содержит ли строка хотя бы один символ из набора.


result = pkg.ContainsAny(s, chars)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| chars    | string | набор символов  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ContainsAny("abc123", "09")
    print("result =", result)

**Пример 2**


    local result = pkg.ContainsAny("hello", "xyzol")
    print("result =", result)

### ContainsRune

Проверяет, содержит ли строка указанный рун (Unicode code point) Принимает строку из одного символа.


result = pkg.ContainsRune(s, runeStr)

#### Входные параметры

| Параметр | Тип    | Описание            |
|----------|--------|---------------------|
| s        | string | исходная строка     |
| runeStr  | string | один Unicode-символ |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ContainsRune("Привет", "в")
    print("result =", result)

**Пример 2**


    local result = pkg.ContainsRune("hello 🌍", "🌍")
    print("result =", result)

### LastIndex

Ищет последний индекс подстроки в строке.


result = pkg.LastIndex(s, substr)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| substr   | string | подстрока       |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.LastIndex("abcabc", "bc")
    print("result =", result)

**Пример 2**


    local result = pkg.LastIndex("a/b/c", "/")
    print("result =", result)

### IndexAny

Ищет индекс первого символа из набора в строке.


result = pkg.IndexAny(s, chars)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| chars    | string | набор символов  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.IndexAny("hello123", "0123456789")
    print("result =", result)

**Пример 2**


    local result = pkg.IndexAny("abcXYZ", "ZY")
    print("result =", result)

### LastIndexAny

Ищет последний индекс первого символа из набора в строке.


result = pkg.LastIndexAny(s, chars)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| chars    | string | набор символов  |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.LastIndexAny("a1b2c3", "123")
    print("result =", result)

**Пример 2**


    local result = pkg.LastIndexAny("file.name.ext", ".")
    print("result =", result)

### IndexRune

Ищет индекс первого вхождения руна (принимает строку из одного символа).


result = pkg.IndexRune(s, runeStr)

#### Входные параметры

| Параметр | Тип    | Описание            |
|----------|--------|---------------------|
| s        | string | исходная строка     |
| runeStr  | string | один Unicode-символ |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.IndexRune("hello 🌍", "🌍")
    print("result =", result)

**Пример 2**


    local result = pkg.IndexRune("Привет", "и")
    print("result =", result)

### Count

Подсчитывает количество непересекающихся вхождений подстроки.


result = pkg.Count(s, substr)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| substr   | string | подстрока       |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | integer | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Count("one two one", "one")
    print("result =", result)

**Пример 2**


    local result = pkg.Count("aaaa", "aa")
    print("result =", result)

### EqualFold

Сравнивает строки без учёта регистра.


result = pkg.EqualFold(s, t)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| t        | string | вторая строка   |

#### Результирующие параметры

| №   | Значение | Тип     | Описание  |
|-----|----------|---------|-----------|
| 1   | result   | boolean | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.EqualFold("DamuBPM", "damubpm")
    print("result =", result)

**Пример 2**


    local result = pkg.EqualFold("TEST", "test")
    print("result =", result)

### ReplaceAll

Заменяет все вхождения old на new.


result = pkg.ReplaceAll(s, old, newStr)

#### Входные параметры

| Параметр | Тип    | Описание           |
|----------|--------|--------------------|
| s        | string | исходная строка    |
| old      | string | исходная подстрока |
| newStr   | string | новая подстрока    |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ReplaceAll("a-b-c", "-", "/")
    print("result =", result)

**Пример 2**


    local result = pkg.ReplaceAll("foo foo", "foo", "bar")
    print("result =", result)

### TrimPrefix

Удаляет указанный префикс из строки (если есть).


result = pkg.TrimPrefix(s, prefix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| prefix   | string | префикс         |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.TrimPrefix("order:501", "order:")
    print("result =", result)

**Пример 2**


    local result = pkg.TrimPrefix("https://example.kz", "https://")
    print("result =", result)

### TrimSuffix

Удаляет указанный суффикс из строки (если есть).


result = pkg.TrimSuffix(s, suffix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| suffix   | string | суффикс         |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.TrimSuffix("report.pdf", ".pdf")
    print("result =", result)

**Пример 2**


    local result = pkg.TrimSuffix("name.tmp", ".tmp")
    print("result =", result)

### SplitN

Разделяет строку на не более чем n подстрок.


parts = pkg.SplitN(s, sep, n)

#### Входные параметры

| Параметр | Тип     | Описание         |
|----------|---------|------------------|
| s        | string  | исходная строка  |
| sep      | string  | разделитель      |
| n        | integer | входной параметр |

#### Результирующие параметры

| №   | Значение | Тип             | Описание     |
|-----|----------|-----------------|--------------|
| 1   | parts    | table\<string\> | массив строк |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local parts = pkg.SplitN("a,b,c,d", ",", 3)
    print("parts =", parts)
    for i,v in ipairs(parts) do print(i,v) end

**Пример 2**


    local parts = pkg.SplitN("key=value=extra", "=", 2)
    print("parts =", parts)
    print("count:", #parts)
    for i,v in ipairs(parts) do print(i,v) end

### SplitAfter

Разделяет строку, оставляя разделитель в конце каждой части.


parts = pkg.SplitAfter(s, sep)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| sep      | string | разделитель     |

#### Результирующие параметры

| №   | Значение | Тип             | Описание     |
|-----|----------|-----------------|--------------|
| 1   | parts    | table\<string\> | массив строк |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local parts = pkg.SplitAfter("a,b,c", ",")
    print("parts =", parts)
    for i,v in ipairs(parts) do print(i,v) end

**Пример 2**


    local parts = pkg.SplitAfter("one.two.three", ".")
    print("parts =", parts)
    print("count:", #parts)
    for i,v in ipairs(parts) do print(i,v) end

### SplitAfterN

Разделяет строку на не более чем n частей, оставляя разделитель.


parts = pkg.SplitAfterN(s, sep, n)

#### Входные параметры

| Параметр | Тип     | Описание         |
|----------|---------|------------------|
| s        | string  | исходная строка  |
| sep      | string  | разделитель      |
| n        | integer | входной параметр |

#### Результирующие параметры

| №   | Значение | Тип             | Описание     |
|-----|----------|-----------------|--------------|
| 1   | parts    | table\<string\> | массив строк |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local parts = pkg.SplitAfterN("a,b,c,d", ",", 2)
    print("parts =", parts)
    for i,v in ipairs(parts) do print(i,v) end

**Пример 2**


    local parts = pkg.SplitAfterN("x/y/z", "/", 2)
    print("parts =", parts)
    print("count:", #parts)
    for i,v in ipairs(parts) do print(i,v) end

### Fields

Разбивает строку по пробельным символам (аналог strings.Fields).


parts = pkg.Fields(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип             | Описание     |
|-----|----------|-----------------|--------------|
| 1   | parts    | table\<string\> | массив строк |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local parts = pkg.Fields("one  two\tthree")
    print("parts =", parts)
    for i,v in ipairs(parts) do print(i,v) end

**Пример 2**


    local parts = pkg.Fields("  a b c  ")
    print("parts =", parts)
    print("count:", #parts)
    for i,v in ipairs(parts) do print(i,v) end

### ToTitle

Преобразует строку к заглавному регистру согласно Unicode.


result = pkg.ToTitle(s)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |

#### Результирующие параметры

| №   | Значение | Тип    | Описание  |
|-----|----------|--------|-----------|
| 1   | result   | string | результат |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.ToTitle("hello world")
    print("result =", result)

**Пример 2**


    local result = pkg.ToTitle("привет мир")
    print("result =", result)

### Cut

Разрезает строку по первому вхождению sep. Возвращает три значения: before, after, found (bool).


before, after, found = pkg.Cut(s, sep)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| sep      | string | разделитель     |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                |
|-----|----------|---------|-------------------------|
| 1   | before   | string  | часть до разделителя    |
| 2   | after    | string  | часть после разделителя |
| 3   | found    | boolean | найден ли разделитель   |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local before, after, found = pkg.Cut("key=value", "=")
    print("before =", before)
    print("after =", after)
    print("found =", found)

**Пример 2**


    local before, after, found = pkg.Cut("abc", "/")
    print("before =", before)
    print("after =", after)
    print("found =", found)

### CutPrefix

Отрезает префикс от строки, возвращает оставшуюся часть и bool (Go 1.20+).


after, found = pkg.CutPrefix(s, prefix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| prefix   | string | префикс         |

#### Результирующие параметры

| №   | Значение | Тип     | Описание            |
|-----|----------|---------|---------------------|
| 1   | after    | string  | строка без префикса |
| 2   | found    | boolean | префикс найден      |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local after, found = pkg.CutPrefix("order:501", "order:")
    print("after =", after)
    print("found =", found)

**Пример 2**


    local after, found = pkg.CutPrefix("abc", "x")
    print("after =", after)
    print("found =", found)

### CutSuffix

Отрезает суффикс от строки, возвращает оставшуюся часть и bool (Go 1.20+).


before, found = pkg.CutSuffix(s, suffix)

#### Входные параметры

| Параметр | Тип    | Описание        |
|----------|--------|-----------------|
| s        | string | исходная строка |
| suffix   | string | суффикс         |

#### Результирующие параметры

| №   | Значение | Тип     | Описание            |
|-----|----------|---------|---------------------|
| 1   | before   | string  | строка без суффикса |
| 2   | found    | boolean | суффикс найден      |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local before, found = pkg.CutSuffix("report.pdf", ".pdf")
    print("before =", before)
    print("found =", found)

**Пример 2**


    local before, found = pkg.CutSuffix("abc", ".txt")
    print("before =", before)
    print("found =", found)


## pkg/fmt

Форматирование, печать и разбор строк в стиле Go fmt.

13 функций

**Инициализация:** `local pkg = require("pkg/fmt")`

### Print

fmt.Print(...) → (n int, err string).


n, err = pkg.Print(...values)

#### Входные параметры

| Параметр  | Тип    | Описание            |
|-----------|--------|---------------------|
| ...values | any... | значения для печати |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Print("id=", 501, " state=NEW")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Print("hello", " ", "world")
    print("n =", n)
    print("err =", err)

### Println

fmt.Println(...) → (n int, err string).


n, err = pkg.Println(...values)

#### Входные параметры

| Параметр  | Тип    | Описание                               |
|-----------|--------|----------------------------------------|
| ...values | any... | значения для печати с переводом строки |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Println("order", 501, "NEW")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Println("hello world")
    print("n =", n)
    print("err =", err)

### Printf

fmt.Printf(format, ...) → (n int, err string).


n, err = pkg.Printf(format, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание         |
|-----------|--------|------------------|
| format    | string | формат fmt       |
| ...values | any... | значения формата |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Printf("order=%d state=%s\n", 501, "NEW")
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Printf("price=%.2f\n", 123.456)
    print("n =", n)
    print("err =", err)

### Sprint

fmt.Sprint(...) → string.


text = pkg.Sprint(...values)

#### Входные параметры

| Параметр  | Тип    | Описание                  |
|-----------|--------|---------------------------|
| ...values | any... | значения для конкатенации |

#### Результирующие параметры

| №   | Значение | Тип    | Описание              |
|-----|----------|--------|-----------------------|
| 1   | text     | string | сформированная строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.Sprint("order-", 501)
    print("s =", s)

**Пример 2**


    local s = pkg.Sprint("a", 1, true)
    print("s =", s)

### Sprintln

fmt.Sprintln(...) → string.


text = pkg.Sprintln(...values)

#### Входные параметры

| Параметр  | Тип    | Описание                                |
|-----------|--------|-----------------------------------------|
| ...values | any... | значения с пробелами и переводом строки |

#### Результирующие параметры

| №   | Значение | Тип    | Описание              |
|-----|----------|--------|-----------------------|
| 1   | text     | string | сформированная строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.Sprintln("order", 501, "NEW")
    print("s =", s)

**Пример 2**


    local s = pkg.Sprintln("hello", "world")
    print("s =", s)

### Sprintf

fmt.Sprintf(format, ...) → string.


text = pkg.Sprintf(format, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание         |
|-----------|--------|------------------|
| format    | string | формат fmt       |
| ...values | any... | значения формата |

#### Результирующие параметры

| №   | Значение | Тип    | Описание              |
|-----|----------|--------|-----------------------|
| 1   | text     | string | сформированная строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.Sprintf("order=%d state=%s", 501, "NEW")
    print("s =", s)

**Пример 2**


    local s = pkg.Sprintf("%.2f%%", 99.95)
    print("s =", s)

### Fprint

fmt.Fprint(w, ...) → (n int, err string).


n, err = pkg.Fprint(writer, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание              |
|-----------|--------|-----------------------|
| writer    | string | "stdout" или "stderr" |
| ...values | any... | значения              |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Fprint("stdout", "hello", 501)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Fprint("stderr", "error: ", "failed")
    print("n =", n)
    print("err =", err)

### Fprintln

fmt.Fprintln(w, ...) → (n int, err string).


n, err = pkg.Fprintln(writer, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание              |
|-----------|--------|-----------------------|
| writer    | string | "stdout" или "stderr" |
| ...values | any... | значения              |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Fprintln("stdout", "done", 501)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Fprintln("stderr", "warning")
    print("n =", n)
    print("err =", err)

### Fprintf

fmt.Fprintf(w, format, ...) → (n int, err string).


n, err = pkg.Fprintf(writer, format, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание              |
|-----------|--------|-----------------------|
| writer    | string | "stdout" или "stderr" |
| format    | string | формат fmt            |
| ...values | any... | значения              |

#### Результирующие параметры

| №   | Значение | Тип         | Описание              |
|-----|----------|-------------|-----------------------|
| 1   | n        | integer     | число записанных байт |
| 2   | err      | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local n, err = pkg.Fprintf("stdout", "id=%d\n", 501)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local n, err = pkg.Fprintf("stderr", "error=%s\n", "timeout")
    print("n =", n)
    print("err =", err)

### Errorf

fmt.Errorf(format, ...) → string.


text = pkg.Errorf(format, ...values)

#### Входные параметры

| Параметр  | Тип    | Описание   |
|-----------|--------|------------|
| format    | string | формат fmt |
| ...values | any... | значения   |

#### Результирующие параметры

| №   | Значение | Тип    | Описание              |
|-----|----------|--------|-----------------------|
| 1   | text     | string | сформированная строка |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local s = pkg.Errorf("order %d: %s", 501, "not found")
    print("s =", s)

**Пример 2**


    local s = pkg.Errorf("invalid value: %s", "abc")
    print("s =", s)

### Sscan

fmt.Sscan(str, ...) → (n int, err string) Сканирует строку и возвращает количество успешно считанных элементов. Из Lua передаётся строка-источник; результаты возвращаются как множественные значения.


results..., n, err = pkg.Sscan(src, ...placeholders)

#### Входные параметры

| Параметр        | Тип    | Описание                                                                                                       |
|-----------------|--------|----------------------------------------------------------------------------------------------------------------|
| src             | string | строка-источник                                                                                                |
| ...placeholders | any... | количество дополнительных аргументов задаёт число считываемых полей; значения самих аргументов не используются |

#### Результирующие параметры

| №   | Значение   | Тип         | Описание              |
|-----|------------|-------------|-----------------------|
| 1   | results... | string...   | считанные значения    |
| 2   | n          | integer     | число считанных полей |
| 3   | err        | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local a, b, n, err = pkg.Sscan("10 hello", true, true)
    print("a =", a)
    print("b =", b)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local a, b, c, n, err = pkg.Sscan("one two three", 0, 0, 0)
    print("a =", a)
    print("b =", b)
    print("c =", c)
    print("n =", n)
    print("err =", err)

### Sscanf

fmt.Sscanf(str, format) → (results..., n int, err string).


results..., n, err = pkg.Sscanf(src, format)

#### Входные параметры

| Параметр | Тип    | Описание            |
|----------|--------|---------------------|
| src      | string | строка-источник     |
| format   | string | формат сканирования |

#### Результирующие параметры

| №   | Значение   | Тип         | Описание              |
|-----|------------|-------------|-----------------------|
| 1   | results... | string...   | считанные значения    |
| 2   | n          | integer     | число считанных полей |
| 3   | err        | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local id, state, n, err = pkg.Sscanf("501 NEW", "%s %s")
    print("id =", id)
    print("state =", state)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local a, b, n, err = pkg.Sscanf("x=10 y=20", "x=%s y=%s")
    print("a =", a)
    print("b =", b)
    print("n =", n)
    print("err =", err)

### Sscanln

fmt.Sscanln(str) → (results..., n int, err string).


results..., n, err = pkg.Sscanln(src, ...placeholders)

#### Входные параметры

| Параметр        | Тип    | Описание                                                            |
|-----------------|--------|---------------------------------------------------------------------|
| src             | string | строка-источник                                                     |
| ...placeholders | any... | количество дополнительных аргументов задаёт число считываемых полей |

#### Результирующие параметры

| №   | Значение   | Тип         | Описание              |
|-----|------------|-------------|-----------------------|
| 1   | results... | string...   | считанные значения    |
| 2   | n          | integer     | число считанных полей |
| 3   | err        | string\|nil | nil на успехе         |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local a, b, n, err = pkg.Sscanln("10 hello", true, true)
    print("a =", a)
    print("b =", b)
    print("n =", n)
    print("err =", err)

**Пример 2**


    local a, n, err = pkg.Sscanln("single", true)
    print("a =", a)
    print("n =", n)
    print("err =", err)


## pkg/path/filepath

Операции над файловыми путями и рекурсивный обход дерева файлов.

9 функций

**Инициализация:** `local pkg = require("pkg/path/filepath")`

### Abs

Abs конвертирует filepath.Abs для Lua. Принимает путь в качестве входного параметра, конвертирует его в абсолютный путь и возвращает результат. В случае ошибки возвращает nil и сообщение об ошибке.


path, err = pkg.Abs(path)

#### Входные параметры

| Параметр | Тип    | Описание                                       |
|----------|--------|------------------------------------------------|
| path     | string | путь, который нужно преобразовать в абсолютный |

#### Результирующие параметры

| №   | Значение | Тип         | Описание                                                                   |
|-----|----------|-------------|----------------------------------------------------------------------------|
| 1   | path     | string\|nil | абсолютный путь; nil при ошибке                                            |
| 2   | err      | string\|nil | сообщение ошибки; на успехе второй результат отсутствует и в Lua будет nil |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local p, err = pkg.Abs("./data/report.csv")
    print("p =", p)
    print("err =", err)

**Пример 2**


    local p, err = pkg.Abs("../tmp")
    print("p =", p)
    print("err =", err)

### Base

Base конвертирует filepath.Base для Lua. Принимает путь в качестве входного параметра и возвращает последний элемент пути (имя файла или директории). Если путь некорректен, возвращает пустую строку.


result = pkg.Base(path)

#### Входные параметры

| Параметр | Тип    | Описание                  |
|----------|--------|---------------------------|
| path     | string | путь к файлу или каталогу |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                       |
|-----|----------|--------|--------------------------------|
| 1   | result   | string | результирующий путь/часть пути |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Base("/var/log/app.log")
    print("result =", result)

**Пример 2**


    local result = pkg.Base("/var/lib/postgresql")
    print("result =", result)

### Clean

Clean конвертирует filepath.Clean для Lua. Принимает путь в качестве входного параметра, очищает его (убирает лишние элементы, такие как "..", ".", и т.д.), и возвращает очищенный путь.


result = pkg.Clean(path)

#### Входные параметры

| Параметр | Тип    | Описание              |
|----------|--------|-----------------------|
| path     | string | путь для нормализации |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                       |
|-----|----------|--------|--------------------------------|
| 1   | result   | string | результирующий путь/часть пути |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Clean("/var/log/../lib//app")
    print("result =", result)

**Пример 2**


    local result = pkg.Clean("./a/./b/../c")
    print("result =", result)

### Dir

Dir конвертирует filepath.Dir для Lua. Принимает путь в качестве входного параметра и возвращает директорию, содержащую указанный файл или директорию. Если путь некорректен, возвращает пустую строку.


result = pkg.Dir(path)

#### Входные параметры

| Параметр | Тип    | Описание                  |
|----------|--------|---------------------------|
| path     | string | путь к файлу или каталогу |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                       |
|-----|----------|--------|--------------------------------|
| 1   | result   | string | результирующий путь/часть пути |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Dir("/var/log/app.log")
    print("result =", result)

**Пример 2**


    local result = pkg.Dir("reports/2026/a.pdf")
    print("result =", result)

### Ext

Ext конвертирует filepath.Ext для Lua. Принимает путь в качестве входного параметра и возвращает расширение файла (например, ".txt"). Если путь некорректен или у файла нет расширения, возвращает пустую строку.


result = pkg.Ext(path)

#### Входные параметры

| Параметр | Тип    | Описание           |
|----------|--------|--------------------|
| path     | string | путь или имя файла |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                       |
|-----|----------|--------|--------------------------------|
| 1   | result   | string | результирующий путь/часть пути |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.Ext("report.pdf")
    print("result =", result)

**Пример 2**


    local result = pkg.Ext("archive.tar.gz")
    print("result =", result)

### Join

Join конвертирует filepath.Join для Lua. Принимает несколько сегментов пути из Lua и объединяет их в один путь. Результат возвращается в виде одной строки.


result = pkg.Join(...parts)

#### Входные параметры

| Параметр | Тип       | Описание      |
|----------|-----------|---------------|
| ...parts | string... | сегменты пути |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                       |
|-----|----------|--------|--------------------------------|
| 1   | result   | string | результирующий путь/часть пути |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local p = pkg.Join("/var", "log", "app", "events.log")
    print("p =", p)

**Пример 2**


    local p = pkg.Join("data", "2026", "08", "report.csv")
    print("p =", p)

### IsAbs

IsAbs конвертирует filepath.IsAbs для Lua. Проверяет, является ли указанный путь абсолютным. Возвращает true, если путь абсолютный, иначе false.


result = pkg.IsAbs(path)

#### Входные параметры

| Параметр | Тип    | Описание         |
|----------|--------|------------------|
| path     | string | проверяемый путь |

#### Результирующие параметры

| №   | Значение | Тип     | Описание                  |
|-----|----------|---------|---------------------------|
| 1   | result   | boolean | true если путь абсолютный |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local result = pkg.IsAbs("/var/log")
    print("result =", result)

**Пример 2**


    local result = pkg.IsAbs("data/report.csv")
    print("result =", result)

### Walk

Walk конвертирует filepath.Walk для Lua. Рекурсивно проходит по всем файлам и директориям в указанной корневой директории. Для каждого файла или директории вызывает Lua-функцию с аргументами: путь, булево значение (является ли объект директорией), и возможная ошибка.


err = pkg.Walk(root, callback)

#### Входные параметры

| Параметр | Тип      | Описание                                                                 |
|----------|----------|--------------------------------------------------------------------------|
| root     | string   | корневой каталог                                                         |
| callback | function | задуман callback(path, isDir, err); см. примечание по текущей реализации |

#### Результирующие параметры

| №   | Значение | Тип         | Описание      |
|-----|----------|-------------|---------------|
| 1   | err      | string\|nil | nil на успехе |

⚠ Комментарий исходника описывает callback(path, isDir, err), но текущий код не извлекает callback явно и вызывает \`l.Call(2, 0)\` после помещения значений в стек. Проверьте эту функцию в вашей сборке перед использованием.

#### Примеры вызова и вывод значений результата

**Пример 1**


    local err = pkg.Walk("/tmp", function(path, isDir, walkErr)
    print("err =", err)
      print(path, isDir, walkErr)
    end)

**Пример 2**


    local err = pkg.Walk("./data", function(path, isDir, walkErr)
    print("err =", err)
      if not isDir then print("file:", path) end
    end)

### Split

Split конвертирует filepath.Split для Lua. Разбивает путь на директорию и имя файла, возвращая оба в виде отдельных строк. Если путь некорректен, возвращает две пустые строки.


dir, file = pkg.Split(path)

#### Входные параметры

| Параметр | Тип    | Описание                                             |
|----------|--------|------------------------------------------------------|
| path     | string | путь, который нужно разделить на каталог и имя файла |

#### Результирующие параметры

| №   | Значение | Тип    | Описание                              |
|-----|----------|--------|---------------------------------------|
| 1   | dir      | string | директория с завершающим разделителем |
| 2   | file     | string | имя файла                             |

#### Примеры вызова и вывод значений результата

**Пример 1**


    local dir, file = pkg.Split("/var/log/app.log")
    print("dir =", dir)
    print("file =", file)

**Пример 2**


    local dir, file = pkg.Split("reports/2026/a.pdf")
    print("dir =", dir)
    print("file =", file)

Справочник отражает предоставленную реализацию Lua API. Закомментированные/незарегистрированные функции не включены как доступные.
