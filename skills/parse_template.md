# ParseTemplate — Lua справочник

[← На главную](index.html)

Практический справочник по формированию текста, HTML, документов и динамических фрагментов из Lua-скриптов с помощью `ParseTemplate`.

## Содержание

- [Быстрый старт](#быстрый-старт)
- [Сигнатура](#сигнатура)
- [Результат и ошибки](#результат-и-ошибки)
- [Синтаксис шаблона](#синтаксис-шаблона)
- [Функции внутри шаблона](#функции-внутри-шаблона)
- [Шаблонные Lua-функции](#шаблонные-lua-функции)
- [Важные нюансы](#важные-нюансы)
- [70 примеров](#70-примеров)

## Быстрый старт

```lua
local template = "Привет, {{.name}}!"
local data = { name = "Ельдар" }

local result, errText, errNum = ParseTemplate(
    template,
    data,
    tostring(userId)
)

if errNum ~= 0 then
    return nil, errText, errNum
end

print(result)
```

## Сигнатура

```lua
result, errText, errNum = ParseTemplate(templateText, dataTable, userIdString)
```

| Аргумент | Что передавать | Пример |
|---|---|---|
| `templateText` | Строка с шаблоном `{{...}}` | `"Привет, {{.name}}"` |
| `dataTable` | Lua-таблица с данными | `{ name = "Ельдар" }` |
| `userIdString` | Строка, содержащая целое число | `tostring(userId)` |

> Рекомендуется всегда приводить `userId` через `tostring()` и проверять `errNum` перед использованием результата.

## Результат и ошибки

| `errNum` | Смысл | Что делать |
|---:|---|---|
| `0` | Шаблон успешно сформирован | Используйте `result`; `errText` пустой. |
| `1` | Ошибка преобразования `userId` либо ошибка разбора/выполнения шаблона | Логируйте `errText`, результат не используйте. |
| `2` | Некорректный тип входного аргумента или ошибка преобразования Lua-таблицы | Проверьте: 1-й аргумент строка, 2-й таблица, 3-й строка. |

## Синтаксис шаблона

### Поле

```text
{{.name}}
```

### Вложенное поле

```text
{{.client.name}}
```

### Условие

```text
{{if .active}}Активен{{else}}Заблокирован{{end}}
```

### Перебор

```text
{{range .items}}
  {{.title}}
{{end}}
```

### Вызов функции

```text
{{formatNumber .amount}}
```

## Функции внутри шаблона

| Функция | Назначение |
|---|---|
| `sum a b` | Сложение значений как чисел с плавающей точкой. |
| `inc a b` | Целочисленное сложение. |
| `eq a b` | Сравнение строковых представлений значений. |
| `neq a b` | Проверка неравенства строковых представлений. |
| `gt a b` | Числовое сравнение «больше». |
| `contains a b` | Проверка наличия подстроки. |
| `HasPrefix a b` | Проверка префикса строки. |
| `isnil value` | Считает пустыми nil, пустую строку и строку <nil>. |
| `ifnil a b` | Возвращает b только если a == nil. |
| `title value` | Преобразование строки к заголовочному виду. |
| `InterfaceToInt value` | Преобразование значения в целое число. |
| `InterfaceToJsonString value` | Сериализация значения в JSON. |
| `formatNumber value` | Форматирование числа с разделителями; безопаснее передавать строку. |
| `StrTrimSpace value` | Удаление пробелов по краям. |
| `StrReplace value old new count` | Замена подстрок. |
| `HTMLEscapeString value` | HTML-экранирование. |
| `QueryEscape value` | URL query escaping. |
| `StripTags value` | Удаление HTML-тегов. |
| `Base64Encode value` | Кодирование Base64. |
| `Base64Decode value` | Декодирование Base64. |
| `QRCodeBase64 value level size` | Генерация PNG QR-кода в Base64. |
| `DBCurrentDateTime` | Текущие дата и время. |
| `TimeParseFormat value inputFormat outputFormat` | Преобразование формата даты/времени. |
| `TimeParseUnix value inputFormat` | Преобразование даты во временную метку Unix. |
| `Hostname` | Имя текущего узла. |
| `Getenv name` | Чтение переменной окружения. |
| `UUID` | Генерация UUID. |
| `Version` | Текстовая версия приложения. |
| `VersionNum` | Числовая версия приложения. |
| `Iterate from to` | Создание диапазона строк от from до to включительно. |
| `ruNum2Word value` | Число прописью на русском. |
| `kkNum2Word value` | Число прописью на казахском. |
| `getParamValue code / GetParamValue code` | Получение системного параметра. |
| `getUserParamValue code / GetUserParamValue code` | Получение параметра пользователя, чей userId передан в ParseTemplate. |
| `parseTemplate template data / ParseTemplate template data` | Вложенная обработка шаблона с тем же userId. |
| `lua code args...` | Вызов script из template_funcs; аргументы доступны как argv1, argv2, ... |
| `lua2 code p1 p2` | Вызов script с param1 и param2. |
| `lua3 code p1 p2 p3` | Вызов script с param1..param3. |
| `lua4 code p1 p2 p3 p4` | Вызов script с param1..param4. |
| `lua5 code p1 p2 p3 p4 p5` | Вызов script с param1..param5. |
| `EntityValueById a b c` | Получение значения сущности по трём аргументам; точная семантика определяется реализацией проекта. |
| `EntityValueByCode a b c` | Получение значения сущности по трём аргументам; точная семантика определяется реализацией проекта. |
| `EntityValueByUUID a b c` | Получение значения сущности по трём аргументам; точная семантика определяется реализацией проекта. |
| `HTMLToFODTStyle value` | Преобразование HTML-стилей для FODT. |
| `HTMLToFODTContent value` | Преобразование HTML-содержимого для FODT. |

## Шаблонные Lua-функции

Перед обработкой шаблона доступны скрипты из `template_funcs`, где используется соответствие `code → script`.

### `lua`

```text
{{lua "make_label" .code .title .status}}
```

В вызываемом script аргументы доступны как:

```lua
argv1
argv2
argv3
```

Пример содержимого script:

```lua
local code = tostring(argv1 or "")
local title = tostring(argv2 or "")
return "[" .. code .. "] " .. title
```

### `lua2` … `lua5`

```text
{{lua2 "concat2" .first .second}}
{{lua3 "format_person" .surname .name .middleName}}
{{lua4 "make_address" .city .street .house .flat}}
{{lua5 "build_code" .a .b .c .d .e}}
```

Для этих функций используются глобальные `param1`, `param2`, … `param5`. Script должен вернуть значение.

## Важные нюансы

1. **`userId` передавайте строкой.** Наиболее безопасный вариант — `tostring(userId)`.
2. **`formatNumber` лучше кормить строкой.** Например: `"1250000.50"`.
3. **`isnil` и `ifnil` работают по-разному.** `isnil` считает пустыми `nil`, `""` и `"<nil>"`; `ifnil` делает fallback только для настоящего `nil`.
4. **`gt` выполняет числовое сравнение.** Передавайте числовые строки без валютных символов и лишних пробелов.
5. **`lua` и `lua2…lua5` вызывают script из `template_funcs`.** `lua` использует `argv1…`, остальные — `param1…param5`.
6. **Вложенный `parseTemplate` наследует текущий `userId`.** Это удобно для переиспользуемых карточек, строк таблиц и блоков документов.
7. **`EntityValueById`, `EntityValueByCode`, `EntityValueByUUID` принимают по три аргумента.** Точная семантика этих аргументов определяется реализацией проекта, поэтому не следует считать примерный порядок аргументов универсальным.
8. **`QRCodeBase64 value level size`:** уровни `0/1/2/3` соответствуют Low/Medium/High/Highest; `size = 0` считается ошибочным и возвращает пустой результат.

### Рекомендуемая безопасная обертка

```lua
local function render(template, data, userId)
    local result, errText, errNum = ParseTemplate(
        template,
        data or {},
        tostring(userId)
    )

    if errNum ~= 0 then
        return nil, "ParseTemplate: " .. tostring(errText), errNum
    end

    return result, "", 0
end
```

## 70 примеров

### Основы

#### #01 — Минимальный вызов

```lua
local template = "Привет, {{.name}}!"
local data = { name = "Ельдар" }
local result, errText, errNum = ParseTemplate(template, data, "100")

if errNum == 0 then
    print(result)
else
    print(errNum, errText)
end
```

**Пояснение:** Привет, Ельдар!

#### #02 — userId из переменной

```lua
local userId = 125
local result, errText, errNum = ParseTemplate(
    "Пользователь: {{.name}}",
    { name = "Администратор" },
    tostring(userId)
)
```

**Пояснение:** Третий аргумент передавайте строкой с числовым идентификатором.

#### #03 — Несколько полей

```lua
local template = [[
ФИО: {{.fio}}
Email: {{.email}}
Телефон: {{.phone}}
]]
local data = {
    fio = "Иванов Иван",
    email = "ivanov@example.com",
    phone = "+7 700 000 00 00"
}
local result, errText, errNum = ParseTemplate(template, data, "100")
```

**Пояснение:** Подстановка нескольких ключей верхнего уровня.

#### #04 — Вложенные данные

```lua
local template = [[
Клиент: {{.client.name}}
Город: {{.client.city}}
]]
local data = {
    client = {
        name = "ТОО Альфа",
        city = "Алматы"
    }
}
local result, errText, errNum = ParseTemplate(template, data, "100")
```

**Пояснение:** Доступ к вложенным полям через точку.

#### #05 — Многострочный HTML

```lua
local template = [[
<div class="card">
  <h3>{{.title}}</h3>
  <p>{{.text}}</p>
</div>
]]
local data = { title = "Уведомление", text = "Заявка принята" }
local htmlText, errText, errNum = ParseTemplate(template, data, "100")
```

**Пояснение:** Функция возвращает обычную строку, поэтому ею удобно собирать HTML.

#### #06 — Обработка ошибки

```lua
local result, errText, errNum = ParseTemplate(
    "{{if .active}}Активен{{end}}",
    { active = true },
    "100"
)

if errNum ~= 0 then
    return nil, errText, errNum
end
return result, "", 0
```

**Пояснение:** Удобный паттерн для сервисов и бизнес-логики.

#### #07 — Неверный userId

```lua
local result, errText, errNum = ParseTemplate(
    "{{.name}}",
    { name = "Test" },
    "abc"
)

print(result)   -- nil
print(errText)  -- текст ошибки преобразования
print(errNum)   -- 1
```

**Пояснение:** userId должен преобразовываться в целое число.

#### #08 — Пустая таблица данных

```lua
local result, errText, errNum = ParseTemplate(
    "Статический текст без переменных",
    {},
    "100"
)
```

**Пояснение:** Таблица данных обязательна как второй аргумент, даже если поля не используются.

### Условия

#### #09 — Условие if

```lua
local template = [[{{if .active}}Пользователь активен{{else}}Пользователь заблокирован{{end}}]]
local result = ParseTemplate(template, { active = true }, "100")
```

**Пояснение:** Базовая развилка по значению.

#### #10 — Сравнение eq

```lua
local template = [[{{if eq .status "done"}}Выполнено{{else}}В работе{{end}}]]
local result = ParseTemplate(template, { status = "done" }, "100")
```

**Пояснение:** eq сравнивает строковые представления значений.

#### #11 — Сравнение neq

```lua
local template = [[{{if neq .status "deleted"}}Показывать запись{{end}}]]
local result = ParseTemplate(template, { status = "active" }, "100")
```

**Пояснение:** neq — противоположность eq.

#### #12 — Числовое сравнение gt

```lua
local template = [[{{if gt .amount "100000"}}Крупная сумма{{else}}Обычная сумма{{end}}]]
local result = ParseTemplate(template, { amount = "125000.50" }, "100")
```

**Пояснение:** gt преобразует оба значения в числа с плавающей точкой.

#### #13 — contains

```lua
local template = [[{{if contains .email "@bapps.kz"}}Корпоративный адрес{{else}}Внешний адрес{{end}}]]
local result = ParseTemplate(template, { email = "user@bapps.kz" }, "100")
```

**Пояснение:** Проверка наличия подстроки.

#### #14 — HasPrefix

```lua
local template = [[{{if HasPrefix .code "REQ_"}}Это заявка{{end}}]]
local result = ParseTemplate(template, { code = "REQ_2026_001" }, "100")
```

**Пояснение:** Проверка начала строки.

#### #15 — isnil

```lua
local template = [[{{if isnil .comment}}Комментарий не заполнен{{else}}{{.comment}}{{end}}]]
local result = ParseTemplate(template, { comment = "" }, "100")
```

**Пояснение:** isnil считает пустыми nil, пустую строку и строку <nil>.

#### #16 — ifnil

```lua
local template = [[Ответственный: {{ifnil .owner "Не назначен"}}]]
local result = ParseTemplate(template, { owner = nil }, "100")
```

**Пояснение:** ifnil подставляет запасное значение только когда исходное значение nil.

#### #17 — Комбинация условий

```lua
local template = [[
{{if eq .type "invoice"}}
  {{if gt .amount "1000000"}}Счет требует дополнительного контроля{{else}}Обычный счет{{end}}
{{else}}
  Документ другого типа
{{end}}
]]
local result = ParseTemplate(template, { type = "invoice", amount = "1500000" }, "100")
```

**Пояснение:** Условия можно вкладывать.

### Коллекции

#### #18 — range по списку

```lua
local template = [[
{{range .items}}- {{.name}}: {{.amount}}
{{end}}
]]
local data = {
    items = {
        { name = "Услуга 1", amount = "1000" },
        { name = "Услуга 2", amount = "2500" },
        { name = "Услуга 3", amount = "500" }
    }
}
local result = ParseTemplate(template, data, "100")
```

**Пояснение:** Типичный вывод набора строк.

#### #19 — range с else

```lua
local template = [[
{{range .items}}<li>{{.title}}</li>{{else}}<li>Нет данных</li>{{end}}
]]
local result = ParseTemplate(template, { items = {} }, "100")
```

**Пояснение:** Ветка else срабатывает для пустой коллекции.

#### #20 — range по простым значениям

```lua
local template = [[{{range .tags}}#{{.}} {{end}}]]
local result = ParseTemplate(template, {
    tags = { "bpm", "lua", "api" }
}, "100")
```

**Пояснение:** Точка внутри range указывает на текущий элемент.

#### #21 — Таблица HTML

```lua
local template = [[
<table>
<tr><th>№</th><th>Наименование</th><th>Сумма</th></tr>
{{range .rows}}
<tr><td>{{.n}}</td><td>{{.title}}</td><td>{{formatNumber .amount}}</td></tr>
{{end}}
</table>
]]
local data = { rows = {
    { n = 1, title = "Работы", amount = "1250000.50" },
    { n = 2, title = "Материалы", amount = "230000.00" }
}}
local result = ParseTemplate(template, data, "100")
```

**Пояснение:** Практический отчет с форматированием сумм.

#### #22 — Iterate 1..5

```lua
local template = [[{{range Iterate 1 5}}Шаг {{.}}
{{end}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Iterate создает список строк от первого числа до второго включительно.

#### #23 — Iterate для ячеек

```lua
local template = [[<tr>{{range Iterate 1 6}}<td>Колонка {{.}}</td>{{end}}</tr>]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Удобно для фиксированного количества повторов.

### Числа и строки

#### #24 — sum

```lua
local template = [[Итого: {{sum .amount .tax}}]]
local result = ParseTemplate(template, {
    amount = "1000.50",
    tax = "120.25"
}, "100")
```

**Пояснение:** sum приводит значения к числу и складывает их.

#### #25 — inc

```lua
local template = [[Следующий номер: {{inc .number 1}}]]
local result = ParseTemplate(template, { number = "41" }, "100")
```

**Пояснение:** inc работает как целочисленное сложение.

#### #26 — InterfaceToInt

```lua
local template = [[Количество: {{InterfaceToInt .count}}]]
local result = ParseTemplate(template, { count = "15" }, "100")
```

**Пояснение:** Явное преобразование значения к целому числу.

#### #27 — formatNumber

```lua
local template = [[Сумма: {{formatNumber .amount}} ₸]]
local result = ParseTemplate(template, { amount = "1234567.89" }, "100")
```

**Пояснение:** Передавайте значение строкой. Результат форматируется с разделителем тысяч и двумя знаками.

#### #28 — title

```lua
local template = [[{{title .text}}]]
local result = ParseTemplate(template, { text = "hello world" }, "100")
```

**Пояснение:** Преобразование регистра заголовка.

#### #29 — StrTrimSpace

```lua
local template = [[>{{StrTrimSpace .value}}<]]
local result = ParseTemplate(template, { value = "   текст   " }, "100")
```

**Пояснение:** Удаляет пробелы по краям.

#### #30 — StrReplace

```lua
local template = [[{{StrReplace .phone " " "" -1}}]]
local result = ParseTemplate(template, { phone = "+7 700 123 45 67" }, "100")
```

**Пояснение:** Четвертый аргумент задает число замен; -1 означает заменить все вхождения.

#### #31 — ruNum2Word

```lua
local template = [[{{ruNum2Word .amount}}]]
local result = ParseTemplate(template, { amount = "1250" }, "100")
```

**Пояснение:** Преобразование числа в слова на русском; точное оформление определяется реализацией функции.

#### #32 — kkNum2Word

```lua
local template = [[{{kkNum2Word .amount}}]]
local result = ParseTemplate(template, { amount = "1250" }, "100")
```

**Пояснение:** Преобразование числа в слова на казахском; точное оформление определяется реализацией функции.

#### #33 — InterfaceToJsonString

```lua
local template = [[Данные JSON: {{InterfaceToJsonString .payload}}]]
local result = ParseTemplate(template, {
    payload = { id = 10, status = "new" }
}, "100")
```

**Пояснение:** Сериализация переданного значения в JSON-строку.

### HTML и кодирование

#### #34 — HTMLEscapeString

```lua
local template = [[<div>{{HTMLEscapeString .unsafe}}</div>]]
local result = ParseTemplate(template, {
    unsafe = [[<script>alert("x")</script>]]
}, "100")
```

**Пояснение:** Экранирует специальные HTML-символы.

#### #35 — QueryEscape

```lua
local template = [[/search?q={{QueryEscape .query}}]]
local result = ParseTemplate(template, { query = "бизнес процесс & BPM" }, "100")
```

**Пояснение:** Подготовка значения для query-параметра URL.

#### #36 — StripTags

```lua
local template = [[{{StripTags .html}}]]
local result = ParseTemplate(template, {
    html = "<p>Привет <b>мир</b>&nbsp;!</p>"
}, "100")
```

**Пояснение:** Удаляет HTML-теги и заменяет &nbsp; на обычный пробел.

#### #37 — Base64Encode

```lua
local template = [[{{Base64Encode .text}}]]
local result = ParseTemplate(template, { text = "DamuBPM" }, "100")
```

**Пояснение:** Кодирование строки в Base64.

#### #38 — Base64Decode

```lua
local template = [[{{Base64Decode .encoded}}]]
local result = ParseTemplate(template, { encoded = "RGFtdUJQTQ==" }, "100")
```

**Пояснение:** Декодирование Base64; при ошибке возвращается пустая строка.

#### #39 — QRCodeBase64

```lua
local template = [[
<img alt="QR" src="data:image/png;base64,{{QRCodeBase64 .url 1 256}}">
]]
local result = ParseTemplate(template, {
    url = "https://example.com/document/123"
}, "100")
```

**Пояснение:** Уровень: 0 Low, 1 Medium, 2 High, 3 Highest. Размер не должен быть 0.

#### #40 — HTMLToFODTStyle

```lua
local template = [[{{HTMLToFODTStyle .html}}]]
local result = ParseTemplate(template, { html = "<p><b>Текст</b></p>" }, "100")
```

**Пояснение:** Преобразование HTML в стилевое представление FODT; детали зависят от внутренней функции.

#### #41 — HTMLToFODTContent

```lua
local template = [[{{HTMLToFODTContent .html}}]]
local result = ParseTemplate(template, { html = "<p>Документ</p>" }, "100")
```

**Пояснение:** Преобразование HTML-контента для FODT.

### Дата и окружение

#### #42 — DBCurrentDateTime

```lua
local template = [[Сформировано: {{DBCurrentDateTime}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Возвращает текущие дату и время в формате YYYY-MM-DD HH:MM:SS.

#### #43 — TimeParseFormat

```lua
local template = [[{{TimeParseFormat .date "2006-01-02" "02.01.2006"}}]]
local result = ParseTemplate(template, { date = "2026-09-06" }, "100")
```

**Пояснение:** Первый аргумент — дата, второй — входной формат, третий — выходной формат.

#### #44 — TimeParseUnix

```lua
local template = [[Unix: {{TimeParseUnix .date "2006-01-02 15:04:05"}}]]
local result = ParseTemplate(template, { date = "2026-09-06 23:30:00" }, "100")
```

**Пояснение:** Преобразует дату по заданному формату в Unix timestamp.

#### #45 — Hostname

```lua
local template = [[Сервер: {{Hostname}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Возвращает hostname текущего узла.

#### #46 — Getenv

```lua
local template = [[Среда: {{Getenv "DAMU_ENV"}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Чтение переменной окружения.

#### #47 — UUID

```lua
local template = [[ID документа: {{UUID}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Генерирует новый UUID.

#### #48 — Version

```lua
local template = [[Версия: {{Version}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Текстовое значение версии приложения.

#### #49 — VersionNum

```lua
local template = [[Номер версии: {{VersionNum}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Числовое значение версии приложения.

### Параметры

#### #50 — getParamValue

```lua
local template = [[Название системы: {{getParamValue "system_name"}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Чтение системного параметра по коду.

#### #51 — GetParamValue

```lua
local template = [[Параметр: {{GetParamValue "system_name"}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Доступен и вариант имени с заглавной буквы.

#### #52 — getUserParamValue

```lua
local userId = 125
local template = [[Язык: {{getUserParamValue "language"}}]]
local result = ParseTemplate(template, {}, tostring(userId))
```

**Пояснение:** Читает параметр именно для userId, переданного третьим аргументом ParseTemplate.

#### #53 — GetUserParamValue

```lua
local result = ParseTemplate(
    [[Тема: {{GetUserParamValue "theme"}}]],
    {},
    "125"
)
```

**Пояснение:** Альтернативное имя той же операции.

### Вложенные шаблоны

#### #54 — Вложенный parseTemplate

```lua
local template = [[
Внешний шаблон.
Вложенный: {{parseTemplate .inner .data}}
]]
local data = {
    inner = "Привет, {{.name}}!",
    data = { name = "Ельдар" }
}
local result = ParseTemplate(template, data, "100")
```

**Пояснение:** Вложенный шаблон наследует текущий userId.

#### #55 — Вложенный ParseTemplate

```lua
local template = [[{{ParseTemplate .rowTemplate .row}}]]
local data = {
    rowTemplate = "{{.code}} — {{.title}}",
    row = { code = "A01", title = "Заявка" }
}
local result = ParseTemplate(template, data, "100")
```

**Пояснение:** Доступны оба варианта имени: ParseTemplate и parseTemplate.

#### #56 — Динамическая карточка

```lua
local template = [[
{{range .cards}}
  {{parseTemplate $.cardTemplate .}}
{{end}}
]]
local data = {
    cardTemplate = [[<div class="card"><b>{{.title}}</b><span>{{.value}}</span></div>]],
    cards = {
        { title = "Статус", value = "Активен" },
        { title = "Приоритет", value = "Высокий" }
    }
}
local result = ParseTemplate(template, data, "100")
```

**Пояснение:** Полезный паттерн повторного использования фрагментов.

### Шаблонные Lua-функции

#### #57 — lua без параметров

```lua
-- В template_funcs есть запись с code = "hello"
-- Ее script должен вернуть одно значение.
local template = [[Результат: {{lua "hello"}}]]
local result = ParseTemplate(template, {}, "100")
```

**Пояснение:** Функция lua ищет script по code в template_funcs и выполняет его.

#### #58 — lua с argv1

```lua
-- script с code = "upper_name" может использовать глобальную argv1
local template = [[{{lua "upper_name" .name}}]]
local result = ParseTemplate(template, { name = "Ельдар" }, "100")
```

**Пояснение:** Для lua параметры выставляются как argv1, argv2, ... перед выполнением script.

#### #59 — lua с несколькими argv

```lua
local template = [[{{lua "make_label" .code .title .status}}]]
local result = ParseTemplate(template, {
    code = "REQ-100",
    title = "Согласование",
    status = "new"
}, "100")
```

**Пояснение:** Количество параметров для lua не ограничено фиксированными lua2..lua5.

#### #60 — lua2

```lua
-- script с code = "concat2" использует param1 и param2
local template = [[{{lua2 "concat2" .first .second}}]]
local result = ParseTemplate(template, {
    first = "Damu",
    second = "BPM"
}, "100")
```

**Пояснение:** lua2 выставляет глобальные param1 и param2.

#### #61 — lua3

```lua
local template = [[{{lua3 "format_person" .surname .name .middleName}}]]
local result = ParseTemplate(template, {
    surname = "Иванов",
    name = "Иван",
    middleName = "Иванович"
}, "100")
```

**Пояснение:** lua3 передает param1..param3.

#### #62 — lua4

```lua
local template = [[{{lua4 "make_address" .city .street .house .flat}}]]
local result = ParseTemplate(template, {
    city = "Алматы", street = "Абая", house = "10", flat = "25"
}, "100")
```

**Пояснение:** lua4 передает param1..param4.

#### #63 — lua5

```lua
local template = [[{{lua5 "build_code" .a .b .c .d .e}}]]
local result = ParseTemplate(template, {
    a="A", b="B", c="C", d="D", e="E"
}, "100")
```

**Пояснение:** lua5 передает param1..param5.

#### #64 — Пример script для lua

```lua
-- Содержимое поля script для code = "make_label"
local code = tostring(argv1 or "")
local title = tostring(argv2 or "")
return "[" .. code .. "] " .. title
```

**Пояснение:** script должен вернуть значение, которое попадет в итоговый шаблон.

#### #65 — Пример script для lua2

```lua
-- Содержимое поля script для code = "concat2"
local a = tostring(param1 or "")
local b = tostring(param2 or "")
return a .. b
```

**Пояснение:** Для lua2 используются param1 и param2.

### Значения сущностей

#### #66 — EntityValueById

```lua
local template = [[{{EntityValueById .entity .id .attribute}}]]
local result = ParseTemplate(template, {
    entity = "customers",
    id = "123",
    attribute = "title"
}, "100")
```

**Пояснение:** Функция доступна с тремя аргументами. Точный смысл и порядок аргументов определяется реализацией EntityValueById в вашей сборке.

#### #67 — EntityValueByCode

```lua
local template = [[{{EntityValueByCode .entity .code .attribute}}]]
local result = ParseTemplate(template, {
    entity = "customers",
    code = "C-001",
    attribute = "title"
}, "100")
```

**Пояснение:** Функция принимает три аргумента; проверьте принятую в проекте семантику каждого аргумента.

#### #68 — EntityValueByUUID

```lua
local template = [[{{EntityValueByUUID .entity .uuid .attribute}}]]
local result = ParseTemplate(template, {
    entity = "customers",
    uuid = "00000000-0000-0000-0000-000000000001",
    attribute = "title"
}, "100")
```

**Пояснение:** Функция принимает три аргумента и возвращает строку.

### Практика

#### #69 — Комплексный документ

```lua
local template = [[
<h2>{{HTMLEscapeString .title}}</h2>
<p>Номер: {{.number}}</p>
<p>Дата: {{TimeParseFormat .date "2006-01-02" "02.01.2006"}}</p>
<p>Контрагент: {{ifnil .customer "Не указан"}}</p>
<table>
{{range .items}}
<tr>
  <td>{{.title}}</td>
  <td>{{formatNumber .amount}} ₸</td>
</tr>
{{end}}
</table>
<p><b>Итого: {{formatNumber .total}} ₸</b></p>
]]
local data = {
    title = "Счет на оплату",
    number = "INV-2026-001",
    date = "2026-09-06",
    customer = "ТОО Альфа",
    total = "1500000.00",
    items = {
        { title = "Услуги", amount = "1000000.00" },
        { title = "Поддержка", amount = "500000.00" }
    }
}
local result, errText, errNum = ParseTemplate(template, data, "100")
```

**Пояснение:** Большой пример: HTML, дата, fallback, range и форматирование чисел.

#### #70 — Безопасная обертка

```lua
local function render(template, data, userId)
    local result, errText, errNum = ParseTemplate(
        template,
        data or {},
        tostring(userId)
    )
    if errNum ~= 0 then
        return nil, "ParseTemplate: " .. tostring(errText), errNum
    end
    return result, "", 0
end

local htmlText, errText, errNum = render(
    "<b>{{.title}}</b>",
    { title = "Готово" },
    100
)
```

**Пояснение:** Рекомендуемый helper для повторного использования в Lua-скриптах.

---

[← Вернуться на главную](index.html)

`ParseTemplate` Lua Reference