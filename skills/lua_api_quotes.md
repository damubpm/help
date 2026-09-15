# DamuBPM Lua API

[← Главная](index.html)

Практический справочник Lua-вызовов функций, зарегистрированных Go-окружением. Для каждой функции отдельно указаны входящие параметры и все возвращаемые переменные в фактическом порядке. В каждом примере после вызова явно выводятся значения результирующих переменных через `print(...)`. Для SQL-функций количество значений после SQL соответствует количеству `?`-плейсхолдеров и их порядку.

**Всего функций:** 210

## Оглавление

### Прочее

- [EncodeQRCode](#EncodeQRCode)
- [QRCodeBase64](#QRCodeBase64)
- [AddLinks](#AddLinks)
- [BeginTransaction](#BeginTransaction)
- [ClearCache](#ClearCache)
- [Commit](#Commit)
- [CommitTransaction](#CommitTransaction)
- [ExtractFromMultipart](#ExtractFromMultipart)
- [GetHTTPListenHostPort](#GetHTTPListenHostPort)
- [HTMLToFODTStyle](#HTMLToFODTStyle)
- [HTMLToFODTContent](#HTMLToFODTContent)
- [Join](#Join)
- [Md5](#Md5)
- [ParseHTMLTemplate](#ParseHTMLTemplate)
- [ParseTemplate](#ParseTemplate)
- [ParseSecond](#ParseSecond)
- [RateLimiter](#RateLimiter)
- [RollBackTransaction](#RollBackTransaction)
- [Rollback](#Rollback)
- [Sha256](#Sha256)
- [Split](#Split)
- [WriteLog](#WriteLog)
- [beBe](#beBe)

### DamuBPM API

- [AccClsPublish](#AccClsPublish)
- [AccPostByPkNoOper](#AccPostByPkNoOper)
- [AccPostByPkOper](#AccPostByPkOper)
- [AccUndoByPkNoOper](#AccUndoByPkNoOper)
- [BPMNPublish](#BPMNPublish)
- [CachedGetParamValue](#CachedGetParamValue)
- [CheckFullGrantOfEntity](#CheckFullGrantOfEntity)
- [CheckGrantOfEntity](#CheckGrantOfEntity)
- [CheckLicense](#CheckLicense)
- [Detail](#Detail)
- [ExtendSession](#ExtendSession)
- [EntityValueByCode](#EntityValueByCode)
- [EntityValueById](#EntityValueById)
- [EntityTitleById](#EntityTitleById)
- [EntityValueByUUID](#EntityValueByUUID)
- [EntityValueByUqAttr](#EntityValueByUqAttr)
- [GetDomainParamValue](#GetDomainParamValue)
- [GetParamValue](#GetParamValue)
- [GetUserParamValue](#GetUserParamValue)
- [DeleteExpiredSessions](#DeleteExpiredSessions)

### Файлы и S3

- [AppendFile](#AppendFile)
- [Chdir](#Chdir)
- [CopyFile](#CopyFile)
- [FileContent](#FileContent)
- [FileExists](#FileExists)
- [FileDate](#FileDate)
- [FilepathGlob](#FilepathGlob)
- [Getwd](#Getwd)
- [IoutilReadDir](#IoutilReadDir)
- [MkdirAll](#MkdirAll)
- [PDFBatch](#PDFBatch)
- [PDFInfo](#PDFInfo)
- [PNG2JPEG](#PNG2JPEG)
- [PathEscape](#PathEscape)
- [ReadFile](#ReadFile)
- [ReadFilePart](#ReadFilePart)
- [S3GetObject](#S3GetObject)
- [S3ListObjects](#S3ListObjects)
- [S3UploadObject](#S3UploadObject)
- [TempDir](#TempDir)
- [TempFile](#TempFile)
- [VertialTextToPNG](#VertialTextToPNG)
- [UpdateRawData](#UpdateRawData)
- [UploadRawData](#UploadRawData)
- [WriteFile](#WriteFile)
- [WriteFile2](#WriteFile2)

### Форматы и кодирование

- [Base64Decode](#Base64Decode)
- [Base64Encode](#Base64Encode)
- [CSVRead](#CSVRead)
- [FromCP1048](#FromCP1048)
- [HexToString](#HexToString)
- [JWTTokenToJson](#JWTTokenToJson)
- [JWTTokenWithoutVerificationToJson](#JWTTokenWithoutVerificationToJson)
- [JsonToJWTToken](#JsonToJWTToken)
- [JsonToString](#JsonToString)
- [JsonToStringIndent](#JsonToStringIndent)
- [JsonToXML](#JsonToXML)
- [StringToJson](#StringToJson)
- [ToCP1048](#ToCP1048)
- [XmlPathParse](#XmlPathParse)
- [XmltoJSONString](#XmltoJSONString)
- [GunZipString](#GunZipString)
- [GZipString](#GZipString)
- [ZipString](#ZipString)

### SQL и данные

- [CachedSqlQueryRow](#CachedSqlQueryRow)
- [CachedSqlQueryRow2](#CachedSqlQueryRow2)
- [CachedSqlQueryRows](#CachedSqlQueryRows)
- [CheckQuery](#CheckQuery)
- [ColumnsByQuery](#ColumnsByQuery)
- [Query](#Query)
- [QueryEscape](#QueryEscape)
- [QueryUnescape](#QueryUnescape)
- [QueryWithCount](#QueryWithCount)
- [QueryCount](#QueryCount)
- [RedisSqlQueryRow2](#RedisSqlQueryRow2)
- [RedisSqlQueryRows](#RedisSqlQueryRows)
- [SqlCall](#SqlCall)
- [SqlCallExtDb](#SqlCallExtDb)
- [SqlExec](#SqlExec)
- [SqlExec2](#SqlExec2)
- [SqlExec3](#SqlExec3)
- [SqlInsert](#SqlInsert)
- [SqlQueryRow](#SqlQueryRow)
- [SqlQueryRow2](#SqlQueryRow2)
- [SqlQueryRows](#SqlQueryRows)
- [SqlQueryRowsExtDb](#SqlQueryRowsExtDb)
- [SqlQueryRowsExtDbCursor](#SqlQueryRowsExtDbCursor)

### Безопасность и LDAP

- [SSLExpireDays](#SSLExpireDays)
- [CheckSSLExpire](#CheckSSLExpire)
- [CompareHashAndPassword](#CompareHashAndPassword)
- [CryptoGetPfxInfo](#CryptoGetPfxInfo)
- [CryptoSignPKCS1v15](#CryptoSignPKCS1v15)
- [Decrypt](#Decrypt)
- [DecryptAES](#DecryptAES)
- [Encrypt](#Encrypt)
- [GetPasswordHash](#GetPasswordHash)
- [LdapCreateUser](#LdapCreateUser)
- [LdapSearch](#LdapSearch)
- [LdapSearchCaCert](#LdapSearchCaCert)

### Система и выполнение

- [Command](#Command)
- [CommandEnv](#CommandEnv)
- [CommandEnvOutput](#CommandEnvOutput)
- [Cron](#Cron)
- [CronCheckInterval](#CronCheckInterval)
- [CronEntries](#CronEntries)
- [CronRemove](#CronRemove)
- [CronRunEntry](#CronRunEntry)
- [DBCurrentDateTime](#DBCurrentDateTime)
- [DoScript](#DoScript)
- [DoScriptGetBool](#DoScriptGetBool)
- [DoScriptGetTable](#DoScriptGetTable)
- [DoScriptReturnTableRec](#DoScriptReturnTableRec)
- [Hostname](#Hostname)
- [KillProcess](#KillProcess)
- [LoadScript](#LoadScript)
- [LoadString](#LoadString)
- [LoadStringNamed](#LoadStringNamed)
- [OsStat](#OsStat)
- [Plugin](#Plugin)
- [RunParallel](#RunParallel)
- [ShutdownServer](#ShutdownServer)
- [Sleep](#Sleep)
- [UUID](#UUID)
- [UUIDFromString](#UUIDFromString)
- [Version](#Version)
- [GoVersion](#GoVersion)
- [VersionNum](#VersionNum)

### Строки и утилиты

- [EncodeToScientific](#EncodeToScientific)
- [EmailMask](#EmailMask)
- [EncodeToISO9A](#EncodeToISO9A)
- [EncodeToISO9B](#EncodeToISO9B)
- [EncodeToBGN](#EncodeToBGN)
- [EncodeToPCGN](#EncodeToPCGN)
- [EncodeToALALC](#EncodeToALALC)
- [EncodeToBS](#EncodeToBS)
- [EncodeToICAO](#EncodeToICAO)
- [HTMLEscapeString](#HTMLEscapeString)
- [HasPrefix](#HasPrefix)
- [HasSuffix](#HasSuffix)
- [RegexpCheck](#RegexpCheck)
- [RegexpFindAllStringsAndJoin](#RegexpFindAllStringsAndJoin)
- [RegexpFindStringSubmatch](#RegexpFindStringSubmatch)
- [ReplaceWholeWord](#ReplaceWholeWord)
- [RuNum2Word](#RuNum2Word)
- [KkNum2Word](#KkNum2Word)
- [StrContains](#StrContains)
- [StrReplace](#StrReplace)
- [StrToLower](#StrToLower)
- [StrToUpper](#StrToUpper)
- [StrTrimSpace](#StrTrimSpace)
- [StripTags](#StripTags)
- [TimeParseFormat](#TimeParseFormat)
- [TimeParseUnix](#TimeParseUnix)
- [ToLower](#ToLower)

### HTTP / WebSocket

- [HttpGet2](#HttpGet2)
- [HttpGet2WithProxy](#HttpGet2WithProxy)
- [HttpGetKerberos](#HttpGetKerberos)
- [HttpsGet](#HttpsGet)
- [SendWSAsync](#SendWSAsync)
- [httpGet](#httpGet)
- [httpPost](#httpPost)
- [httpPost2](#httpPost2)
- [httpPost2WithProxy](#httpPost2WithProxy)

### Почта и сообщения

- [ImapNotify](#ImapNotify)
- [ImapRemoveInBoxMessage](#ImapRemoveInBoxMessage)
- [ImapProcessInBoxToMessage](#ImapProcessInBoxToMessage)
- [ParseEmailAddress](#ParseEmailAddress)
- [SendEmail](#SendEmail)
- [SendMail2](#SendMail2)
- [SendMail3](#SendMail3)
- [SendMail2NoTLS](#SendMail2NoTLS)
- [SendMail2_ICALTEST](#SendMail2_ICALTEST)
- [TelegramNewDocumentShare](#TelegramNewDocumentShare)
- [TelegramNewMessage](#TelegramNewMessage)

### Очереди и Kafka

- [KafFkaReaderList](#KafFkaReaderList)
- [KafkaAvroConsumer](#KafkaAvroConsumer)
- [KafkaAvroProducer](#KafkaAvroProducer)
- [KafkaReaderClose](#KafkaReaderClose)
- [KafkaReaderCreate](#KafkaReaderCreate)
- [KafkaReaderCreate2](#KafkaReaderCreate2)
- [KafkaWriteMessage](#KafkaWriteMessage)
- [KafkaWriteMessage2](#KafkaWriteMessage2)
- [KafkaWriteMessage3](#KafkaWriteMessage3)
- [KafkaEnqueue](#KafkaEnqueue)
- [KafkaInitProducer](#KafkaInitProducer)
- [MqReceive](#MqReceive)
- [MqSend](#MqSend)

---

<a id="EncodeQRCode"></a>
## EncodeQRCode

**Категория:** Прочее

Создаёт PNG QR-кода и загружает его в файловое хранилище, возвращая идентификатор загруженного файла.

### Сигнатура

```lua
result, err, code = EncodeQRCode(str, level, size, dir, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | level | integer | Уровень коррекции QR: 0 Low, 1 Medium, 2 High, 3 Highest |
| 3 | size | integer | Размер QR PNG в пикселях |
| 4 | dir | string | Каталог файлового хранилища |
| 5 | userId | integer | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | UUID/идентификатор загруженного QR-файла. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = EncodeQRCode("demo", 1, 256, "documents/qr", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = EncodeQRCode("example", 1, 256, "documents/qr", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="QRCodeBase64"></a>
## QRCodeBase64

**Категория:** Прочее

Генерирует PNG QR-кода и возвращает его содержимое в Base64.

### Сигнатура

```lua
base64Png, err, code = QRCodeBase64(str, level, size)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | level | integer | Уровень коррекции QR: 0 Low, 1 Medium, 2 High, 3 Highest |
| 3 | size | integer | Размер QR PNG в пикселях |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | base64Png | string | Base64 PNG QR-кода. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local base64Png, err, code = QRCodeBase64("demo", 1, 256)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", base64Png)
end

-- Значения всех результирующих переменных
print("base64Png:", base64Png)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local base64Png, err, code = QRCodeBase64("example", 1, 256)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", base64Png)
end

-- Значения всех результирующих переменных
print("base64Png:", base64Png)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AccClsPublish"></a>
## AccClsPublish

**Категория:** DamuBPM API

Публикует бухгалтерский класс по его идентификатору.

### Сигнатура

```lua
err, code = AccClsPublish(accClsId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | accClsId | integer | Идентификатор бухгалтерского класса. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = AccClsPublish(1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = AccClsPublish(2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AccPostByPkNoOper"></a>
## AccPostByPkNoOper

**Категория:** DamuBPM API

Создаёт бухгалтерскую проводку по записи и коду операции с явно заданной датой.

### Сигнатура

```lua
result, err, code = AccPostByPkNoOper(pk, operCode, date)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | pk | integer | Первичный ключ записи. |
| 2 | operCode | string | Код бухгалтерской операции. |
| 3 | date | string | Дата операции. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | ID созданного движения/проводки. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = AccPostByPkNoOper(1, "demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = AccPostByPkNoOper(2, "example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AccPostByPkOper"></a>
## AccPostByPkOper

**Категория:** DamuBPM API

Создаёт бухгалтерскую проводку по записи и коду операции.

### Сигнатура

```lua
result, err, code = AccPostByPkOper(pk, operCode)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | pk | integer | Первичный ключ записи. |
| 2 | operCode | string | Код бухгалтерской операции. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | ID созданного движения/проводки. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = AccPostByPkOper(1, "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = AccPostByPkOper(2, "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AccUndoByPkNoOper"></a>
## AccUndoByPkNoOper

**Категория:** DamuBPM API

Отменяет бухгалтерскую проводку для сущности и записи.

### Сигнатура

```lua
err, code = AccUndoByPkNoOper(entityId, pk)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityId | integer | Идентификатор записи сущности. |
| 2 | pk | integer | Первичный ключ записи. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = AccUndoByPkNoOper(1, 1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = AccUndoByPkNoOper(2, 2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AddLinks"></a>
## AddLinks

**Категория:** Прочее

Преобразует URL/ссылки, встречающиеся в тексте, в ссылочное представление.

### Сигнатура

```lua
result = AddLinks(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = AddLinks("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = AddLinks("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="AppendFile"></a>
## AppendFile

**Категория:** Файлы и S3

Дописывает строку в конец файла.

### Сигнатура

```lua
err, code = AppendFile(fileName, s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |
| 2 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = AppendFile("/tmp/demo.txt", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = AppendFile("/tmp/demo.txt", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="BPMNPublish"></a>
## BPMNPublish

**Категория:** DamuBPM API

Публикует BPMN-процесс по идентификатору.

### Сигнатура

```lua
err, code = BPMNPublish(processId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | processId | integer | Идентификатор BPMN-процесса. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = BPMNPublish(1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = BPMNPublish(2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Base64Decode"></a>
## Base64Decode

**Категория:** Форматы и кодирование

Декодирует строку Base64 в исходные байты/строку.

### Сигнатура

```lua
decoded = Base64Decode(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | decoded | string\|nil | Результат функции. |

### Примеры

#### Пример 1

```lua
local decoded = Base64Decode("demo")
print(decoded)

-- Значения всех результирующих переменных
print("decoded:", decoded)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local decoded = Base64Decode("example")
print(decoded)

-- Значения всех результирующих переменных
print("decoded:", decoded)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Base64Encode"></a>
## Base64Encode

**Категория:** Форматы и кодирование

Кодирует строку или бинарные данные в Base64.

### Сигнатура

```lua
base64 = Base64Encode(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | base64 | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local base64 = Base64Encode("demo")
print(base64)

-- Значения всех результирующих переменных
print("base64:", base64)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local base64 = Base64Encode("example")
print(base64)

-- Значения всех результирующих переменных
print("base64:", base64)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="BeginTransaction"></a>
## BeginTransaction

**Категория:** Прочее

Начинает транзакцию текущего соединения БД.

### Сигнатура

```lua
err, code = BeginTransaction()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = BeginTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = BeginTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CSVRead"></a>
## CSVRead

**Категория:** Форматы и кодирование

Разбирает CSV-текст с указанным разделителем и возвращает строки как Lua-таблицу.

### Сигнатура

```lua
result, err, code = CSVRead(str, comma)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | comma | string | Односимвольный разделитель CSV. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | table | Массив CSV-строк. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = CSVRead("demo", ",")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = CSVRead("example", ",")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CachedGetParamValue"></a>
## CachedGetParamValue

**Категория:** DamuBPM API

Возвращает системный параметр через кешированный механизм чтения.

### Сигнатура

```lua
result = CachedGetParamValue(code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | code | string | Код/ключ |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = CachedGetParamValue("APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = CachedGetParamValue("APP_TITLE")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CachedSqlQueryRow"></a>
## CachedSqlQueryRow

**Категория:** SQL и данные

Выполняет кешированный SQL-запрос одной строки и помещает колонки результата в глобальные Lua-переменные.

### Сигнатура

```lua
err, code = CachedSqlQueryRow(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пусто при успехе; колонки результата устанавливаются как глобальные Lua-переменные. |
| 2 | code | integer | 0 — успех; 2 — нет данных; 3 — больше одной строки; другие — ошибка. |

### Примеры

#### Пример 1

```lua
local err, code = CachedSqlQueryRow(
  "select name, code from dict where id = ?",
  10
)
if code == 0 then print(name, code) else print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CachedSqlQueryRow(
  "select title from roles where code = ? and active = ?",
  "ADMIN", 1
)
if code == 0 then print(title) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CachedSqlQueryRow2"></a>
## CachedSqlQueryRow2

**Категория:** SQL и данные

Выполняет кешированный SQL-запрос одной строки и возвращает строку как Lua-таблицу.

### Сигнатура

```lua
row, err, code = CachedSqlQueryRow2(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | row | table\|nil | Одна строка результата. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local row, err, code = CachedSqlQueryRow2(
  "select id, name from dict where code = ?",
  "KZ"
)
if code == 0 then print(row.name) else print(err) end

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local row, err, code = CachedSqlQueryRow2(
  "select code, title from roles where id = ? and active = ?",
  5, 1
)
print(code, row and row.title)

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CachedSqlQueryRows"></a>
## CachedSqlQueryRows

**Категория:** SQL и данные

Выполняет кешированный SQL SELECT и возвращает массив строк.

### Сигнатура

```lua
rows, err, code = CachedSqlQueryRows(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | Массив строк. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = CachedSqlQueryRows(
  "select id, name from dict where type = ? and active = ?",
  "CITY", 1
)
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = CachedSqlQueryRows(
  "select id from roles where code in (?, ?)",
  "ADMIN", "USER"
)
print(code, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Chdir"></a>
## Chdir

**Категория:** Файлы и S3

Меняет текущий рабочий каталог процесса.

### Сигнатура

```lua
err, code = Chdir(location)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | location | string | Новый рабочий каталог. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = Chdir("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = Chdir("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CheckFullGrantOfEntity"></a>
## CheckFullGrantOfEntity

**Категория:** DamuBPM API

Проверяет полный набор прав пользователя на конкретную запись сущности.

### Сигнатура

```lua
err, code = CheckFullGrantOfEntity(user_id, TableName, grant, id)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user_id | integer | Идентификатор пользователя |
| 2 | TableName | string | Код/имя сущности (таблицы). |
| 3 | grant | string | Код проверяемого права. |
| 4 | id | integer | Идентификатор записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CheckFullGrantOfEntity(101, "demo", "demo", 1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CheckFullGrantOfEntity(101, "example", "example", 2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CheckGrantOfEntity"></a>
## CheckGrantOfEntity

**Категория:** DamuBPM API

Проверяет указанное право пользователя на конкретную запись сущности.

### Сигнатура

```lua
err, code = CheckGrantOfEntity(user_id, TableName, grant, id)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user_id | integer | Идентификатор пользователя |
| 2 | TableName | string | Код/имя сущности (таблицы). |
| 3 | grant | string | Код проверяемого права. |
| 4 | id | integer | Идентификатор записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CheckGrantOfEntity(101, "demo", "demo", 1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CheckGrantOfEntity(101, "example", "example", 2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CheckLicense"></a>
## CheckLicense

**Категория:** DamuBPM API

Расшифровывает и проверяет ключ лицензии, возвращая сведения о лицензии.

### Сигнатура

```lua
result, err, code = CheckLicense(licenseKey)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | licenseKey | string | Ключ лицензии |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | table\|nil | Сведения о лицензии. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = CheckLicense("prefix:encrypted-license")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = CheckLicense("prefix:encrypted-license")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CheckQuery"></a>
## CheckQuery

**Категория:** SQL и данные

Проверяет, может ли SQL-запрос быть подготовлен, не выполняя его полезное действие.

### Сигнатура

```lua
err, code = CheckQuery(sql)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sql | string | SQL-текст запроса |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CheckQuery("select id, name from users")
if code == 0 then print("query is valid") else print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CheckQuery("select count(*) from orders where state = 'NEW'")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SSLExpireDays"></a>
## SSLExpireDays

**Категория:** Безопасность и LDAP

Подключается к TLS-сервису и возвращает число дней до окончания сертификата.

### Сигнатура

```lua
days, err, code = SSLExpireDays(hostport)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | hostport | string | TLS endpoint в формате host:port. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | days | integer | Число дней до NotAfter сертификата. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local days, err, code = SSLExpireDays("example.com:443")
if code == 0 then print("days left:", days) else print(err) end

-- Значения всех результирующих переменных
print("days:", days)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local days, err, code = SSLExpireDays("api.example.com:443")
if code == 0 and days < 30 then print("certificate expires soon:", days) end

-- Значения всех результирующих переменных
print("days:", days)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CheckSSLExpire"></a>
## CheckSSLExpire

**Категория:** Безопасность и LDAP

Проверяет TLS-сертификат удалённого host:port на истечение срока.

### Сигнатура

```lua
err, code = CheckSSLExpire(hostport)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | hostport | string | TLS endpoint в формате host:port. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CheckSSLExpire("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CheckSSLExpire("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ClearCache"></a>
## ClearCache

**Категория:** Прочее

Очищает внутренний кеш приложения.

### Сигнатура

```lua
ClearCache()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Явных возвращаемых значений нет. |  |  |  |

### Примеры

#### Пример 1

```lua
ClearCache()
print("done")

-- Функция не возвращает значений.
```

#### Пример 2

```lua
ClearCache()
print("done")
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Функция не возвращает значений.
```

[↑ К оглавлению](#оглавление)

---

<a id="ColumnsByQuery"></a>
## ColumnsByQuery

**Категория:** SQL и данные

Возвращает список имён колонок, которые формирует SQL-запрос.

### Сигнатура

```lua
columns, err, code = ColumnsByQuery(sql)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sql | string | SQL-текст запроса |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | columns | table\|nil | Массив имён колонок. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local columns, err, code = ColumnsByQuery("select id, name, email from users")
if code == 0 then for _, name in ipairs(columns) do print(name) end else print(err) end

-- Значения всех результирующих переменных
if type(columns) == "table" then
  print("columns:", JsonToString(columns))
else
  print("columns:", columns)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local columns, err, code = ColumnsByQuery("select id, state, total from orders")
print(code, err, JsonToString(columns))

-- Значения всех результирующих переменных
if type(columns) == "table" then
  print("columns:", JsonToString(columns))
else
  print("columns:", columns)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Command"></a>
## Command

**Категория:** Система и выполнение

Запускает внешнюю программу; каждый дополнительный Lua-аргумент становится отдельным аргументом командной строки.

### Сигнатура

```lua
err, code = Command(cmd, ...)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | cmd | string | Имя исполняемой программы |
| 2… | ... | varargs | Аргументы командной строки. Каждый Lua-аргумент становится отдельным argv; Lua-таблица разворачивается в несколько argv. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = Command("printf", "%s %s\n", "hello", "lua")
if code ~= 0 then print(err) else print("command completed") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = Command("ls", "-la", "/tmp")
print("code:", code, "err:", err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 3

```lua
-- Таблица также разворачивается в отдельные аргументы
local err, code = Command("printf", {"%s-%s\n", "A", "B"})
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CommandEnv"></a>
## CommandEnv

**Категория:** Система и выполнение

Запускает внешнюю программу с явно заданным набором переменных окружения.

### Сигнатура

```lua
err, code = CommandEnv(cmd, env, ...)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | cmd | string | Имя исполняемой программы |
| 2 | env | string | Переменные окружения, разделённые переводом строки |
| 3… | ... | varargs | Аргументы командной строки. Каждый Lua-аргумент становится отдельным argv; Lua-таблица разворачивается в несколько argv. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local env = "PATH=/usr/bin:/bin\nLANG=C"
local err, code = CommandEnv("sh", env, "-c", "printf '%s\n' "$LANG"")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local env = "PATH=/usr/bin:/bin\nAPP_MODE=test"
local err, code = CommandEnv("env", env)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CommandEnvOutput"></a>
## CommandEnvOutput

**Категория:** Система и выполнение

Запускает внешнюю программу с окружением и возвращает stdout и stderr.

### Сигнатура

```lua
stdout, stderr, err, code = CommandEnvOutput(cmd, env, ...)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | cmd | string | Имя исполняемой программы |
| 2 | env | string | Переменные окружения, разделённые переводом строки |
| 3… | ... | varargs | Аргументы командной строки. Каждый Lua-аргумент становится отдельным argv; Lua-таблица разворачивается в несколько argv. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | stdout | string | Стандартный вывод процесса. |
| 2 | stderr | string | Стандартный поток ошибок процесса. |
| 3 | err | string | Ошибка запуска/завершения. |
| 4 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local env = "PATH=/usr/bin:/bin\nLANG=C"
local stdout, stderr, err, code = CommandEnvOutput("printf", env, "%s", "hello")
print("stdout:", stdout)
print("stderr:", stderr)
print("code:", code, err)

-- Значения всех результирующих переменных
print("stdout:", stdout)
print("stderr:", stderr)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local env = "PATH=/usr/bin:/bin"
local stdout, stderr, err, code = CommandEnvOutput("sh", env, "-c", "echo ok; echo warn >&2")
print(stdout, stderr, err, code)

-- Значения всех результирующих переменных
print("stdout:", stdout)
print("stderr:", stderr)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Commit"></a>
## Commit

**Категория:** Прочее

Фиксирует текущую транзакцию/изменения.

### Сигнатура

```lua
err, code = Commit()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = Commit()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = Commit()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CommitTransaction"></a>
## CommitTransaction

**Категория:** Прочее

Фиксирует транзакцию, созданную транзакционным API.

### Сигнатура

```lua
err, code = CommitTransaction()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CommitTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CommitTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CompareHashAndPassword"></a>
## CompareHashAndPassword

**Категория:** Безопасность и LDAP

Сравнивает пароль с bcrypt-хешем.

### Сигнатура

```lua
result = CompareHashAndPassword(password, hash)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | password | string | Пароль |
| 2 | hash | string | bcrypt-хеш |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = CompareHashAndPassword("secret", "$2a$10$...")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = CompareHashAndPassword("secret", "$2a$10$...")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CopyFile"></a>
## CopyFile

**Категория:** Файлы и S3

Копирует файл и возвращает количество скопированных байт.

### Сигнатура

```lua
bytesCopied, err, code = CopyFile(src, dst)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | src | string | Исходный путь |
| 2 | dst | string | Целевой путь |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | bytesCopied | integer | Количество скопированных байт. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local bytesCopied, err, code = CopyFile("/tmp/source.txt", "/tmp/copy.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", bytesCopied)
end

-- Значения всех результирующих переменных
print("bytesCopied:", bytesCopied)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local bytesCopied, err, code = CopyFile("/tmp/source.txt", "/tmp/copy.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", bytesCopied)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("bytesCopied:", bytesCopied)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Cron"></a>
## Cron

**Категория:** Система и выполнение

Регистрирует Lua-скрипт как cron-задачу и возвращает entry ID.

### Сигнатура

```lua
result, err, code = Cron(str, script, input, id)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | script | string | Lua-код для выполнения. |
| 3 | input | table | Входная Lua-таблица/данные. |
| 4 | id | string | Идентификатор записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | Entry ID cron-задачи. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = Cron("demo", "result = input.value ~= nil", {value=42, name="demo"}, "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = Cron("example", "result = input.value ~= nil", {value=42, name="demo"}, "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CronCheckInterval"></a>
## CronCheckInterval

**Категория:** Система и выполнение

Проверяет корректность cron-выражения с секундами.

### Сигнатура

```lua
err, code = CronCheckInterval(expr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | expr | string | Регулярное либо cron-выражение (зависит от функции). |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CronCheckInterval("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CronCheckInterval("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CronEntries"></a>
## CronEntries

**Категория:** Система и выполнение

Возвращает список зарегистрированных cron-задач с предыдущим/следующим запуском.

### Сигнатура

```lua
entries, err, code = CronEntries()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entries | table | Список cron entries. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local entries, err, code = CronEntries()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", entries)
end

-- Значения всех результирующих переменных
if type(entries) == "table" then
  print("entries:", JsonToString(entries))
else
  print("entries:", entries)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local entries, err, code = CronEntries()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", entries)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(entries) == "table" then
  print("entries:", JsonToString(entries))
else
  print("entries:", entries)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CronRemove"></a>
## CronRemove

**Категория:** Система и выполнение

Удаляет cron-задачу по entry ID.

### Сигнатура

```lua
err, code = CronRemove(i)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | i | integer | I |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CronRemove(1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CronRemove(2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CronRunEntry"></a>
## CronRunEntry

**Категория:** Система и выполнение

Принудительно запускает зарегистрированную cron-задачу.

### Сигнатура

```lua
err, code = CronRunEntry(i, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | i | integer | I |
| 2 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = CronRunEntry(1, true)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = CronRunEntry(2, false)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CryptoGetPfxInfo"></a>
## CryptoGetPfxInfo

**Категория:** Безопасность и LDAP

Читает PFX/PKCS#12 и возвращает сведения о сертификате.

### Сигнатура

```lua
result, err, code = CryptoGetPfxInfo(pfx, password)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | pfx | string | Содержимое PFX/PKCS#12. |
| 2 | password | string | Пароль |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string\|nil | Информация о PFX. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = CryptoGetPfxInfo("demo", "secret")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = CryptoGetPfxInfo("example", "secret")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="CryptoSignPKCS1v15"></a>
## CryptoSignPKCS1v15

**Категория:** Безопасность и LDAP

Формирует криптографическую подпись PKCS#1 v1.5 и возвращает подпись и сертификат.

### Сигнатура

```lua
signature, certificate, err, code = CryptoSignPKCS1v15(data, password, str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | data | string | Данные для обработки/подписи. |
| 2 | password | string | Пароль |
| 3 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | signature | string | Подпись. |
| 2 | certificate | string | Сертификат. |
| 3 | err | string | Ошибка. |
| 4 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local signature, certificate, err, code = CryptoSignPKCS1v15("demo", "secret", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", signature)
end

-- Значения всех результирующих переменных
print("signature:", signature)
print("certificate:", certificate)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local signature, certificate, err, code = CryptoSignPKCS1v15("example", "secret", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", signature)
end

-- Значения всех результирующих переменных
print("signature:", signature)
print("certificate:", certificate)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DBCurrentDateTime"></a>
## DBCurrentDateTime

**Категория:** Система и выполнение

Возвращает текущие дату и время в формате YYYY-MM-DD HH:MM:SS.

### Сигнатура

```lua
result = DBCurrentDateTime()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = DBCurrentDateTime()
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = DBCurrentDateTime()
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Decrypt"></a>
## Decrypt

**Категория:** Безопасность и LDAP

Расшифровывает строку внутренним алгоритмом приложения.

### Сигнатура

```lua
result, err, code = Decrypt(crypted, keyStr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | crypted | string | Crypted |
| 2 | keyStr | string | KeyStr |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Расшифрованная строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = Decrypt("demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = Decrypt("example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DecryptAES"></a>
## DecryptAES

**Категория:** Безопасность и LDAP

Расшифровывает строку AES-алгоритмом приложения.

### Сигнатура

```lua
result, err, code = DecryptAES(crypted, keyStr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | crypted | string | Crypted |
| 2 | keyStr | string | KeyStr |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Расшифрованная строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = DecryptAES("demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = DecryptAES("example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Detail"></a>
## Detail

**Категория:** DamuBPM API

Загружает детальное представление записи сущности для пользователя.

### Сигнатура

```lua
row, err, code = Detail(id, code, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | id | integer | Идентификатор записи |
| 2 | code | string | Код/ключ |
| 3 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | row | table | Детальные данные записи. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local row, err, code = Detail(1, "APP_TITLE", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", row)
end

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local row, err, code = Detail(2, "APP_TITLE", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", row)
end

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DoScript"></a>
## DoScript

**Категория:** Система и выполнение

Выполняет переданный Lua-код, предварительно помещая таблицу во глобальную переменную input.

### Сигнатура

```lua
err, code = DoScript(script, input)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | script | string | Lua-код для выполнения. |
| 2 | input | table | Входная Lua-таблица/данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = DoScript("result = input.value ~= nil", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = DoScript("result = input.value ~= nil", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DoScriptGetBool"></a>
## DoScriptGetBool

**Категория:** Система и выполнение

Выполняет Lua-код и возвращает значение указанной глобальной boolean-переменной.

### Сигнатура

```lua
value, err, code = DoScriptGetBool(script, input, variable)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | script | string | Lua-код для выполнения. |
| 2 | input | table | Входная Lua-таблица/данные. |
| 3 | variable | string | Имя глобальной переменной результата |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | value | boolean | Полученное boolean-значение. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local value, err, code = DoScriptGetBool("value = input.value ~= nil", {value=42, name="demo"}, "value")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", value)
end

-- Значения всех результирующих переменных
print("value:", value)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local value, err, code = DoScriptGetBool("value = input.value ~= nil", {value=42, name="demo"}, "value")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", value)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("value:", value)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DoScriptGetTable"></a>
## DoScriptGetTable

**Категория:** Система и выполнение

Выполняет Lua-код в отдельном Lua-state и возвращает указанную глобальную таблицу.

### Сигнатура

```lua
resultTable, err, code = DoScriptGetTable(script, input, variable)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | script | string | Lua-код для выполнения. |
| 2 | input | table | Входная Lua-таблица/данные. |
| 3 | variable | string | Имя глобальной переменной результата |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | resultTable | table\|nil | Полученная таблица. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local resultTable, err, code = DoScriptGetTable("resultTable = input.value ~= nil", {value=42, name="demo"}, "resultTable")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", resultTable)
end

-- Значения всех результирующих переменных
if type(resultTable) == "table" then
  print("resultTable:", JsonToString(resultTable))
else
  print("resultTable:", resultTable)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local resultTable, err, code = DoScriptGetTable("resultTable = input.value ~= nil", {value=42, name="demo"}, "resultTable")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", resultTable)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(resultTable) == "table" then
  print("resultTable:", JsonToString(resultTable))
else
  print("resultTable:", resultTable)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DoScriptReturnTableRec"></a>
## DoScriptReturnTableRec

**Категория:** Система и выполнение

Выполняет Lua-код, который должен вернуть таблицу, и рекурсивно переносит её в вызывающий state.

### Сигнатура

```lua
resultTable, err, code = DoScriptReturnTableRec(script, input)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | script | string | Lua-код для выполнения. |
| 2 | input | table | Входная Lua-таблица/данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | resultTable | table\|nil | Таблица, возвращённая скриптом. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local resultTable, err, code = DoScriptReturnTableRec("resultTable = input.value ~= nil", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", resultTable)
end

-- Значения всех результирующих переменных
if type(resultTable) == "table" then
  print("resultTable:", JsonToString(resultTable))
else
  print("resultTable:", resultTable)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local resultTable, err, code = DoScriptReturnTableRec("resultTable = input.value ~= nil", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", resultTable)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(resultTable) == "table" then
  print("resultTable:", JsonToString(resultTable))
else
  print("resultTable:", resultTable)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToScientific"></a>
## EncodeToScientific

**Категория:** Строки и утилиты

Транслитерирует строку по научной системе.

### Сигнатура

```lua
result = EncodeToScientific(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToScientific("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToScientific("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EmailMask"></a>
## EmailMask

**Категория:** Строки и утилиты

Маскирует адрес электронной почты.

### Сигнатура

```lua
result = EmailMask(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EmailMask("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EmailMask("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ExtractFromMultipart"></a>
## ExtractFromMultipart

**Категория:** Прочее

Извлекает данные первой части из multipart-тела по boundary.

### Сигнатура

```lua
result, err, code = ExtractFromMultipart(input, separator)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | input | string | Входная Lua-таблица/данные. |
| 2 | separator | string | Разделитель/boundary |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Байты/содержимое первой multipart-части. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = ExtractFromMultipart({value=42, name="demo"}, ",")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = ExtractFromMultipart({value=42, name="demo"}, ",")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToISO9A"></a>
## EncodeToISO9A

**Категория:** Строки и утилиты

Транслитерирует строку по ISO 9, вариант A.

### Сигнатура

```lua
result = EncodeToISO9A(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToISO9A("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToISO9A("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToISO9B"></a>
## EncodeToISO9B

**Категория:** Строки и утилиты

Транслитерирует строку по ISO 9, вариант B.

### Сигнатура

```lua
result = EncodeToISO9B(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToISO9B("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToISO9B("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToBGN"></a>
## EncodeToBGN

**Категория:** Строки и утилиты

Транслитерирует строку по системе BGN/PCGN.

### Сигнатура

```lua
result = EncodeToBGN(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToBGN("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToBGN("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToPCGN"></a>
## EncodeToPCGN

**Категория:** Строки и утилиты

Транслитерирует строку по системе PCGN.

### Сигнатура

```lua
result = EncodeToPCGN(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToPCGN("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToPCGN("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToALALC"></a>
## EncodeToALALC

**Категория:** Строки и утилиты

Транслитерирует строку по системе ALA-LC.

### Сигнатура

```lua
result = EncodeToALALC(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToALALC("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToALALC("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToBS"></a>
## EncodeToBS

**Категория:** Строки и утилиты

Транслитерирует строку по British Standard.

### Сигнатура

```lua
result = EncodeToBS(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToBS("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToBS("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EncodeToICAO"></a>
## EncodeToICAO

**Категория:** Строки и утилиты

Транслитерирует строку в ICAO-совместимое представление.

### Сигнатура

```lua
result = EncodeToICAO(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EncodeToICAO("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EncodeToICAO("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Encrypt"></a>
## Encrypt

**Категория:** Безопасность и LDAP

Шифрует строку внутренним алгоритмом приложения.

### Сигнатура

```lua
result, err, code = Encrypt(txt, key)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | txt | string | Исходный текст. |
| 2 | key | string | Ключ шифрования либо ключ сообщения. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Зашифрованная строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = Encrypt("demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = Encrypt("example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ExtendSession"></a>
## ExtendSession

**Категория:** DamuBPM API

Проверяет пользовательскую сессию и продлевает её активность.

### Сигнатура

```lua
err, code = ExtendSession(anonymousSessionId, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | anonymousSessionId | string | Идентификатор анонимной сессии. |
| 2 | userId | integer | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = ExtendSession("demo", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = ExtendSession("example", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EntityValueByCode"></a>
## EntityValueByCode

**Категория:** DamuBPM API

Возвращает значение поля сущности у записи с указанным code.

### Сигнатура

```lua
result = EntityValueByCode(entityCode, entityField, code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityCode | string | Код сущности |
| 2 | entityField | string | Код поля сущности |
| 3 | code | any | Код/ключ |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EntityValueByCode("orders", "name", "APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EntityValueByCode("orders", "name", "APP_TITLE")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EntityValueById"></a>
## EntityValueById

**Категория:** DamuBPM API

Возвращает значение поля сущности у записи с указанным id.

### Сигнатура

```lua
result = EntityValueById(entityCode, entityField, id)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityCode | string | Код сущности |
| 2 | entityField | string | Код поля сущности |
| 3 | id | any | Идентификатор записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EntityValueById("orders", "name", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EntityValueById("orders", "name", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EntityTitleById"></a>
## EntityTitleById

**Категория:** DamuBPM API

Возвращает отображаемый заголовок записи сущности по id.

### Сигнатура

```lua
result = EntityTitleById(entityCode, id)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityCode | string | Код сущности |
| 2 | id | any | Идентификатор записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EntityTitleById("orders", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EntityTitleById("orders", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EntityValueByUUID"></a>
## EntityValueByUUID

**Категория:** DamuBPM API

Возвращает значение поля сущности у записи с указанным sys$uuid.

### Сигнатура

```lua
result = EntityValueByUUID(entityCode, entityField, uuid)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityCode | string | Код сущности |
| 2 | entityField | string | Код поля сущности |
| 3 | uuid | string | UUID записи |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EntityValueByUUID("orders", "name", "550e8400-e29b-41d4-a716-446655440000")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EntityValueByUUID("orders", "name", "550e8400-e29b-41d4-a716-446655440000")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="EntityValueByUqAttr"></a>
## EntityValueByUqAttr

**Категория:** DamuBPM API

Возвращает значение поля сущности по произвольному уникальному атрибуту.

### Сигнатура

```lua
result = EntityValueByUqAttr(entityCode, entityField, uniqueField, uniqueValue)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | entityCode | string | Код сущности |
| 2 | entityField | string | Код поля сущности |
| 3 | uniqueField | string | Уникальное поле |
| 4 | uniqueValue | any | Значение уникального поля |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = EntityValueByUqAttr("orders", "name", "name", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = EntityValueByUqAttr("orders", "name", "name", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="FileContent"></a>
## FileContent

**Категория:** Файлы и S3

Читает содержимое файла из файлового/S3-хранилища с учётом пользователя и опциональной миниатюры.

### Сигнатура

```lua
data, filename, contentType, err, code = FileContent(fileId, userId, thumb?)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileId | integer | Идентификатор файла |
| 2 | userId | integer | Идентификатор пользователя |
| 3 | thumb | string | Опциональный суффикс миниатюры вида -thumb-… опционально |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | data | string\|nil | Содержимое файла. |
| 2 | filename | string | Имя файла. |
| 3 | contentType | string | MIME type. |
| 4 | err | string | Ошибка. |
| 5 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local data, filename, contentType, err, code = FileContent(1, 101, "-thumb-small")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", data)
end

-- Значения всех результирующих переменных
print("data:", data)
print("filename:", filename)
print("contentType:", contentType)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local data, filename, contentType, err, code = FileContent(2, 101, "-thumb-small")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", data)
end

-- Значения всех результирующих переменных
print("data:", data)
print("filename:", filename)
print("contentType:", contentType)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="FileExists"></a>
## FileExists

**Категория:** Файлы и S3

Проверяет существование файла или пути.

### Сигнатура

```lua
result = FileExists(fileName)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = FileExists("/tmp/demo.txt")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = FileExists("/tmp/demo.txt")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="FileDate"></a>
## FileDate

**Категория:** Файлы и S3

Возвращает дату изменения файла в указанном Go layout.

### Сигнатура

```lua
date, err, code = FileDate(fileName, layout)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |
| 2 | layout | string | Go time layout, используемый для форматирования даты. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | date | string | Дата изменения файла. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local date, err, code = FileDate("/tmp/demo.txt", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", date)
end

-- Значения всех результирующих переменных
print("date:", date)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local date, err, code = FileDate("/tmp/demo.txt", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", date)
end

-- Значения всех результирующих переменных
print("date:", date)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="FilepathGlob"></a>
## FilepathGlob

**Категория:** Файлы и S3

Возвращает список файлов, совпавших с glob-шаблоном.

### Сигнатура

```lua
files, err, code = FilepathGlob(path)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | path | string | Путь или шаблон пути |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | files | table\|nil | Список совпавших путей. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local files, err, code = FilepathGlob("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", files)
end

-- Значения всех результирующих переменных
if type(files) == "table" then
  print("files:", JsonToString(files))
else
  print("files:", files)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local files, err, code = FilepathGlob("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", files)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(files) == "table" then
  print("files:", JsonToString(files))
else
  print("files:", files)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="FromCP1048"></a>
## FromCP1048

**Категория:** Форматы и кодирование

Декодирует строку из кодировки CP1048.

### Сигнатура

```lua
result, err, code = FromCP1048(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Декодированный текст. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = FromCP1048("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = FromCP1048("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GetDomainParamValue"></a>
## GetDomainParamValue

**Категория:** DamuBPM API

Возвращает параметр домена.

### Сигнатура

```lua
result = GetDomainParamValue(domain, code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | domain | string | Код домена параметров. |
| 2 | code | string | Код/ключ |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = GetDomainParamValue("demo", "APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = GetDomainParamValue("example", "APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GetHTTPListenHostPort"></a>
## GetHTTPListenHostPort

**Категория:** Прочее

Возвращает настроенный адрес/порт HTTP listener приложения.

### Сигнатура

```lua
result = GetHTTPListenHostPort()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = GetHTTPListenHostPort()
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = GetHTTPListenHostPort()
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GetParamValue"></a>
## GetParamValue

**Категория:** DamuBPM API

Возвращает значение системного параметра.

### Сигнатура

```lua
result = GetParamValue(code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | code | string | Код/ключ |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = GetParamValue("APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = GetParamValue("APP_TITLE")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GetPasswordHash"></a>
## GetPasswordHash

**Категория:** Безопасность и LDAP

Создаёт bcrypt-хеш пароля.

### Сигнатура

```lua
hash = GetPasswordHash(password)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | password | string | Пароль |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | hash | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local hash = GetPasswordHash("secret")
print(hash)

-- Значения всех результирующих переменных
print("hash:", hash)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local hash = GetPasswordHash("secret")
print(hash)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("hash:", hash)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GetUserParamValue"></a>
## GetUserParamValue

**Категория:** DamuBPM API

Возвращает пользовательский параметр по user ID и коду.

### Сигнатура

```lua
result = GetUserParamValue(userId, code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | userId | integer | Идентификатор пользователя |
| 2 | code | string | Код/ключ |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = GetUserParamValue(101, "APP_TITLE")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = GetUserParamValue(101, "APP_TITLE")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Getwd"></a>
## Getwd

**Категория:** Файлы и S3

Возвращает текущий рабочий каталог процесса.

### Сигнатура

```lua
dir, err, code = Getwd()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | dir | string | Текущий каталог. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local dir, err, code = Getwd()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", dir)
end

-- Значения всех результирующих переменных
print("dir:", dir)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local dir, err, code = Getwd()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", dir)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("dir:", dir)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HTMLEscapeString"></a>
## HTMLEscapeString

**Категория:** Строки и утилиты

Экранирует специальные HTML-символы.

### Сигнатура

```lua
result = HTMLEscapeString(value)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | value | any | Value |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = HTMLEscapeString("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = HTMLEscapeString("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HTMLToFODTStyle"></a>
## HTMLToFODTStyle

**Категория:** Прочее

Преобразует HTML-фрагмент в FODT-стили.

### Сигнатура

```lua
result, err, code = HTMLToFODTStyle(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | FODT style XML. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HTMLToFODTStyle("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HTMLToFODTStyle("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HTMLToFODTContent"></a>
## HTMLToFODTContent

**Категория:** Прочее

Преобразует HTML-фрагмент в FODT-содержимое.

### Сигнатура

```lua
result, err, code = HTMLToFODTContent(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | FODT content XML. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HTMLToFODTContent("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HTMLToFODTContent("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HasPrefix"></a>
## HasPrefix

**Категория:** Строки и утилиты

Проверяет, начинается ли строка с заданного префикса.

### Сигнатура

```lua
result = HasPrefix(s1, s2)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |
| 2 | s2 | string | Вторая строка / искомое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = HasPrefix("demo", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = HasPrefix("example", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HasSuffix"></a>
## HasSuffix

**Категория:** Строки и утилиты

Проверяет, заканчивается ли строка заданным суффиксом.

### Сигнатура

```lua
result = HasSuffix(s1, s2)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |
| 2 | s2 | string | Вторая строка / искомое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = HasSuffix("demo", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = HasSuffix("example", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HexToString"></a>
## HexToString

**Категория:** Форматы и кодирование

Декодирует hex-строку в обычную строку/байты.

### Сигнатура

```lua
result, err, code = HexToString(hexStr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | hexStr | string | Hex-строка без префикса 0x. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Декодированная строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HexToString("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HexToString("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Hostname"></a>
## Hostname

**Категория:** Система и выполнение

Возвращает hostname текущей машины.

### Сигнатура

```lua
hostname, err, code = Hostname()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | hostname | string | Hostname. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local hostname, err, code = Hostname()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", hostname)
end

-- Значения всех результирующих переменных
print("hostname:", hostname)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local hostname, err, code = Hostname()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", hostname)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("hostname:", hostname)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HttpGet2"></a>
## HttpGet2

**Категория:** HTTP / WebSocket

Выполняет HTTP GET с пользовательскими заголовками и возвращает тело ответа.

### Сигнатура

```lua
result, err, code = HttpGet2(url, headers)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | headers | table | Lua-таблица HTTP-заголовков key=value |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Тело HTTP-ответа. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HttpGet2("https://example.com/api", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HttpGet2("https://example.com/health", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HttpGet2WithProxy"></a>
## HttpGet2WithProxy

**Категория:** HTTP / WebSocket

Выполняет HTTP GET через указанный proxy с пользовательскими заголовками.

### Сигнатура

```lua
result, err, code = HttpGet2WithProxy(url, headers, reserved?, proxyUrl)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | headers | table | Lua-таблица HTTP-заголовков key=value |
| 3 | reserved | any | Не используется текущей реализацией; оставлено для совместимости опционально |
| 4 | proxyUrl | string | URL proxy |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | any | Результат операции. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HttpGet2WithProxy("https://example.com/api", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, nil, "http://127.0.0.1:3128")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HttpGet2WithProxy("https://example.com/health", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, nil, "http://127.0.0.1:3128")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HttpGetKerberos"></a>
## HttpGetKerberos

**Категория:** HTTP / WebSocket

Выполняет HTTP GET с Kerberos/SPNEGO-аутентификацией.

### Сигнатура

```lua
headers, body, err, code = HttpGetKerberos(vUrl, config, login, realm, password, arrInterface)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | vUrl | string | URL HTTP-запроса с Kerberos/SPNEGO. |
| 2 | config | string | Текст конфигурации krb5.conf. |
| 3 | login | string | Логин |
| 4 | realm | string | Kerberos realm |
| 5 | password | string | Пароль |
| 6 | arrInterface | table | Lua-таблица HTTP-заголовков key=value. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | headers | table\|nil | Заголовки HTTP-ответа. |
| 2 | body | string | Тело ответа. |
| 3 | err | string | Ошибка. |
| 4 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local headers, body, err, code = HttpGetKerberos("https://example.com/api", "demo", "demo", "EXAMPLE.COM", "secret", {})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", headers)
end

-- Значения всех результирующих переменных
if type(headers) == "table" then
  print("headers:", JsonToString(headers))
else
  print("headers:", headers)
end
print("body:", body)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local headers, body, err, code = HttpGetKerberos("https://example.com/health", "example", "example", "EXAMPLE.COM", "secret", {})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", headers)
end

-- Значения всех результирующих переменных
if type(headers) == "table" then
  print("headers:", JsonToString(headers))
else
  print("headers:", headers)
end
print("body:", body)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="HttpsGet"></a>
## HttpsGet

**Категория:** HTTP / WebSocket

Выполняет HTTPS GET с заголовками и настраиваемым timeout; проверка TLS-сертификата отключена.

### Сигнатура

```lua
result, err, code = HttpsGet(url, headers?, timeoutMs?)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | headers | table | Lua-таблица HTTP-заголовков key=value опционально |
| 3 | timeoutMs | integer | Timeout в миллисекундах опционально |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Тело HTTPS-ответа. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = HttpsGet("https://example.com/api", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, 1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = HttpsGet("https://example.com/health", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, 2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ImapNotify"></a>
## ImapNotify

**Категория:** Почта и сообщения

Подключается к IMAP по TLS и вызывает Lua callback при изменениях INBOX.

### Сигнатура

```lua
err, code = ImapNotify(server, username, password, callback)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | server | string | IMAP TLS endpoint, например imap.example.com:993. |
| 2 | username | string | Логин |
| 3 | password | string | Пароль |
| 4 | callback | function | Lua callback-функция |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = ImapNotify("demo", "demo", "secret", function(value) print(value) end)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = ImapNotify("example", "example", "secret", function(value) print(value) end)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ImapRemoveInBoxMessage"></a>
## ImapRemoveInBoxMessage

**Категория:** Почта и сообщения

Удаляет/помечает для удаления сообщение INBOX по указанному IMAP sequence set.

### Сигнатура

```lua
err, code = ImapRemoveInBoxMessage(user, password, hostPort, setStr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user | string | Пользователь/LDAP bind DN. |
| 2 | password | string | Пароль |
| 3 | hostPort | string | HostPort |
| 4 | setStr | string | IMAP sequence-set/UID set. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = ImapRemoveInBoxMessage("demo", "secret", "demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = ImapRemoveInBoxMessage("example", "secret", "example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ImapProcessInBoxToMessage"></a>
## ImapProcessInBoxToMessage

**Категория:** Почта и сообщения

Обрабатывает письма INBOX через Lua callback-скрипт и возвращает максимальный UID.

### Сигнатура

```lua
result, err, code = ImapProcessInBoxToMessage(user, password, hostPort, callBack, lastCount, lastUid, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user | string | Пользователь/LDAP bind DN. |
| 2 | password | string | Пароль |
| 3 | hostPort | string | HostPort |
| 4 | callBack | string | Имя callback-функции/скрипта. |
| 5 | lastCount | number | Количество последних писем для обработки. |
| 6 | lastUid | number | Последний обработанный UID. |
| 7 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | Максимальный обработанный UID. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = ImapProcessInBoxToMessage("demo", "secret", "demo", "demo", 1, 1, "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = ImapProcessInBoxToMessage("example", "secret", "example", "example", 2, 2, "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="IoutilReadDir"></a>
## IoutilReadDir

**Категория:** Файлы и S3

Возвращает имена элементов каталога.

### Сигнатура

```lua
files, err, code = IoutilReadDir(path)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | path | string | Путь или шаблон пути |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | files | table | Массив имён файлов. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local files, err, code = IoutilReadDir("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", files)
end

-- Значения всех результирующих переменных
if type(files) == "table" then
  print("files:", JsonToString(files))
else
  print("files:", files)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local files, err, code = IoutilReadDir("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", files)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(files) == "table" then
  print("files:", JsonToString(files))
else
  print("files:", files)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Join"></a>
## Join

**Категория:** Прочее

Объединяет элементы Lua-таблицы в строку через разделитель.

### Сигнатура

```lua
result = Join(s1, sep)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | table | Первая строка / основное входное значение. |
| 2 | sep | string | Разделитель |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = Join({}, ",")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = Join({}, ",")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JWTTokenToJson"></a>
## JWTTokenToJson

**Категория:** Форматы и кодирование

Проверяет JWT по секрету и возвращает payload как Lua-таблицу.

### Сигнатура

```lua
payload, err, code = JWTTokenToJson(token, secret)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | token | string | JWT |
| 2 | secret | string | Секрет |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | payload | table\|nil | JWT payload. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local payload, err, code = JWTTokenToJson("eyJ...", "secret-key")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", payload)
end

-- Значения всех результирующих переменных
if type(payload) == "table" then
  print("payload:", JsonToString(payload))
else
  print("payload:", payload)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local payload, err, code = JWTTokenToJson("eyJ...", "secret-key")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", payload)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(payload) == "table" then
  print("payload:", JsonToString(payload))
else
  print("payload:", payload)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JWTTokenWithoutVerificationToJson"></a>
## JWTTokenWithoutVerificationToJson

**Категория:** Форматы и кодирование

Разбирает payload JWT без проверки подписи.

### Сигнатура

```lua
payload, err, code = JWTTokenWithoutVerificationToJson(token)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | token | string | JWT |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | payload | table\|nil | JWT payload без верификации. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local payload, err, code = JWTTokenWithoutVerificationToJson("eyJ...")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", payload)
end

-- Значения всех результирующих переменных
if type(payload) == "table" then
  print("payload:", JsonToString(payload))
else
  print("payload:", payload)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local payload, err, code = JWTTokenWithoutVerificationToJson("eyJ...")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", payload)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(payload) == "table" then
  print("payload:", JsonToString(payload))
else
  print("payload:", payload)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JsonToJWTToken"></a>
## JsonToJWTToken

**Категория:** Форматы и кодирование

Создаёт JWT из Lua-таблицы с указанным алгоритмом и key ID.

### Сигнатура

```lua
token, err, code = JsonToJWTToken(s1, secret, methodString, keyID)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | table | Первая строка / основное входное значение. |
| 2 | secret | string | Секрет |
| 3 | methodString | string | Алгоритм подписи JWT. |
| 4 | keyID | string | Опциональный JWT key id (kid). |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | token | string | JWT token. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local token, err, code = JsonToJWTToken({sub="101", role="USER", exp=1893456000}, "jwt-secret", "HS256", "main-key")
if code == 0 then print(token) else print(err) end

-- Значения всех результирующих переменных
print("token:", token)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local token, err, code = JsonToJWTToken({order_id=1001, scope="orders.read"}, "jwt-secret", "HS256", "")
print(code, err, token)

-- Значения всех результирующих переменных
print("token:", token)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JsonToString"></a>
## JsonToString

**Категория:** Форматы и кодирование

Сериализует Lua-таблицу в JSON.

### Сигнатура

```lua
json = JsonToString(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | table | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | json | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local json = JsonToString({id=1001, state="NEW", total=125000})
print(json)

-- Значения всех результирующих переменных
print("json:", json)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local payload = {user={id=101, name="Aruzhan"}, roles={"USER", "EDITOR"}}
local json = JsonToString(payload)
print("json:", json)

-- Значения всех результирующих переменных
print("json:", json)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JsonToStringIndent"></a>
## JsonToStringIndent

**Категория:** Форматы и кодирование

Сериализует Lua-таблицу в форматированный JSON.

### Сигнатура

```lua
json = JsonToStringIndent(s1, prefix, indent)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | table | Первая строка / основное входное значение. |
| 2 | prefix | string | Префикс/служебный идентификатор (зависит от функции). |
| 3 | indent | string | Строка отступа для pretty JSON. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | json | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local json = JsonToStringIndent({id=1001, state="NEW"}, "", "  ")
print(json)

-- Значения всех результирующих переменных
print("json:", json)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local json = JsonToStringIndent({items={{id=1},{id=2}}}, "", "    ")
print(json)

-- Значения всех результирующих переменных
print("json:", json)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="JsonToXML"></a>
## JsonToXML

**Категория:** Форматы и кодирование

Преобразует Lua-таблицу/JSON-структуру в XML.

### Сигнатура

```lua
xml = JsonToXML(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | table | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | xml | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local xml = JsonToXML({order={id=1001, state="NEW"}})
print(xml)

-- Значения всех результирующих переменных
print("xml:", xml)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local xml = JsonToXML({customer={name="Aruzhan", city="Almaty"}})
print(xml)

-- Значения всех результирующих переменных
print("xml:", xml)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafFkaReaderList"></a>
## KafFkaReaderList

**Категория:** Очереди и Kafka

Возвращает список созданных Kafka reader-ов.

### Сигнатура

```lua
err, code, readers = KafFkaReaderList()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Ошибка (обычно пусто). |
| 2 | code | integer | Код состояния. |
| 3 | readers | table | Список Kafka reader-ов. |

### Примеры

#### Пример 1

```lua
local err, code, readers = KafFkaReaderList()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", readers)
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
if type(readers) == "table" then
  print("readers:", JsonToString(readers))
else
  print("readers:", readers)
end
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code, readers = KafFkaReaderList()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", readers)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
if type(readers) == "table" then
  print("readers:", JsonToString(readers))
else
  print("readers:", readers)
end
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaAvroConsumer"></a>
## KafkaAvroConsumer

**Категория:** Очереди и Kafka

Запускает/настраивает Avro consumer Kafka по таблице параметров.

### Сигнатура

```lua
err, code = KafkaAvroConsumer(params)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | params | table | Lua-таблица параметров функции. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaAvroConsumer({value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaAvroConsumer({value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaAvroProducer"></a>
## KafkaAvroProducer

**Категория:** Очереди и Kafka

Отправляет Avro-сообщение в Kafka по таблице параметров.

### Сигнатура

```lua
err, code = KafkaAvroProducer(params)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | params | table | Lua-таблица параметров функции. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaAvroProducer({value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaAvroProducer({value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaReaderClose"></a>
## KafkaReaderClose

**Категория:** Очереди и Kafka

Закрывает Kafka reader по идентификатору.

### Сигнатура

```lua
err, code = KafkaReaderClose(readerID)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | readerID | string | Уникальный идентификатор Kafka reader-а. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaReaderClose("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaReaderClose("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaReaderCreate"></a>
## KafkaReaderCreate

**Категория:** Очереди и Kafka

Создаёт Kafka reader и связывает его с Lua callback.

### Сигнатура

```lua
err, code = KafkaReaderCreate(readerID, host, topic, offset, cb, confString, ppartition)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | readerID | string | Уникальный идентификатор Kafka reader-а. |
| 2 | host | string | Адрес сервиса. |
| 3 | topic | string | Kafka topic |
| 4 | offset | integer | Начальный Kafka offset. |
| 5 | cb | string | Имя Lua callback-функции. |
| 6 | confString | string | Пользовательская строка конфигурации, передаваемая callback. |
| 7 | ppartition | integer | Номер Kafka partition. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
function onKafkaMessage(conf, offset, data, partition)
  print(conf, offset, partition, data)
end
local err, code = KafkaReaderCreate("orders-reader", "kafka.example.com:9092", "orders", 0, "onKafkaMessage", "worker=orders", 0)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
function onAudit(conf, offset, data, partition) print("audit", offset, data) end
local err, code = KafkaReaderCreate("audit-reader", "127.0.0.1:9092", "audit", 0, "onAudit", "worker=audit", 1)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaReaderCreate2"></a>
## KafkaReaderCreate2

**Категория:** Очереди и Kafka

Создаёт Kafka reader с group/SASL-параметрами и Lua callback.

### Сигнатура

```lua
err, code = KafkaReaderCreate2(readerID, host, group, username, password, topic, offset, cb, confString, ppartition)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | readerID | string | Уникальный идентификатор Kafka reader-а. |
| 2 | host | string | Адрес сервиса. |
| 3 | group | string | Kafka consumer group. |
| 4 | username | string | Логин |
| 5 | password | string | Пароль |
| 6 | topic | string | Kafka topic |
| 7 | offset | integer | Начальный Kafka offset. |
| 8 | cb | string | Имя Lua callback-функции. |
| 9 | confString | string | Пользовательская строка конфигурации, передаваемая callback. |
| 10 | ppartition | integer | Номер Kafka partition. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
function onKafkaMessage(conf, offset, data, partition)
  print(conf, offset, partition, data)
end
local err, code = KafkaReaderCreate2("orders-reader", "kafka.example.com:9092", "damubpm-workers", "kafka-user", "secret", "orders", 0, "onKafkaMessage", "worker=orders", 0)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
function onAudit(conf, offset, data, partition) print(offset, data) end
local err, code = KafkaReaderCreate2("audit-reader", "127.0.0.1:9092", "audit-workers", "user", "secret", "audit", 0, "onAudit", "worker=audit", 1)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaWriteMessage"></a>
## KafkaWriteMessage

**Категория:** Очереди и Kafka

Отправляет строковое сообщение в Kafka topic.

### Сигнатура

```lua
err, code = KafkaWriteMessage(broker, topic, msg)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | broker | string | Адрес Kafka broker |
| 2 | topic | string | Kafka topic |
| 3 | msg | string | Сообщение |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaWriteMessage("kafka.example.com:9092", "events", "{\"type\":\"order.created\",\"id\":1001}")
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaWriteMessage("127.0.0.1:9092", "audit", "user 101 logged in")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaWriteMessage2"></a>
## KafkaWriteMessage2

**Категория:** Очереди и Kafka

Отправляет сообщение в Kafka с логином и паролем.

### Сигнатура

```lua
err, code = KafkaWriteMessage2(broker, username, password, topic, msg)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | broker | string | Адрес Kafka broker |
| 2 | username | string | Логин |
| 3 | password | string | Пароль |
| 4 | topic | string | Kafka topic |
| 5 | msg | string | Сообщение |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaWriteMessage2("kafka.example.com:9092", "kafka-user", "secret", "events", "order:1001")
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaWriteMessage2("127.0.0.1:9092", "user", "secret", "audit", "login:101")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaWriteMessage3"></a>
## KafkaWriteMessage3

**Категория:** Очереди и Kafka

Отправляет сообщение в Kafka с ключом и выбранным SASL-механизмом.

### Сигнатура

```lua
err, code = KafkaWriteMessage3(broker, username, password, topic, msg, key, mechanismStr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | broker | string | Адрес Kafka broker |
| 2 | username | string | Логин |
| 3 | password | string | Пароль |
| 4 | topic | string | Kafka topic |
| 5 | msg | string | Сообщение |
| 6 | key | string | Ключ шифрования либо ключ сообщения. |
| 7 | mechanismStr | string | SASL mechanism, например SHA256, в формате ожидаемом реализацией. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaWriteMessage3("kafka.example.com:9092", "kafka-user", "secret", "events", "order:1001", "1001", "SHA256")
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaWriteMessage3("127.0.0.1:9092", "user", "secret", "audit", "login:101", "101", "SHA256")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaEnqueue"></a>
## KafkaEnqueue

**Категория:** Очереди и Kafka

Добавляет сообщение в заранее инициализированную очередь Kafka producer-а.

### Сигнатура

```lua
err, code = KafkaEnqueue(name, msg, headers)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | name | string | Имя ресурса/producer-а. |
| 2 | msg | string | Сообщение |
| 3 | headers | table | Lua-таблица HTTP-заголовков key=value |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaEnqueue("events-producer", "order:1001", {event_type="order.created", source="damubpm"})
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaEnqueue("audit-producer", "login:101", {event_type="user.login"})
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KafkaInitProducer"></a>
## KafkaInitProducer

**Категория:** Очереди и Kafka

Инициализирует именованный асинхронный Kafka producer.

### Сигнатура

```lua
err, code = KafkaInitProducer(broker, username, password, topic, name)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | broker | string | Адрес Kafka broker |
| 2 | username | string | Логин |
| 3 | password | string | Пароль |
| 4 | topic | string | Kafka topic |
| 5 | name | string | Имя ресурса/producer-а. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KafkaInitProducer("kafka.example.com:9092", "kafka-user", "secret", "events", "events-producer")
if code ~= 0 then print(err) else print("producer initialized") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KafkaInitProducer("127.0.0.1:9092", "user", "secret", "audit", "audit-producer")
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KillProcess"></a>
## KillProcess

**Категория:** Система и выполнение

Завершает локальный процесс по PID.

### Сигнатура

```lua
err, code = KillProcess(pid)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | pid | integer | PID процесса. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = KillProcess(12345)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = KillProcess(12345)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LdapCreateUser"></a>
## LdapCreateUser

**Категория:** Безопасность и LDAP

Создаёт LDAP-пользователя через настроенное LDAP-подключение.

### Сигнатура

```lua
err, code = LdapCreateUser(ldapId, userName, password)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | ldapId | integer | Идентификатор LDAP-конфигурации DamuBPM. |
| 2 | userName | string | Логин создаваемого LDAP-пользователя. |
| 3 | password | string | Пароль |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = LdapCreateUser(12345, "demo", "secret")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = LdapCreateUser(12345, "example", "secret")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LdapSearch"></a>
## LdapSearch

**Категория:** Безопасность и LDAP

Выполняет LDAP search и возвращает выбранные атрибуты записей.

### Сигнатура

```lua
rows, err, code = LdapSearch(user, password, host, baseDN, filter, ...)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user | string | Пользователь/LDAP bind DN. |
| 2 | password | string | Пароль |
| 3 | host | string | Адрес сервиса. |
| 4 | baseDN | string | LDAP Base DN |
| 5 | filter | string | LDAP filter |
| 6… | ... | varargs | Имена LDAP-атрибутов, которые нужно вернуть (например, "cn", "mail", "department"). |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | LDAP entries. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = LdapSearch(
  "cn=svc,ou=service,dc=example,dc=com", "secret",
  "ldap://ldap.example.com:389", "dc=example,dc=com",
  "(&(objectClass=person)(sAMAccountName=test.user))",
  "cn", "mail", "department", "sAMAccountName"
)
if code == 0 then for _, row in ipairs(rows) do print(row.DN, row.cn, row.mail) end else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = LdapSearch(
  "cn=svc,ou=service,dc=example,dc=com", "secret",
  "ldap://ldap.example.com:389", "ou=Users,dc=example,dc=com",
  "(department=IT)", "displayName", "title", "telephoneNumber"
)
print(code, err, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LdapSearchCaCert"></a>
## LdapSearchCaCert

**Категория:** Безопасность и LDAP

Выполняет LDAP search с пользовательским CA-сертификатом.

### Сигнатура

```lua
rows, err, code = LdapSearchCaCert(user, password, host, baseDN, filter, cacert, ...)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | user | string | Пользователь/LDAP bind DN. |
| 2 | password | string | Пароль |
| 3 | host | string | Адрес сервиса. |
| 4 | baseDN | string | LDAP Base DN |
| 5 | filter | string | LDAP filter |
| 6 | cacert | string | PEM CA-сертификат; пустая строка — без собственного CA. |
| 7… | ... | varargs | Имена LDAP-атрибутов, которые нужно вернуть (например, "cn", "mail", "department"). |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | LDAP entries. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local ca, readErr, readCode = ReadFile("/etc/ssl/certs/company-ca.pem")
if readCode ~= 0 then print(readErr) return end
local rows, err, code = LdapSearchCaCert(
  "cn=svc,ou=service,dc=example,dc=com", "secret",
  "ldaps://ldap.example.com:636", "dc=example,dc=com",
  "(sAMAccountName=test.user)", ca, "cn", "mail", "department"
)
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = LdapSearchCaCert(
  "cn=svc,ou=service,dc=example,dc=com", "secret",
  "ldaps://ldap.example.com:636", "dc=example,dc=com",
  "(objectClass=group)", "", "cn", "description"
)
print(code, err, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LoadScript"></a>
## LoadScript

**Категория:** Система и выполнение

Загружает Lua-скрипт из таблицы luas по code и выполняет его.

### Сигнатура

```lua
err, code = LoadScript(Code)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | Code | string | Код Lua-скрипта в таблице luas. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = LoadScript("APP_TITLE")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = LoadScript("APP_TITLE")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LoadString"></a>
## LoadString

**Категория:** Система и выполнение

Компилирует переданную Lua-строку в текущем state.

### Сигнатура

```lua
err, code = LoadString(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = LoadString("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = LoadString("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="LoadStringNamed"></a>
## LoadStringNamed

**Категория:** Система и выполнение

Компилирует Lua-строку с заданным именем chunk-а.

### Сигнатура

```lua
err, code = LoadStringNamed(str, name)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | name | string | Имя ресурса/producer-а. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = LoadStringNamed("demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = LoadStringNamed("example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Md5"></a>
## Md5

**Категория:** Прочее

Возвращает MD5-хеш строки в hex.

### Сигнатура

```lua
result = Md5(param1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | param1 | string | Param1 |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = Md5("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = Md5("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="MkdirAll"></a>
## MkdirAll

**Категория:** Файлы и S3

Создаёт каталог вместе с недостающими родительскими каталогами.

### Сигнатура

```lua
err, code = MkdirAll(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = MkdirAll("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = MkdirAll("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="MqReceive"></a>
## MqReceive

**Категория:** Очереди и Kafka

Запускает получение сообщений из AMQP/RabbitMQ и обработку callback-скриптом.

### Сигнатура

```lua
err, code = MqReceive(ConnStr, Queue, Exchange, RoutingKey, durable, autoDelete, cb, cbParams)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | ConnStr | string | AMQP connection string. |
| 2 | Queue | string | Имя AMQP-очереди. |
| 3 | Exchange | string | Имя AMQP exchange. |
| 4 | RoutingKey | string | AMQP routing key. |
| 5 | durable | boolean | Признак durable очереди/exchange. |
| 6 | autoDelete | boolean | Признак автоматического удаления очереди. |
| 7 | cb | string | Имя Lua callback-функции. |
| 8 | cbParams | string | Строка параметров, передаваемая callback. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = MqReceive("demo", "demo", "demo", "demo", true, true, "demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = MqReceive("example", "example", "example", "example", false, false, "example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="MqSend"></a>
## MqSend

**Категория:** Очереди и Kafka

Отправляет сообщение в AMQP/RabbitMQ.

### Сигнатура

```lua
err, code = MqSend(ConnStr, Queue, Exchange, routingKey, Body, durable, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | ConnStr | string | AMQP connection string. |
| 2 | Queue | string | Имя AMQP-очереди. |
| 3 | Exchange | string | Имя AMQP exchange. |
| 4 | routingKey | string | AMQP routing key. |
| 5 | Body | string | Тело AMQP-сообщения. |
| 6 | durable | boolean | Признак durable очереди/exchange. |
| 7 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = MqSend("demo", "demo", "demo", "demo", "Hello from Lua", true, true)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = MqSend("example", "example", "example", "example", "Hello from Lua", false, false)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="OsStat"></a>
## OsStat

**Категория:** Система и выполнение

Возвращает CPU, RAM и uptime текущего сервера.

### Сигнатура

```lua
stats, err, code = OsStat()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | stats | table\|nil | CPU/RAM/uptime. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local stats, err, code = OsStat()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", stats)
end

-- Значения всех результирующих переменных
if type(stats) == "table" then
  print("stats:", JsonToString(stats))
else
  print("stats:", stats)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local stats, err, code = OsStat()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", stats)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(stats) == "table" then
  print("stats:", JsonToString(stats))
else
  print("stats:", stats)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="PDFBatch"></a>
## PDFBatch

**Категория:** Файлы и S3

Применяет пакет операций к PDF: шрифты, вставку текста/изображений и другие действия из таблицы actions.

### Сигнатура

```lua
err, code = PDFBatch(filename, actions)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | filename | string | Имя или путь файла. |
| 2 | actions | table | Таблица операций |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local actions = {
  {action="AddFont", param1="dejavu", param2="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"},
  {action="SetFont", param1="dejavu", param2="", param3=12},
  {action="Insert", param1="DamuBPM", param2=1, param3=50, param4=50, param5=300, param6=30, param7=0},
  {action="Save", param1="/tmp/result.pdf"}
}
local err, code = PDFBatch("/tmp/source.pdf", actions)
if code ~= 0 then print(err) else print("saved /tmp/result.pdf") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local actions = {
  {action="InsertImg", param1="/tmp/stamp.png", param2=1, param3=420, param4=40, param5=100, param6=60},
  {action="Save", param1="/tmp/stamped.pdf"}
}
local err, code = PDFBatch("/tmp/source.pdf", actions)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="PDFInfo"></a>
## PDFInfo

**Категория:** Файлы и S3

Возвращает информацию о PDF, включая количество страниц.

### Сигнатура

```lua
info, err, code = PDFInfo(filename)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | filename | string | Имя или путь файла. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | info | table | Информация о PDF. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local info, err, code = PDFInfo("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", info)
end

-- Значения всех результирующих переменных
if type(info) == "table" then
  print("info:", JsonToString(info))
else
  print("info:", info)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local info, err, code = PDFInfo("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", info)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
if type(info) == "table" then
  print("info:", JsonToString(info))
else
  print("info:", info)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="PNG2JPEG"></a>
## PNG2JPEG

**Категория:** Файлы и S3

Конвертирует PNG-файл в JPEG.

### Сигнатура

```lua
err, code = PNG2JPEG(src, dst)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | src | string | Исходный путь |
| 2 | dst | string | Целевой путь |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = PNG2JPEG("/tmp/source.txt", "/tmp/copy.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = PNG2JPEG("/tmp/source.txt", "/tmp/copy.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ParseEmailAddress"></a>
## ParseEmailAddress

**Категория:** Почта и сообщения

Разбирает email-строку на отображаемое имя и адрес, включая KOI8-R/KOI8-U варианты.

### Сигнатура

```lua
name, address, err, code = ParseEmailAddress(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | name | string | Отображаемое имя. |
| 2 | address | string | Email-адрес. |
| 3 | err | string | Ошибка разбора. |
| 4 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local name, address, err, code = ParseEmailAddress('Aruzhan <aruzhan@example.com>')
if code == 0 then print(name, address) else print(err) end

-- Значения всех результирующих переменных
print("name:", name)
print("address:", address)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local name, address, err, code = ParseEmailAddress('support@example.com')
print(code, err, name, address)

-- Значения всех результирующих переменных
print("name:", name)
print("address:", address)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ParseHTMLTemplate"></a>
## ParseHTMLTemplate

**Категория:** Прочее

Рендерит HTML-шаблон с данными и user ID.

### Сигнатура

```lua
html, err, code = ParseHTMLTemplate(s, arr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |
| 2 | arr | table | Lua-таблица данных/параметров. |
| 3 | userId | integer | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | html | any | Результат операции. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local html, err, code = ParseHTMLTemplate("<h1>{{.name}}</h1><p>Order: {{.order_no}}</p>", {name="Aruzhan", order_no="ORD-1001"}, 101)
if code == 0 then print(html) else print(err) end

-- Значения всех результирующих переменных
print("html:", html)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local html, err, code = ParseHTMLTemplate("<p>{{.title}}: {{.amount}}</p>", {title="Total", amount=125000}, 101)
print(code, err, html)

-- Значения всех результирующих переменных
print("html:", html)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ParseTemplate"></a>
## ParseTemplate

**Категория:** Прочее

Рендерит текстовый шаблон с данными и user ID.

### Сигнатура

```lua
text, err, code = ParseTemplate(s, arr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |
| 2 | arr | table | Lua-таблица данных/параметров. |
| 3 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | text | any | Результат операции. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local text, err, code = ParseTemplate("Hello {{.name}}, order {{.order_no}} is ready", {name="Aruzhan", order_no="ORD-1001"}, "101")
if code == 0 then print(text) else print(err) end

-- Значения всех результирующих переменных
print("text:", text)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local text, err, code = ParseTemplate("{{.title}} = {{.amount}}", {title="Total", amount=125000}, "101")
print(code, err, text)

-- Значения всех результирующих переменных
print("text:", text)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ParseSecond"></a>
## ParseSecond

**Категория:** Прочее

Проверяет cron-выражение парсером, поддерживающим секунды.

### Сигнатура

```lua
err, code = ParseSecond(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = ParseSecond("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = ParseSecond("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="PathEscape"></a>
## PathEscape

**Категория:** Файлы и S3

URL-экранирует значение для использования в path-сегменте.

### Сигнатура

```lua
result = PathEscape(value)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | value | any | Value |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = PathEscape("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = PathEscape("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Plugin"></a>
## Plugin

**Категория:** Система и выполнение

Загружает Go plugin (.so), находит функцию и вызывает её с Lua-таблицей параметров.

### Сигнатура

```lua
result, err, code = Plugin(pluginPath, functionName, params)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | pluginPath | string | Путь к Go plugin (.so). |
| 2 | functionName | string | Имя экспортированной функции plugin-а. |
| 3 | params | table | Lua-таблица параметров функции. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | any | Результат операции. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = Plugin("/tmp/demo.txt", "demo", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = Plugin("/tmp/demo.txt", "example", {value=42, name="demo"})
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Query"></a>
## Query

**Категория:** SQL и данные

Выполняет DamuBPM QueryByUrl и возвращает строки результата.

### Сигнатура

```lua
rows, err, code = Query(urlStr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | urlStr | string | Строка QueryByUrl DamuBPM; точный формат зависит от настроенного query/endpoint. |
| 2 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table | Строки QueryByUrl. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = Query("orders?state=NEW", "101")
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = Query("customers?city=Almaty", "101")
print(code, err, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="QueryEscape"></a>
## QueryEscape

**Категория:** SQL и данные

URL-экранирует строку для query-параметра.

### Сигнатура

```lua
result = QueryEscape(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = QueryEscape("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = QueryEscape("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="QueryUnescape"></a>
## QueryUnescape

**Категория:** SQL и данные

Декодирует URL-escaped строку query-параметра.

### Сигнатура

```lua
result = QueryUnescape(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = QueryUnescape("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = QueryUnescape("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="QueryWithCount"></a>
## QueryWithCount

**Категория:** SQL и данные

Выполняет QueryByUrl и возвращает общее количество и строки.

### Сигнатура

```lua
count, rows, err, code = QueryWithCount(urlStr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | urlStr | string | Строка QueryByUrl DamuBPM; точный формат зависит от настроенного query/endpoint. |
| 2 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | count | integer | Общее количество записей. |
| 2 | rows | table | Строки результата. |
| 3 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 4 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local count, rows, err, code = QueryWithCount("orders?state=NEW", "101")
if code == 0 then print("count:", count, JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
print("count:", count)
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local count, rows, err, code = QueryWithCount("customers?city=Almaty", "101")
print(code, err, count, rows and #rows or 0)

-- Значения всех результирующих переменных
print("count:", count)
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="QueryCount"></a>
## QueryCount

**Категория:** SQL и данные

Выполняет QueryByUrl в режиме подсчёта и возвращает общее количество.

### Сигнатура

```lua
count, err, code = QueryCount(urlStr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | urlStr | string | Строка QueryByUrl DamuBPM; точный формат зависит от настроенного query/endpoint. |
| 2 | userId | string | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | count | integer | Общее количество записей. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local count, err, code = QueryCount("orders?state=NEW", "101")
if code == 0 then print("count:", count) else print(err) end

-- Значения всех результирующих переменных
print("count:", count)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local count, err, code = QueryCount("customers?city=Almaty", "101")
print(code, err, count)

-- Значения всех результирующих переменных
print("count:", count)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RateLimiter"></a>
## RateLimiter

**Категория:** Прочее

Проверяет лимит обращений для комбинации ключа/IP за заданный интервал.

### Сигнатура

```lua
err, code = RateLimiter(uniq, ip, interval, limit)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | uniq | string | Уникальный ключ rate limiter-а. |
| 2 | ip | string | IP или иной ключ клиента. |
| 3 | interval | string | Интервал как Go duration, например 10s или 1m. |
| 4 | limit | integer | Максимальное число разрешённых обращений за интервал. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = RateLimiter("login", "192.0.2.10", "1m", 10)
if code ~= 0 then print("blocked:", err) else print("allowed") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = RateLimiter("api-orders", "user:101", "10s", 20)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ReadFile"></a>
## ReadFile

**Категория:** Файлы и S3

Читает файл целиком и возвращает его содержимое.

### Сигнатура

```lua
content, err, code = ReadFile(fileName)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | content | any | Результат операции. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local content, err, code = ReadFile("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", content)
end

-- Значения всех результирующих переменных
print("content:", content)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local content, err, code = ReadFile("/tmp/demo.txt")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", content)
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("content:", content)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ReadFilePart"></a>
## ReadFilePart

**Категория:** Файлы и S3

Читает файл порциями и передаёт каждую порцию в Lua callback.

### Сигнатура

```lua
err, code = ReadFilePart(fileName, chunkSize, callback)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |
| 2 | chunkSize | integer | Размер одной читаемой порции в байтах. |
| 3 | callback | function | Lua callback-функция |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local total = 0
local err, code = ReadFilePart("/tmp/large.bin", 65536, function(chunk)
  total = total + #chunk
end)
print("bytes read:", total, "code:", code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local parts = 0
local err, code = ReadFilePart("/tmp/data.txt", 4096, function(chunk)
  parts = parts + 1
  print("part", parts, "bytes", #chunk)
end)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="DeleteExpiredSessions"></a>
## DeleteExpiredSessions

**Категория:** DamuBPM API

Удаляет пользовательские сессии, неактивные более 15 минут.

### Сигнатура

```lua
DeleteExpiredSessions()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Явных возвращаемых значений нет. |  |  |  |

### Примеры

#### Пример 1

```lua
DeleteExpiredSessions()
print("done")

-- Функция не возвращает значений.
```

#### Пример 2

```lua
DeleteExpiredSessions()
print("done")
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Функция не возвращает значений.
```

[↑ К оглавлению](#оглавление)

---

<a id="RedisSqlQueryRow2"></a>
## RedisSqlQueryRow2

**Категория:** SQL и данные

Выполняет SQL через Redis ORM и возвращает одну строку как Lua-таблицу.

### Сигнатура

```lua
row, err, code = RedisSqlQueryRow2(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | row | table\|nil | Одна строка результата. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local row, err, code = RedisSqlQueryRow2(
  "select id, value from cache_items where id = ?",
  10
)
if code == 0 then print(row.value) else print(err) end

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local row, err, code = RedisSqlQueryRow2(
  "select value from cache_items where group_code = ? and item_code = ?",
  "MENU", "MAIN"
)
print(code, row and row.value)

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RedisSqlQueryRows"></a>
## RedisSqlQueryRows

**Категория:** SQL и данные

Выполняет SQL через Redis ORM и возвращает массив строк.

### Сигнатура

```lua
rows, err, code = RedisSqlQueryRows(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | Массив строк. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = RedisSqlQueryRows(
  "select id, value from cache_items where group_code = ?",
  "MENU"
)
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = RedisSqlQueryRows(
  "select id from cache_items where id in (?, ?)",
  10, 20
)
print(code, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RegexpCheck"></a>
## RegexpCheck

**Категория:** Строки и утилиты

Проверяет строку на соответствие регулярному выражению.

### Сигнатура

```lua
result = RegexpCheck(text, pattern)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | text | string | Исходный текст |
| 2 | pattern | string | Регулярное выражение |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = RegexpCheck("Hello 123", "^\\d+$")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = RegexpCheck("Hello 123", "^\\d+$")
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RegexpFindAllStringsAndJoin"></a>
## RegexpFindAllStringsAndJoin

**Категория:** Строки и утилиты

Находит все совпадения regexp и объединяет их указанным разделителем.

### Сигнатура

```lua
text = RegexpFindAllStringsAndJoin(expr, str, cnt, sep)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | expr | string | Регулярное либо cron-выражение (зависит от функции). |
| 2 | str | string | Строковое значение. |
| 3 | cnt | integer | Максимум совпадений; -1 — найти все. |
| 4 | sep | string | Разделитель |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | text | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local text = RegexpFindAllStringsAndJoin("demo", "demo", 1, ",")
print(text)

-- Значения всех результирующих переменных
print("text:", text)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local text = RegexpFindAllStringsAndJoin("example", "example", 2, ",")
print(text)

-- Значения всех результирующих переменных
print("text:", text)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RegexpFindStringSubmatch"></a>
## RegexpFindStringSubmatch

**Категория:** Строки и утилиты

Возвращает указанную группу первого совпадения regexp.

### Сигнатура

```lua
result = RegexpFindStringSubmatch(text, pattern, groupIndex)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | text | string | Исходный текст |
| 2 | pattern | string | Регулярное выражение |
| 3 | groupIndex | integer | Индекс regexp-группы. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = RegexpFindStringSubmatch("Hello 123", "^\\d+$", 1)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = RegexpFindStringSubmatch("Hello 123", "^\\d+$", 2)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ReplaceWholeWord"></a>
## ReplaceWholeWord

**Категория:** Строки и утилиты

Заменяет только целые слова в строке.

### Сигнатура

```lua
result = ReplaceWholeWord(text, oldWord, newWord)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | text | string | Исходный текст |
| 2 | oldWord | string | Целое слово для замены. |
| 3 | newWord | string | Новое слово. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = ReplaceWholeWord("Hello 123", "demo", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = ReplaceWholeWord("Hello 123", "example", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RollBackTransaction"></a>
## RollBackTransaction

**Категория:** Прочее

Откатывает транзакцию, созданную транзакционным API.

### Сигнатура

```lua
err, code = RollBackTransaction()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = RollBackTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = RollBackTransaction()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Rollback"></a>
## Rollback

**Категория:** Прочее

Откатывает текущую транзакцию.

### Сигнатура

```lua
err, code = Rollback()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = Rollback()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = Rollback()
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RuNum2Word"></a>
## RuNum2Word

**Категория:** Строки и утилиты

Преобразует число в сумму прописью на русском языке.

### Сигнатура

```lua
result = RuNum2Word(number, upp, valCode)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | number | string | Число в строковом виде. |
| 2 | upp | boolean | true — начинать результат с заглавной буквы. |
| 3 | valCode | string | Код валюты. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = RuNum2Word("demo", true, "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = RuNum2Word("example", false, "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="KkNum2Word"></a>
## KkNum2Word

**Категория:** Строки и утилиты

Преобразует число в сумму прописью на казахском языке.

### Сигнатура

```lua
result = KkNum2Word(number, upp, valCode)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | number | string | Число в строковом виде. |
| 2 | upp | boolean | true — начинать результат с заглавной буквы. |
| 3 | valCode | string | Код валюты. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = KkNum2Word("demo", true, "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = KkNum2Word("example", false, "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="RunParallel"></a>
## RunParallel

**Категория:** Система и выполнение

Запускает несколько экземпляров Lua-скрипта параллельно с THREAD_* глобальными переменными.

### Сигнатура

```lua
err, code = RunParallel(prefix, totalCount, script)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | prefix | string | Префикс/служебный идентификатор (зависит от функции). |
| 2 | totalCount | integer | Количество параллельных Lua-задач. |
| 3 | script | string | Lua-код для выполнения. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local script = "\n  print(THREAD_PREFIX, THREAD_KEY, THREAD_CURRENT, THREAD_TOTAL_COUNT)\n"
local err, code = RunParallel("recalc-orders", 4, script)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local script = "\n  local rows, err, code = SqlQueryRows(\"select id from orders where mod(id, ?) = ?\", THREAD_TOTAL_COUNT, THREAD_CURRENT)\n  if code == 0 then print(\"thread\", THREAD_CURRENT, \"rows\", #rows) else print(err) end\n"
local err, code = RunParallel("orders", 8, script)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="S3GetObject"></a>
## S3GetObject

**Категория:** Файлы и S3

Читает объект из S3/MinIO и возвращает содержимое.

### Сигнатура

```lua
data, err, code = S3GetObject(s3endpoint, s3access_key_id, s3secret_access_key, s3usessl, s3bucket, filePath)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s3endpoint | string | S3/MinIO endpoint |
| 2 | s3access_key_id | string | Access Key |
| 3 | s3secret_access_key | string | Secret Key |
| 4 | s3usessl | boolean | Использовать HTTPS |
| 5 | s3bucket | string | Имя bucket-а |
| 6 | filePath | string | Ключ/путь объекта внутри S3 bucket. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | data | string\|nil | Содержимое объекта. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local data, err, code = S3GetObject("minio.example.com:9000", "ACCESS_KEY", "SECRET_KEY", true, "documents", "2026/report.pdf")
if code == 0 then print("bytes:", #data) else print(err) end

-- Значения всех результирующих переменных
print("data:", data)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local data, err, code = S3GetObject("127.0.0.1:9000", "minio", "secret", false, "archive", "invoices/invoice-1001.xml")
print(code, err, data and #data or 0)

-- Значения всех результирующих переменных
print("data:", data)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="S3ListObjects"></a>
## S3ListObjects

**Категория:** Файлы и S3

Возвращает список объектов S3/MinIO по prefix.

### Сигнатура

```lua
objects, err, code = S3ListObjects(s3endpoint, s3access_key_id, s3secret_access_key, s3usessl, s3bucket, prefix, recursive)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s3endpoint | string | S3/MinIO endpoint |
| 2 | s3access_key_id | string | Access Key |
| 3 | s3secret_access_key | string | Secret Key |
| 4 | s3usessl | boolean | Использовать HTTPS |
| 5 | s3bucket | string | Имя bucket-а |
| 6 | prefix | string | Префикс/служебный идентификатор (зависит от функции). |
| 7 | recursive | boolean | Рекурсивный список |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | objects | table\|nil | Список объектов. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local objects, err, code = S3ListObjects("minio.example.com:9000", "ACCESS_KEY", "SECRET_KEY", true, "documents", "2026/", true)
if code == 0 then for _, obj in ipairs(objects) do print(obj.name, obj.size) end else print(err) end

-- Значения всех результирующих переменных
if type(objects) == "table" then
  print("objects:", JsonToString(objects))
else
  print("objects:", objects)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local objects, err, code = S3ListObjects("127.0.0.1:9000", "minio", "secret", false, "archive", "invoices/", false)
print(code, err, objects and #objects or 0)

-- Значения всех результирующих переменных
if type(objects) == "table" then
  print("objects:", JsonToString(objects))
else
  print("objects:", objects)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="S3UploadObject"></a>
## S3UploadObject

**Категория:** Файлы и S3

Загружает локальный файл в S3/MinIO и возвращает сведения об объекте.

### Сигнатура

```lua
info, err, code = S3UploadObject(s3endpoint, s3access_key_id, s3secret_access_key, s3usessl, s3bucket, objectName, localFilePath)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s3endpoint | string | S3/MinIO endpoint |
| 2 | s3access_key_id | string | Access Key |
| 3 | s3secret_access_key | string | Secret Key |
| 4 | s3usessl | boolean | Использовать HTTPS |
| 5 | s3bucket | string | Имя bucket-а |
| 6 | objectName | string | Ключ создаваемого S3-объекта. |
| 7 | localFilePath | string | Локальный путь файла для загрузки. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | info | table\|nil | Информация о загруженном объекте. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local info, err, code = S3UploadObject("minio.example.com:9000", "ACCESS_KEY", "SECRET_KEY", true, "documents", "2026/report.pdf", "/tmp/report.pdf")
if code == 0 then print(info.name, info.size, info.eTag) else print(err) end

-- Значения всех результирующих переменных
if type(info) == "table" then
  print("info:", JsonToString(info))
else
  print("info:", info)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local info, err, code = S3UploadObject("127.0.0.1:9000", "minio", "secret", false, "archive", "invoices/invoice-1001.xml", "/tmp/invoice-1001.xml")
print(code, err, info and info.name)

-- Значения всех результирующих переменных
if type(info) == "table" then
  print("info:", JsonToString(info))
else
  print("info:", info)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendEmail"></a>
## SendEmail

**Категория:** Почта и сообщения

Отправляет email через канал, настроенный в DamuBPM.

### Сигнатура

```lua
err, code = SendEmail(channelCode, toText, toEmail, subject, body, arg6)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | channelCode | string | Код настроенного почтового канала DamuBPM. |
| 2 | toText | string | Отображаемое имя получателя. |
| 3 | toEmail | string | Email получателя. |
| 4 | subject | string | Тема письма |
| 5 | body | string | Тело сообщения/запроса |
| 6 | arg6 | any | wait: true — ждать отправку; false — отправить асинхронно. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendEmail("EMAIL_MAIN", "Aruzhan", "user@example.com", "Order is ready", "Your order ORD-1001 is ready", true)
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendEmail("EMAIL_MAIN", "Support", "support@example.com", "Background notification", "Sent asynchronously", false)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendMail2"></a>
## SendMail2

**Категория:** Почта и сообщения

Отправляет письмо напрямую через SMTP с TLS-настройками библиотеки.

### Сигнатура

```lua
err, code = SendMail2(from, to, subject, contentType, body, files, smtpHost, smtpPort, login, password, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | from | string | Адрес отправителя |
| 2 | to | table | Массив адресатов |
| 3 | subject | string | Тема письма |
| 4 | contentType | string | MIME Content-Type |
| 5 | body | string | Тело сообщения/запроса |
| 6 | files | table | Массив путей вложений |
| 7 | smtpHost | string | SMTP host |
| 8 | smtpPort | integer | SMTP port |
| 9 | login | string | Логин |
| 10 | password | string | Пароль |
| 11 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendMail2(
  "noreply@example.com", {"user@example.com"}, "DamuBPM notification",
  "text/plain", "Hello from DamuBPM", {},
  "smtp.example.com", 587, "smtp-user", "secret", false
)
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendMail2(
  "noreply@example.com", {"a@example.com", "b@example.com"}, "Monthly report",
  "text/html", "<b>Report is attached</b>", {"/tmp/report.pdf"},
  "smtp.example.com", 587, "smtp-user", "secret", true
)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendMail3"></a>
## SendMail3

**Категория:** Почта и сообщения

Отправляет письмо напрямую через SMTP с TLS 1.2 и ServerName.

### Сигнатура

```lua
err, code = SendMail3(from, to, subject, contentType, body, files, smtpHost, smtpPort, login, password, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | from | string | Адрес отправителя |
| 2 | to | table | Массив адресатов |
| 3 | subject | string | Тема письма |
| 4 | contentType | string | MIME Content-Type |
| 5 | body | string | Тело сообщения/запроса |
| 6 | files | table | Массив путей вложений |
| 7 | smtpHost | string | SMTP host |
| 8 | smtpPort | integer | SMTP port |
| 9 | login | string | Логин |
| 10 | password | string | Пароль |
| 11 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendMail3(
  "noreply@example.com", {"user@example.com"}, "DamuBPM notification",
  "text/plain", "Hello from DamuBPM", {},
  "smtp.example.com", 587, "smtp-user", "secret", false
)
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendMail3(
  "noreply@example.com", {"a@example.com", "b@example.com"}, "Monthly report",
  "text/html", "<b>Report is attached</b>", {"/tmp/report.pdf"},
  "smtp.example.com", 587, "smtp-user", "secret", true
)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendMail2NoTLS"></a>
## SendMail2NoTLS

**Категория:** Почта и сообщения

Отправляет письмо напрямую через SMTP без SSL-режима.

### Сигнатура

```lua
err, code = SendMail2NoTLS(from, to, subject, contentType, body, files, smtpHost, smtpPort, login, password, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | from | string | Адрес отправителя |
| 2 | to | table | Массив адресатов |
| 3 | subject | string | Тема письма |
| 4 | contentType | string | MIME Content-Type |
| 5 | body | string | Тело сообщения/запроса |
| 6 | files | table | Массив путей вложений |
| 7 | smtpHost | string | SMTP host |
| 8 | smtpPort | integer | SMTP port |
| 9 | login | string | Логин |
| 10 | password | string | Пароль |
| 11 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendMail2NoTLS(
  "noreply@example.com", {"user@example.com"}, "DamuBPM notification",
  "text/plain", "Hello from DamuBPM", {},
  "smtp.example.com", 587, "smtp-user", "secret", false
)
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendMail2NoTLS(
  "noreply@example.com", {"a@example.com", "b@example.com"}, "Monthly report",
  "text/html", "<b>Report is attached</b>", {"/tmp/report.pdf"},
  "smtp.example.com", 587, "smtp-user", "secret", true
)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendMail2_ICALTEST"></a>
## SendMail2_ICALTEST

**Категория:** Почта и сообщения

Тестовый вариант SMTP-отправки с calendar/ICS-вложением.

### Сигнатура

```lua
err, code = SendMail2_ICALTEST(from, to, subject, contentType, body, files, smtpHost, smtpPort, login, password, async)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | from | string | Адрес отправителя |
| 2 | to | table | Массив адресатов |
| 3 | subject | string | Тема письма |
| 4 | contentType | string | MIME Content-Type |
| 5 | body | string | Тело сообщения/запроса |
| 6 | files | table | Массив путей вложений |
| 7 | smtpHost | string | SMTP host |
| 8 | smtpPort | integer | SMTP port |
| 9 | login | string | Логин |
| 10 | password | string | Пароль |
| 11 | async | boolean | true — выполнять асинхронно |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendMail2_ICALTEST(
  "noreply@example.com", {"user@example.com"}, "DamuBPM notification",
  "text/plain", "Hello from DamuBPM", {},
  "smtp.example.com", 587, "smtp-user", "secret", false
)
if code ~= 0 then print(err) else print("sent") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendMail2_ICALTEST(
  "noreply@example.com", {"a@example.com", "b@example.com"}, "Monthly report",
  "text/html", "<b>Report is attached</b>", {"/tmp/report.pdf"},
  "smtp.example.com", 587, "smtp-user", "secret", true
)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SendWSAsync"></a>
## SendWSAsync

**Категория:** HTTP / WebSocket

Асинхронно отправляет сообщение по WebSocket.

### Сигнатура

```lua
err, code = SendWSAsync(wsServer, path, msg)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | wsServer | string | WebSocket URL сервера. |
| 2 | path | string | Путь или шаблон пути |
| 3 | msg | string | Сообщение |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SendWSAsync("demo", "/tmp/demo.txt", "Hello from Lua")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SendWSAsync("example", "/tmp/demo.txt", "Hello from Lua")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Sha256"></a>
## Sha256

**Категория:** Прочее

Возвращает SHA-256 хеш строки в hex.

### Сигнатура

```lua
result = Sha256(param1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | param1 | string | Param1 |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = Sha256("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = Sha256("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ShutdownServer"></a>
## ShutdownServer

**Категория:** Система и выполнение

Инициирует остановку сервера с указанным кодом/режимом.

### Сигнатура

```lua
err, code = ShutdownServer(i)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | i | integer | I |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = ShutdownServer(1)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = ShutdownServer(2)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Sleep"></a>
## Sleep

**Категория:** Система и выполнение

Приостанавливает выполнение Lua на заданное число миллисекунд.

### Сигнатура

```lua
Sleep(interval)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | interval | integer | Интервал как Go duration, например 10s или 1m. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Явных возвращаемых значений нет. |  |  |  |

### Примеры

#### Пример 1

```lua
Sleep(1)
print("done")

-- Функция не возвращает значений.
```

#### Пример 2

```lua
Sleep(2)
print("done")

-- Функция не возвращает значений.
```

[↑ К оглавлению](#оглавление)

---

<a id="Split"></a>
## Split

**Категория:** Прочее

Разбивает строку по разделителю и возвращает Lua-массив.

### Сигнатура

```lua
result = Split(str, sep)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |
| 2 | sep | string | Разделитель |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | table | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = Split("demo", ",")
print(result)

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = Split("example", ",")
print(result)

-- Значения всех результирующих переменных
if type(result) == "table" then
  print("result:", JsonToString(result))
else
  print("result:", result)
end
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlCall"></a>
## SqlCall

**Категория:** SQL и данные

Вызывает SQL procedure/statement с именованными IN/OUT параметрами из Lua-таблицы.

### Сигнатура

```lua
out, err, code = SqlCall(query, arr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | query | string | SQL-текст запроса |
| 2 | arr | table | Lua-таблица данных/параметров. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | out | table\|nil | OUT-параметры. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local params = {
  P_ID = {input=true, output=false, value=1001},
  P_RESULT = {input=false, output=true, value=""}
}
local out, err, code = SqlCall("begin demo_proc(:P_ID, :P_RESULT); end;", params)
if code == 0 then print("P_RESULT:", out.P_RESULT) else print(err) end

-- Значения всех результирующих переменных
if type(out) == "table" then
  print("out:", JsonToString(out))
else
  print("out:", out)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local params = {
  P_CUSTOMER = {input=true, output=false, value=501},
  P_TOTAL = {input=false, output=true, value=0}
}
local out, err, code = SqlCall("begin customer_total(:P_CUSTOMER, :P_TOTAL); end;", params)
print(code, err, out and out.P_TOTAL)

-- Значения всех результирующих переменных
if type(out) == "table" then
  print("out:", JsonToString(out))
else
  print("out:", out)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlCallExtDb"></a>
## SqlCallExtDb

**Категория:** SQL и данные

То же, что SqlCall, но через подключение внешней БД по её code.

### Сигнатура

```lua
out, err, code = SqlCallExtDb(extDbCode, query, arr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | extDbCode | string | Код настроенного подключения внешней БД. |
| 2 | query | string | SQL-текст запроса |
| 3 | arr | table | Lua-таблица данных/параметров. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | out | table\|nil | OUT-параметры. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local params = {
  P_ID = {input=true, output=false, value=1001},
  P_STATE = {input=false, output=true, value=""}
}
local out, err, code = SqlCallExtDb("erp", "begin get_order_state(:P_ID, :P_STATE); end;", params)
if code == 0 then print(out.P_STATE) else print(err) end

-- Значения всех результирующих переменных
if type(out) == "table" then
  print("out:", JsonToString(out))
else
  print("out:", out)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local params = {P_CODE={input=true, output=false, value="A-100"}, P_QTY={input=false, output=true, value=0}}
local out, err, code = SqlCallExtDb("warehouse", "begin stock_qty(:P_CODE, :P_QTY); end;", params)
print(code, err, out and out.P_QTY)

-- Значения всех результирующих переменных
if type(out) == "table" then
  print("out:", JsonToString(out))
else
  print("out:", out)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlExec"></a>
## SqlExec

**Категория:** SQL и данные

Выполняет SQL без Lua-return; ошибки пишет в global last_error, last insert id — в sql_last_insert_id.

### Сигнатура

```lua
SqlExec(sql, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sql | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | last_error | global string | Глобальная переменная: текст ошибки, если выполнение не удалось. |
| 2 | sql_last_insert_id | global string | Глобальная переменная: LastInsertId после успешного выполнения. |

### Примеры

#### Пример 1

```lua
SqlExec("update orders set state = ? where id = ?", "DONE", 1001)
if last_error ~= nil and last_error ~= "" then print(last_error) else print("updated") end

-- Значения всех результирующих переменных
print("last_error:", last_error)
print("sql_last_insert_id:", sql_last_insert_id)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
SqlExec("delete from temp_rows where owner_id = ? and created_at < ?", 101, "2026-01-01")
if last_error ~= nil and last_error ~= "" then print(last_error) else print("deleted") end

-- Значения всех результирующих переменных
print("last_error:", last_error)
print("sql_last_insert_id:", sql_last_insert_id)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlExec2"></a>
## SqlExec2

**Категория:** SQL и данные

Выполняет DML SQL и возвращает err/code.

### Сигнатура

```lua
err, code = SqlExec2(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = SqlExec2(
  "update orders set state = ? where id = ?",
  "DONE", 1001
)
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SqlExec2(
  "delete from temp_rows where created_at < ? and owner_id = ?",
  "2026-01-01", 101
)
if code ~= 0 then print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlExec3"></a>
## SqlExec3

**Категория:** SQL и данные

Выполняет DML SQL с исходными типами параметров; текущая реализация вторым return использует длину второго параметра как строки.

### Сигнатура

```lua
err, value = SqlExec3(sq, arg2, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2 | arg2 | any | Первый bind-параметр SQL; в текущей реализации должен быть string, т.к. его длина используется во втором return. |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе. |
| 2 | value | integer | При успехе текущая реализация возвращает длину второго параметра; при ошибке — код ошибки. |

### Примеры

#### Пример 1

```lua
local err, value = SqlExec3(
  "update files set raw_data = ? where id = ?",
  "raw-data-as-string", 77
)
print(err, value)

-- Значения всех результирующих переменных
print("err:", err)
print("value:", value)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, value = SqlExec3(
  "update entity set code = ? where id = ?",
  "ORDER-1001", 1001
)
print(err, value)

-- Значения всех результирующих переменных
print("err:", err)
print("value:", value)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlInsert"></a>
## SqlInsert

**Категория:** SQL и данные

Выполняет INSERT и возвращает last insert ID.

### Сигнатура

```lua
id, err, code = SqlInsert(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | id | string\|integer | Last insert ID. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local id, err, code = SqlInsert(
  "insert into orders(customer_id, state, total) values(?, ?, ?)",
  501, "NEW", 125000
)
if code == 0 then print("new id:", id) else print(err) end

-- Значения всех результирующих переменных
print("id:", id)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local id, err, code = SqlInsert(
  "insert into audit_log(event_type, object_id) values(?, ?)",
  "ORDER_CREATED", 1001
)
print(id, err, code)

-- Значения всех результирующих переменных
print("id:", id)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlQueryRow"></a>
## SqlQueryRow

**Категория:** SQL и данные

Выполняет запрос одной строки и записывает каждую колонку результата в одноимённую глобальную Lua-переменную.

### Сигнатура

```lua
err, code = SqlQueryRow(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пусто при успехе; при успехе колонки доступны как глобальные Lua-переменные. |
| 2 | code | integer | 0 — успех; 2 — нет данных; 3 — больше одной строки; другие — ошибка. |

### Примеры

#### Пример 1

```lua
local err, code = SqlQueryRow(
  "select name, email from users where id = ?",
  101
)
if code == 0 then print(name, email) else print(err) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = SqlQueryRow(
  "select state, total from orders where id = ? and customer_id = ?",
  1001, 501
)
if code == 0 then print(state, total) end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlQueryRow2"></a>
## SqlQueryRow2

**Категория:** SQL и данные

Выполняет запрос одной строки и возвращает её как Lua-таблицу.

### Сигнатура

```lua
row, err, code = SqlQueryRow2(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | row | table\|nil | Одна строка результата. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local row, err, code = SqlQueryRow2(
  "select id, name, email from users where id = ?",
  101
)
if code == 0 then print(row.name, row.email) else print(err) end

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local row, err, code = SqlQueryRow2(
  "select id, state from orders where customer_id = ? and num = ?",
  501, "ORD-2026-001"
)
print(code, err, row and row.state)

-- Значения всех результирующих переменных
if type(row) == "table" then
  print("row:", JsonToString(row))
else
  print("row:", row)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlQueryRows"></a>
## SqlQueryRows

**Категория:** SQL и данные

Выполняет SQL SELECT и возвращает массив строк как Lua-таблицу.

### Сигнатура

```lua
rows, err, code = SqlQueryRows(sq, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | sq | string | SQL-текст запроса |
| 2… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | Массив строк. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = SqlQueryRows(
  "select * from orders where customer_id = ? and created_at >= ? and state = ?",
  501, "2026-01-01", "NEW"
)
if code ~= 0 then print(err) else
  for _, row in ipairs(rows) do print(row.id, row.state) end
end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = SqlQueryRows(
  "select id, total from orders where id in (?, ?) and total >= ?",
  1001, 1002, 50000
)
print("code:", code, "rows:", rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 3

```lua
local rows, err, code = SqlQueryRows(
  "select id, name from customers where city = ?",
  "Almaty"
)
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlQueryRowsExtDb"></a>
## SqlQueryRowsExtDb

**Категория:** SQL и данные

Выполняет SELECT во внешней БД, настроенной по code.

### Сигнатура

```lua
rows, err, code = SqlQueryRowsExtDb(extDbCode, query, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | extDbCode | string | Код настроенного подключения внешней БД. |
| 2 | query | string | SQL-текст запроса |
| 3… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | rows | table\|nil | Массив строк внешней БД. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local rows, err, code = SqlQueryRowsExtDb(
  "erp",
  "select id, name from customers where city = ? and active = ?",
  "Almaty", 1
)
if code == 0 then print(JsonToString(rows)) else print(err) end

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local rows, err, code = SqlQueryRowsExtDb(
  "warehouse",
  "select sku, qty from stock where sku in (?, ?)",
  "A-100", "B-200"
)
print(code, rows and #rows or 0)

-- Значения всех результирующих переменных
if type(rows) == "table" then
  print("rows:", JsonToString(rows))
else
  print("rows:", rows)
end
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="SqlQueryRowsExtDbCursor"></a>
## SqlQueryRowsExtDbCursor

**Категория:** SQL и данные

Открывает SELECT во внешней БД и возвращает функцию-курсор для чтения порциями по 100 строк.

### Сигнатура

```lua
nextChunk, err, code = SqlQueryRowsExtDbCursor(extDbCode, query, ...)
```

> **Примечание:** Важно: каждый ? в SQL должен иметь соответствующее значение после SQL-строки. Не склеивайте значения вручную в SQL.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | extDbCode | string | Код настроенного подключения внешней БД. |
| 2 | query | string | SQL-текст запроса |
| 3… | ... | varargs | Значения для SQL-плейсхолдеров `?` в порядке появления. Количество значений должно соответствовать числу `?`. Таблица разворачивается в несколько параметров; nil передаётся как SQL NULL. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | nextChunk | function\|nil | Функция курсора; каждый вызов возвращает chunk, err, code. Порция — до 100 строк. |
| 2 | err | string | Ошибка открытия курсора. |
| 3 | code | integer | 0 при успехе. |

### Примеры

#### Пример 1

```lua
local nextChunk, err, code = SqlQueryRowsExtDbCursor(
  "erp",
  "select id, name from customers where active = ?",
  1
)
if code ~= 0 then print(err) else
  while true do
    local chunk, chunkErr, chunkCode = nextChunk()
    if chunkCode ~= 0 then print(chunkErr); break end
    if chunk == nil or #chunk == 0 then break end
    for _, row in ipairs(chunk) do print(row.id, row.name) end
  end
end

-- Значения всех результирующих переменных
print("nextChunk:", nextChunk)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local nextChunk, err, code = SqlQueryRowsExtDbCursor(
  "warehouse",
  "select sku, qty from stock where updated_at >= ? and warehouse_id = ?",
  "2026-01-01", 3
)
if code == 0 then
  local chunk, e, c = nextChunk()
  print(c, e, chunk and #chunk or 0)
end

-- Значения всех результирующих переменных
print("nextChunk:", nextChunk)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StrContains"></a>
## StrContains

**Категория:** Строки и утилиты

Проверяет наличие подстроки.

### Сигнатура

```lua
result = StrContains(s1, s2)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |
| 2 | s2 | string | Вторая строка / искомое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | boolean | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StrContains("demo", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StrContains("example", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StrReplace"></a>
## StrReplace

**Категория:** Строки и утилиты

Заменяет подстроку заданное число раз; -1 означает заменить все вхождения.

### Сигнатура

```lua
result = StrReplace(s1, s2, s3, n)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |
| 2 | s2 | string | Вторая строка / искомое значение. |
| 3 | s3 | string | Строка-замена. |
| 4 | n | number | N |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StrReplace("demo", "demo", "demo", 1)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StrReplace("example", "example", "example", 2)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StrToLower"></a>
## StrToLower

**Категория:** Строки и утилиты

Переводит строку в нижний регистр.

### Сигнатура

```lua
result = StrToLower(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StrToLower("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StrToLower("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StrToUpper"></a>
## StrToUpper

**Категория:** Строки и утилиты

Переводит строку в верхний регистр.

### Сигнатура

```lua
result = StrToUpper(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StrToUpper("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StrToUpper("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StrTrimSpace"></a>
## StrTrimSpace

**Категория:** Строки и утилиты

Удаляет пробелы по краям строки.

### Сигнатура

```lua
result = StrTrimSpace(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StrTrimSpace("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StrTrimSpace("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StringToJson"></a>
## StringToJson

**Категория:** Форматы и кодирование

Разбирает JSON-строку в Lua-таблицу; при ошибке возвращает пустую таблицу.

### Сигнатура

```lua
data = StringToJson(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | data | table | Результат функции. |

### Примеры

#### Пример 1

```lua
local data = StringToJson("demo")
print(data)

-- Значения всех результирующих переменных
if type(data) == "table" then
  print("data:", JsonToString(data))
else
  print("data:", data)
end
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local data = StringToJson("example")
print(data)

-- Значения всех результирующих переменных
if type(data) == "table" then
  print("data:", JsonToString(data))
else
  print("data:", data)
end
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="StripTags"></a>
## StripTags

**Категория:** Строки и утилиты

Удаляет HTML-теги и заменяет &nbsp; на пробел.

### Сигнатура

```lua
result = StripTags(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = StripTags("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = StripTags("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TelegramNewDocumentShare"></a>
## TelegramNewDocumentShare

**Категория:** Почта и сообщения

Отправляет существующий Telegram file_id как документ в чат.

### Сигнатура

```lua
result = TelegramNewDocumentShare(token, chatId, fileId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | token | string | JWT |
| 2 | chatId | number | Telegram chat ID. |
| 3 | fileId | string | Идентификатор файла |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = TelegramNewDocumentShare("eyJ...", 1, "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = TelegramNewDocumentShare("eyJ...", 2, "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TelegramNewMessage"></a>
## TelegramNewMessage

**Категория:** Почта и сообщения

Отправляет Telegram-сообщение и возвращает message_id.

### Сигнатура

```lua
result = TelegramNewMessage(token, chatId, MessageText, MessageId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | token | string | JWT |
| 2 | chatId | number | Telegram chat ID. |
| 3 | MessageText | string | Текст Telegram-сообщения. |
| 4 | MessageId | number | ID сообщения, на которое нужно ответить; 0 — без reply. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = TelegramNewMessage("eyJ...", 1, "Hello from Lua", 1)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = TelegramNewMessage("eyJ...", 2, "Hello from Lua", 2)
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TempDir"></a>
## TempDir

**Категория:** Файлы и S3

Возвращает системный временный каталог.

### Сигнатура

```lua
dir = TempDir()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | dir | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local dir = TempDir()
print(dir)

-- Значения всех результирующих переменных
print("dir:", dir)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local dir = TempDir()
print(dir)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("dir:", dir)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TempFile"></a>
## TempFile

**Категория:** Файлы и S3

Создаёт временный файл с указанным расширением/суффиксом и возвращает путь.

### Сигнатура

```lua
path, err, code = TempFile(ext)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | ext | string | Расширение/суффикс временного файла. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | path | string | Путь созданного временного файла. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local path, err, code = TempFile(".txt")
if code == 0 then print("temp:", path) else print(err) end

-- Значения всех результирующих переменных
print("path:", path)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local path, err, code = TempFile(".json")
if code == 0 then
  local writeErr, writeCode = WriteFile(path, "{\"ok\":true}")
  print(path, writeCode, writeErr)
else print(err) end

-- Значения всех результирующих переменных
print("path:", path)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="VertialTextToPNG"></a>
## VertialTextToPNG

**Категория:** Файлы и S3

Рисует вертикальный текст в PNG по параметрам text/font/outfile.

### Сигнатура

```lua
err, code = VertialTextToPNG(arr)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | arr | table | Lua-таблица данных/параметров. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = VertialTextToPNG({
  text = "CONFIDENTIAL",
  font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
  outfile = "/tmp/confidential.png"
})
if code ~= 0 then print(err) else print("PNG created") end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = VertialTextToPNG({
  text = "DamuBPM 2026",
  font = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
  outfile = "/tmp/damubpm-vertical.png"
})
print(code, err)

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TimeParseFormat"></a>
## TimeParseFormat

**Категория:** Строки и утилиты

Разбирает дату по input layout и форматирует в output layout.

### Сигнатура

```lua
result = TimeParseFormat(input, inputLayout, outputLayout)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | input | string | Входная Lua-таблица/данные. |
| 2 | inputLayout | string | Go time layout входной даты. |
| 3 | outputLayout | string | Go time layout результирующей даты. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = TimeParseFormat({value=42, name="demo"}, "demo", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = TimeParseFormat({value=42, name="demo"}, "example", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="TimeParseUnix"></a>
## TimeParseUnix

**Категория:** Строки и утилиты

Разбирает дату по layout и возвращает Unix time.

### Сигнатура

```lua
result = TimeParseUnix(input, inputLayout)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | input | string | Входная Lua-таблица/данные. |
| 2 | inputLayout | string | Go time layout входной даты. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | integer | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = TimeParseUnix({value=42, name="demo"}, "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = TimeParseUnix({value=42, name="demo"}, "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ToCP1048"></a>
## ToCP1048

**Категория:** Форматы и кодирование

Кодирует строку в CP1048.

### Сигнатура

```lua
result, err, code = ToCP1048(s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Байты в CP1048. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = ToCP1048("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = ToCP1048("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ToLower"></a>
## ToLower

**Категория:** Строки и утилиты

Переводит строку в нижний регистр.

### Сигнатура

```lua
result = ToLower(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = ToLower("demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = ToLower("example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="UUID"></a>
## UUID

**Категория:** Система и выполнение

Генерирует новый UUID.

### Сигнатура

```lua
uuid = UUID()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | uuid | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local uuid = UUID()
print(uuid)

-- Значения всех результирующих переменных
print("uuid:", uuid)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local uuid = UUID()
print(uuid)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("uuid:", uuid)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="UUIDFromString"></a>
## UUIDFromString

**Категория:** Система и выполнение

Нормализует/преобразует строку в UUID-представление.

### Сигнатура

```lua
uuid = UUIDFromString(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | uuid | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local uuid = UUIDFromString("demo")
print(uuid)

-- Значения всех результирующих переменных
print("uuid:", uuid)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local uuid = UUIDFromString("example")
print(uuid)

-- Значения всех результирующих переменных
print("uuid:", uuid)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="UpdateRawData"></a>
## UpdateRawData

**Категория:** Файлы и S3

Перезаписывает содержимое существующего файла в хранилище.

### Сигнатура

```lua
err, code = UpdateRawData(file_id, dataStr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | file_id | integer | Идентификатор файла |
| 2 | dataStr | string | Строковые либо бинарные данные файла. |
| 3 | userId | integer | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = UpdateRawData(1, "demo", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = UpdateRawData(2, "example", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="UploadRawData"></a>
## UploadRawData

**Категория:** Файлы и S3

Загружает строковые/бинарные данные в файловое хранилище и возвращает UUID файла.

### Сигнатура

```lua
fileUuid, err, code = UploadRawData(dir, fileName, dataStr, userId)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | dir | string | Каталог файлового хранилища |
| 2 | fileName | string | Имя или путь файла. |
| 3 | dataStr | string | Строковые либо бинарные данные файла. |
| 4 | userId | integer | Идентификатор пользователя |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileUuid | string | UUID загруженного файла. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local fileUuid, err, code = UploadRawData("documents/qr", "/tmp/demo.txt", "demo", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", fileUuid)
end

-- Значения всех результирующих переменных
print("fileUuid:", fileUuid)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local fileUuid, err, code = UploadRawData("documents/qr", "/tmp/demo.txt", "example", 101)
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", fileUuid)
end

-- Значения всех результирующих переменных
print("fileUuid:", fileUuid)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="Version"></a>
## Version

**Категория:** Система и выполнение

Возвращает версию DamuBPM.

### Сигнатура

```lua
result = Version()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = Version()
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = Version()
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GoVersion"></a>
## GoVersion

**Категория:** Система и выполнение

Возвращает версию Go runtime.

### Сигнатура

```lua
result = GoVersion()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = GoVersion()
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = GoVersion()
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="VersionNum"></a>
## VersionNum

**Категория:** Система и выполнение

Возвращает числовую версию приложения.

### Сигнатура

```lua
result = VersionNum()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | any | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = VersionNum()
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = VersionNum()
print(result)
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="WriteFile"></a>
## WriteFile

**Категория:** Файлы и S3

Записывает строку в файл.

### Сигнатура

```lua
err, code = WriteFile(fileName, s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |
| 2 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = WriteFile("/tmp/demo.txt", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = WriteFile("/tmp/demo.txt", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="WriteFile2"></a>
## WriteFile2

**Категория:** Файлы и S3

Записывает строку/данные в файл альтернативным вариантом реализации.

### Сигнатура

```lua
err, code = WriteFile2(fileName, s)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | fileName | string | Имя или путь файла. |
| 2 | s | string | Строка или строковые/бинарные данные. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 2 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local err, code = WriteFile2("/tmp/demo.txt", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local err, code = WriteFile2("/tmp/demo.txt", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok")
end

-- Значения всех результирующих переменных
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="WriteLog"></a>
## WriteLog

**Категория:** Прочее

Пишет строку в серверный лог. В примерах справочника вместо этой функции используется стандартный print.

### Сигнатура

```lua
WriteLog(str)
```

> **Примечание:** Примечание: функция существует в API, но во всех примерах этого справочника для вывода используется стандартный print , как рекомендовано.

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Явных возвращаемых значений нет. |  |  |  |

### Примеры

#### Пример 1

```lua
-- Для логирования в примерах используйте стандартный Lua print
print("Process started")

-- Функция не возвращает значений.
```

#### Пример 2

```lua
print("order_id=", 1001, "state=", "NEW")

-- Функция не возвращает значений.
```

[↑ К оглавлению](#оглавление)

---

<a id="XmlPathParse"></a>
## XmlPathParse

**Категория:** Форматы и кодирование

Извлекает строковое значение из XML по XML path.

### Сигнатура

```lua
result = XmlPathParse(path, xml)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | path | string | Путь или шаблон пути |
| 2 | xml | string | XML-документ. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = XmlPathParse("/tmp/demo.txt", "demo")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = XmlPathParse("/tmp/demo.txt", "example")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="XmltoJSONString"></a>
## XmltoJSONString

**Категория:** Форматы и кодирование

Преобразует XML в JSON-строку.

### Сигнатура

```lua
json, err, code = XmltoJSONString(s1)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | s1 | string | Первая строка / основное входное значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | json | string | JSON-строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local json, err, code = XmltoJSONString("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", json)
end

-- Значения всех результирующих переменных
print("json:", json)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local json, err, code = XmltoJSONString("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", json)
end

-- Значения всех результирующих переменных
print("json:", json)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GunZipString"></a>
## GunZipString

**Категория:** Форматы и кодирование

Распаковывает gzip-строку.

### Сигнатура

```lua
result, err, code = GunZipString(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Распакованная строка. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = GunZipString("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = GunZipString("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="GZipString"></a>
## GZipString

**Категория:** Форматы и кодирование

Упаковывает строку в gzip с именем, комментарием и временем.

### Сигнатура

```lua
result, err, code = GZipString(name, comment, timestr, str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | name | string | Имя ресурса/producer-а. |
| 2 | comment | string | GZip header Comment. |
| 3 | timestr | string | Дата/время для GZip header. |
| 4 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Gzip-байты в строке. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = GZipString("demo", "demo", "demo", "demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = GZipString("example", "example", "example", "example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="ZipString"></a>
## ZipString

**Категория:** Форматы и кодирование

Упаковывает строку в ZIP-архив с одним файлом.

### Сигнатура

```lua
result, err, code = ZipString(str)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | str | string | Строковое значение. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | ZIP-байты в строке. |
| 2 | err | string | Пустая строка при успехе; текст ошибки при неуспехе. |
| 3 | code | integer | 0 при успехе; ненулевое значение — код ошибки/состояния. |

### Примеры

#### Пример 1

```lua
local result, err, code = ZipString("demo")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result, err, code = ZipString("example")
if code ~= 0 then
  print("error:", err, "code:", code)
else
  print("ok:", result)
end

-- Значения всех результирующих переменных
print("result:", result)
print("err:", err)
print("code:", code)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="beBe"></a>
## beBe

**Категория:** Прочее

Тестовая служебная функция; текущая реализация не возвращает значение в Lua.

### Сигнатура

```lua
beBe()
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Параметры не требуются. |  |  |  |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| Явных возвращаемых значений нет. |  |  |  |

### Примеры

#### Пример 1

```lua
beBe()
print("done")

-- Функция не возвращает значений.
```

#### Пример 2

```lua
beBe()
print("done")
-- Второй сценарий: тот же вызов можно использовать в составе проверки/периодической задачи.

-- Функция не возвращает значений.
```

[↑ К оглавлению](#оглавление)

---

<a id="httpGet"></a>
## httpGet

**Категория:** HTTP / WebSocket

Простой HTTP GET, возвращающий тело ответа или пустую строку при ошибке.

### Сигнатура

```lua
result = httpGet(url)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = httpGet("https://example.com/api")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = httpGet("https://example.com/health")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="httpPost"></a>
## httpPost

**Категория:** HTTP / WebSocket

Простой HTTP POST с content-type и телом.

### Сигнатура

```lua
result = httpPost(url, contentType, body)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | contentType | string | MIME Content-Type |
| 3 | body | string | Тело сообщения/запроса |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = httpPost("https://example.com/api", "text/plain", "Hello from Lua")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = httpPost("https://example.com/health", "text/plain", "Hello from Lua")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="httpPost2"></a>
## httpPost2

**Категория:** HTTP / WebSocket

HTTP POST с произвольными заголовками.

### Сигнатура

```lua
result = httpPost2(url, headers, body)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | headers | table | Lua-таблица HTTP-заголовков key=value |
| 3 | body | string | Тело сообщения/запроса |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = httpPost2("https://example.com/api", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, "Hello from Lua")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = httpPost2("https://example.com/health", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, "Hello from Lua")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)

---

<a id="httpPost2WithProxy"></a>
## httpPost2WithProxy

**Категория:** HTTP / WebSocket

HTTP POST с произвольными заголовками через указанный proxy.

### Сигнатура

```lua
result = httpPost2WithProxy(url, headers, body, proxyUrl)
```

### Входящие параметры

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | url | string | URL запроса. |
| 2 | headers | table | Lua-таблица HTTP-заголовков key=value |
| 3 | body | string | Тело сообщения/запроса |
| 4 | proxyUrl | string | URL proxy |

### Результирующие параметры (возвращаемые переменные)

| # | Параметр | Тип | Описание |
| --- | --- | --- | --- |
| 1 | result | string | Результат функции. |

### Примеры

#### Пример 1

```lua
local result = httpPost2WithProxy("https://example.com/api", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, "Hello from Lua", "http://127.0.0.1:3128")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

#### Пример 2

```lua
local result = httpPost2WithProxy("https://example.com/health", {["Accept"]="application/json", ["X-Request-ID"]="demo-1"}, "Hello from Lua", "http://127.0.0.1:3128")
print(result)

-- Значения всех результирующих переменных
print("result:", result)
-- /Значения всех результирующих переменных
```

[↑ К оглавлению](#оглавление)
