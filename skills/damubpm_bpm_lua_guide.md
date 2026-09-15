[← На главную](index.html)

● Практический справочник

# BPM-процессы из Lua

Как запускать процессы, передавать входные данные, получать **instance** и **task**, продолжать ожидающие задачи, работать с UserTask/ManualTask и обмениваться переменными между BPM и Lua.

BPMSStartProcess · BPMSStartProcess2 · BPMSRunManualTask · var · sys · REST · Frontend

## 1. Как устроено выполнение BPM

Основная идея: запуск процесса выполняет автоматические точки до тех пор, пока процесс не завершится либо не дойдёт до задачи, которая требует продолжения. В ответе вы получаете идентификатор экземпляра и, если есть ожидающая задача, её `task`.

1.  **1. Запуск**  
    processCode + userId + input
2.  **2. Автоматические шаги**  
    скрипты, условия, маршрутизация
3.  **3. Ожидание**  
    возвращается task UUID
4.  **4. Продолжение**  
    task + input → nextTask

- instance

  UUID экземпляра процесса, возвращаемый при старте.

- task

  UUID текущей ожидающей задачи. Это главный ключ для её продолжения.

- output

  Глобальные выходные переменные процесса, доступные вызывающей стороне.

> **Не путайте два идентификатора экземпляра.** `instance`, возвращаемый стартовым API, — строковый UUID экземпляра. Внутри Lua `sys.instance_id` содержит внутренний числовой ID в строковом виде. Для `BPMSStartProcess2` как `parent_id` нужен числовой ID, поэтому обычно используют `tonumber(sys.instance_id)`.

## 2. Быстрый старт

**Lua · запуск процесса**

    local output, instance, task, errText, errNum = BPMSStartProcess(
      "process_code",
      tonumber(sys.user_id),
      {
        id = 125,
        title = "Заявка №125"
      }
    )

    if errNum ~= 0 or output == nil then
      error(errText ~= "" and errText or "Не удалось запустить процесс")
    end

    var.child_instance = instance
    var.child_task = task

**Lua · продолжение ожидающей задачи**

    local nextTask, errText, errNum = BPMSRunManualTask(
      var.task_uuid,
      tonumber(sys.user_id),
      {
        decision = "approve",
        comment = "Согласовано"
      }
    )

    if errNum ~= 0 then
      error(errText)
    end

    var.next_task = nextTask

## 3. Lua API BPM

В Lua-окружении доступны следующие BPM-функции.

### `BPMSStartProcess`

```lua
local output, instance, task, errText, errNum = BPMSStartProcess(
  processCode,
  userId,
  input
)
```

Запускает процесс по коду. `input` — Lua-таблица ключ/значение.

**Возвращает:**

- `output` — таблица выходных переменных;
- `instance` — UUID созданного экземпляра;
- `task` — UUID текущей ожидающей задачи, если она появилась;
- `errText` — текст ошибки;
- `errNum` — код ошибки.

### `BPMSStartProcess2`

```lua
local output, instance, task, errText, errNum = BPMSStartProcess2(
  processCode,
  userId,
  input,
  parentId
)
```

Работает как `BPMSStartProcess`, но позволяет передать внутренний числовой ID родительского экземпляра.

Обычно внутри BPM:

```lua
local parentId = tonumber(sys.instance_id)
```

### `BPMSRunManualTask`

```lua
local newTask, errText, errNum = BPMSRunManualTask(
  task,
  userId,
  input
)
```

Находит BPM-точку по UUID задачи, проверяет входные значения и продолжает экземпляр. При успешном выполнении возвращает UUID следующей задачи.

### `TerminateByInstanceId`

```lua
local errText, errNum = TerminateByInstanceId(instanceId, errorTable)
```

Прерывает процесс по внутреннему ID экземпляра и позволяет передать таблицу с информацией об ошибке.

> **Контракт типов.** `processCode` должен быть строкой, `userId` — числом, `input` — таблицей. Для старта рекомендуется проверять и `errNum`, и `output ~= nil`.

## 4. UserTask: задача пользователя

UserTask — точка процесса, рассчитанная на участие пользователя. У неё есть `task` UUID, открыто/закрыто состояние, форма и акторы, которым разрешено открыть задачу.

- ### Получение формы

  Форма UserTask запрашивается по `task`. Доступ к открытой форме проверяется по акторам задачи; публичный процесс также может разрешать просмотр.

- ### Завершение

  Надёжный внешний контракт — отправить `task` и `input`. Перед продолжением проверяются обязательные выходные переменные точки.

### Правильный сценарий UserTask

1.  **Старт**  
    получили task
2.  **Показ формы**  
    GET ShowUserTaskForm/:task
3.  **Пользователь вводит данные**
4.  **Завершение**  
    POST runUserTaskByTask

> **А что из Lua?** Отдельной Lua-функции с именем «RunUserTask» в предоставленном API нет. Программный вызов `BPMSRunManualTask(task, userId, input)` работает через тот же механизм поиска точки по `task`, проверки переменных и продолжения экземпляра. Явной проверки «это именно ManualTask» в этой Lua-обёртке нет. Поэтому технически механизм общий, но для пользовательской формы рекомендуемый контракт — UserTask REST/Frontend.

## 5. ManualTask из Lua

Для программного продолжения ожидающей задачи используется `BPMSRunManualTask`. Вызов ориентирован на UUID задачи, а не на код процесса или код точки.

| Параметр | Тип     | Назначение                                                         |
|----------|---------|--------------------------------------------------------------------|
| `task`   | string  | UUID текущей BPM-задачи.                                           |
| `userId` | integer | Пользователь, от имени которого продолжается задача.               |
| `input`  | table   | Переменные, которые передаются в текущую точку перед продолжением. |

### Что происходит при вызове

1. По `task` определяется текущая точка
2. Проверяются обязательные переменные
3. Текущая задача выполняется
4. Возвращается `newTask`

**Шаблон безопасного вызова**

    local function runTask(task, userId, input)
      if task == nil or task == "" then
        return nil, "task не задан"
      end

      local newTask, errText, errNum = BPMSRunManualTask(task, userId, input or {})
      if errNum ~= 0 then
        return nil, errText
      end

      return newTask, nil
    end

## 6. Переменные внутри BPM Lua

- ### `var`

  Таблица глобальных переменных процесса. Перед запуском скрипта она заполняется значениями экземпляра; после скрипта значения считываются обратно.

- ### `sys`

  Системный контекст: `instance_id`, `user_id`, `frontend`, `lang`, `action_entity_id`, session ID, IP.

- ### `request`

  Контекст HTTP-запроса. В текущем API используется `request.get` и `request.user_id`.

| Поле                       | Пример               | Комментарий                                                       |
|----------------------------|----------------------|-------------------------------------------------------------------|
| `sys.instance_id`          | `"44125"`            | Внутренний ID как строка.                                         |
| `sys.user_id`              | `"73"`               | Пользователь как строка; для BPM API используйте `tonumber()`.    |
| `sys.frontend`             | зависит от контекста | Признак/контекст frontend.                                        |
| `sys.lang`                 | `"ru"`               | Добавляется при наличии запроса.                                  |
| `sys.action_entity_id`     | `120`                | Сущность действия процесса, если настроена.                       |
| `sys.anonymous_session_id` | строка               | Идентификатор анонимной сессии.                                   |
| `sys.x_real_ip`            | `"10.0.0.15"`        | Берётся из заголовка `X-Real-Ip`.                                 |
| `sys.next_task_uuid`       | UUID                 | Можно задать в Lua; движок считывает значение после скрипта.      |
| `sys.next_task_hide`       | `true`               | Можно задать в Lua; влияет на возврат/видимость следующей задачи. |

**Lua · чтение и изменение контекста**

    local currentUserId = tonumber(sys.user_id)
    local currentInstanceId = tonumber(sys.instance_id)

    var.status = "processing"
    var.updated_by = tostring(currentUserId)

    if request and request.get and request.get.source then
      var.source = request.get.source
    end

## 7. Запуск BPM из Frontend

Для страницы/виджета можно использовать готовую обёртку `bpRun`. Код процесса передаётся первым аргументом, объект входных переменных — вторым, callback — третьим.

**Frontend · запуск процесса**

    this.appComponent.bpRun(
      'process_code',
      {
        id: item.id,
        title: item.title
      },
      data => {
        console.log('BP result:', data);
      }
    );

> **Практика.** Передавайте в объекте только те поля, которые объявлены входными переменными BPM. Коды полей должны совпадать с кодами переменных процесса.

## 8. REST API BPM

### Запуск процесса

**POST /restapi/bpms/start**

    {
      "processCode": "process_code",
      "input": {
        "id": 125,
        "title": "Заявка №125"
      }
    }

**Ответ**

    {
      "ok": true,
      "instance": "INSTANCE-UUID",
      "task": "TASK-UUID",
      "errorText": "",
      "output": {},
      "instanceIsFinished": false
    }

> **Права запуска**Запуск разрешается, если у пользователя есть роль с правом запуска этого процесса либо процесс помечен публичным. Для пользователя в readonly mode запуск блокируется.

### Завершение UserTask по task — рекомендуемый вариант

**POST /restapi/bpms/runUserTaskByTask/**

    {
      "task": "TASK-UUID",
      "input": {
        "decision": "approve",
        "comment": "Согласовано"
      }
    }

Ответ содержит `ok`, `errorVars`, `errorText`, новую `task`, `output`, `instance` и `instanceIsFinished`.

### Форма UserTask

| Метод | Адрес                                              | Назначение                                        |
|-------|----------------------------------------------------|---------------------------------------------------|
| GET   | `/restapi/bpms/ShowUserTaskForm/:task`             | Получить форму, переменные и информацию по шагам. |
| GET   | `/restapi/bpms/ShowUserTaskFormAngular/:task`      | Получить данные Angular-формы UserTask.           |
| GET   | `/restapi/bpms/ShowInstanceForm/:instance`         | Получить форму по экземпляру.                     |
| GET   | `/restapi/bpms/ShowInstanceAngularClass/:instance` | Получить Angular-класс по экземпляру.             |
| GET   | `/restapi/bpms/ShowInstanceAngularForm/:instance`  | Получить Angular-форму по экземпляру.             |

> **Не опирайтесь на лишние поля старых endpoint'ов.** В варианте `runUserTaskByInstance` структура запроса содержит `processCode`, `instance` и `pointCode`, но продолжение фактически строится по `task`. В `manualExecByInstance` текущая реализация также ориентируется на `task` и не использует переданный `input`. Для нового кода проще и понятнее строить контракт вокруг UUID задачи.

## 9. Шаблоны генерации Lua-вызовов

В Markdown-версии вместо интерактивного генератора приведены готовые шаблоны.

### Запуск процесса

```lua
local output, instance, task, errText, errNum = BPMSStartProcess(
  "process_code",
  tonumber(sys.user_id),
  {
    id = var.id,
    title = var.title
  }
)
```

### Запуск дочернего процесса

```lua
local output, instance, task, errText, errNum = BPMSStartProcess2(
  "child_process",
  tonumber(sys.user_id),
  {
    id = var.id
  },
  tonumber(sys.instance_id)
)
```

### Продолжение задачи

```lua
local nextTask, errText, errNum = BPMSRunManualTask(
  var.task_uuid,
  tonumber(sys.user_id),
  {
    decision = "approve",
    comment = var.comment
  }
)
```

## 10. Библиотека примеров

Ниже приведено **45 практических примеров** запуска процессов, продолжения задач, работы с переменными, Frontend и REST.

### Запуск процессов

#### Пример 1. Минимальный запуск

Запуск без входных данных.

```lua
local out, instance, task, errText, errNum = BPMSStartProcess(
  "simple_process",
  tonumber(sys.user_id),
  {}
)
```

#### Пример 2. Запуск с ID сущности

Передаём идентификатор записи.

```lua
local out, instance, task, errText, errNum = BPMSStartProcess(
  "entity_process",
  tonumber(sys.user_id),
  { entity_id = var.id }
)
```

#### Пример 3. Запуск с несколькими полями

Строки, числа и логические значения.

```lua
local out, instance, task, errText, errNum = BPMSStartProcess(
  "request_process",
  tonumber(sys.user_id),
  {
    request_id = var.id,
    title = var.title,
    amount = 150000,
    urgent = true
  }
)
```

#### Пример 4. Передача структуры

Lua-таблица как сложная входная переменная.

```lua
local input = {
  customer = {id = 10, name = "Aruzhan"},
  items = {{id=1, qty=2},{id=2, qty=1}}
}
local out, instance, task, errText, errNum =
  BPMSStartProcess("order_process", tonumber(sys.user_id), input)
```

#### Пример 5. Сохранить task дочернего процесса

Task можно сохранить в переменную родительского процесса.

```lua
local out, instance, task, errText, errNum =
  BPMSStartProcess("approval", tonumber(sys.user_id), {id=var.id})
if errNum == 0 and out ~= nil then
  var.approval_instance = instance
  var.approval_task = task
end
```

#### Пример 6. Проверка output

Читаем выходную переменную дочернего процесса.

```lua
local out, instance, task, errText, errNum =
  BPMSStartProcess("calculator", tonumber(sys.user_id), {a=10,b=20})
if errNum == 0 and out then
  var.result = out.result
end
```

#### Пример 7. Старт от другого userId

Когда userId известен явно.

```lua
local userId = 73
local out, instance, task, errText, errNum =
  BPMSStartProcess("process_code", userId, {id=100})
```

#### Пример 8. Дочерний процесс

Связываем новый экземпляр с текущим.

```lua
local out, instance, task, errText, errNum = BPMSStartProcess2(
  "child_process",
  tonumber(sys.user_id),
  { parent_ref = var.id },
  tonumber(sys.instance_id)
)
```

#### Пример 9. Дочерний процесс с parent_id=0

Явный запуск без родителя через второй API.

```lua
local out, instance, task, errText, errNum =
  BPMSStartProcess2("standalone", tonumber(sys.user_id), {}, 0)
```

#### Пример 10. Цепочка двух процессов

Второй получает данные первого.

```lua
local o1, i1, t1, e1, n1 = BPMSStartProcess("prepare", tonumber(sys.user_id), {id=var.id})
if n1 ~= 0 or not o1 then error(e1) end
local o2, i2, t2, e2, n2 = BPMSStartProcess("notify", tonumber(sys.user_id), {result=o1.result})
if n2 ~= 0 or not o2 then error(e2) end
```

#### Пример 11. Не падать при ошибке

Сохраняем ошибку в переменную процесса.

```lua
local out, instance, task, errText, errNum =
  BPMSStartProcess("external_flow", tonumber(sys.user_id), {id=var.id})
if errNum ~= 0 or out == nil then
  var.child_error = errText
  var.child_ok = "0"
else
  var.child_ok = "1"
end
```

#### Пример 12. Функция-обёртка

Повторно используемый helper.

```lua
local function bpStart(code, input)
  local out, instance, task, errText, errNum = BPMSStartProcess(code, tonumber(sys.user_id), input or {})
  if errNum ~= 0 or out == nil then return nil, errText end
  return {output=out, instance=instance, task=task}, nil
end

local r, err = bpStart("process_code", {id=var.id})
```

### UserTask / ManualTask

#### Пример 13. ManualTask без параметров

Продолжение задачи, если текущая точка не требует данных.

```lua
local nextTask, errText, errNum =
  BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), {})
if errNum ~= 0 then error(errText) end
```

#### Пример 14. ManualTask с решением

Передаём результат согласования.

```lua
local nextTask, errText, errNum = BPMSRunManualTask(
  var.task_uuid,
  tonumber(sys.user_id),
  {decision="approve", comment="OK"}
)
```

#### Пример 15. Сохранить следующую задачу

newTask становится task следующего шага.

```lua
local newTask, errText, errNum =
  BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), {status="done"})
if errNum == 0 then
  var.task_uuid = newTask
end
```

#### Пример 16. Проверка пустого task

Не вызывать API с пустым UUID.

```lua
if var.task_uuid == nil or var.task_uuid == "" then
  error("BPM task UUID is empty")
end
local newTask, errText, errNum =
  BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), {})
```

#### Пример 17. Обработка errNum=3

Task не найден/не определяется точка.

```lua
local newTask, errText, errNum =
  BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), {})
if errNum == 3 then
  var.task_state = "not_found"
  var.task_error = errText
end
```

#### Пример 18. Обработка errNum=4

Не хватает обязательных переменных.

```lua
local newTask, errText, errNum =
  BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), {decision=var.decision})
if errNum == 4 then
  var.validation_error = errText
end
```

#### Пример 19. Прокинуть ID и комментарий

Типовой submit задачи.

```lua
local newTask, errText, errNum = BPMSRunManualTask(
  var.task_uuid, tonumber(sys.user_id),
  {id=var.id, comment=var.comment}
)
```

#### Пример 20. Условное согласование

Собираем input динамически.

```lua
local input = {comment = var.comment}
if tonumber(var.amount or "0") > 1000000 then
  input.decision = "escalate"
else
  input.decision = "approve"
end
local newTask, errText, errNum = BPMSRunManualTask(var.task_uuid, tonumber(sys.user_id), input)
```

#### Пример 21. Повторно используемый helper

Единая обработка ошибок задач.

```lua
local function completeTask(task, input)
  local nextTask, errText, errNum = BPMSRunManualTask(task, tonumber(sys.user_id), input or {})
  if errNum ~= 0 then return nil, errText, errNum end
  return nextTask, nil, 0
end
```

#### Пример 22. Task из запуска процесса

Сразу продолжить задачу нового процесса.

```lua
local out, instance, task, errText, errNum =
  BPMSStartProcess("process_code", tonumber(sys.user_id), {id=var.id})
if errNum == 0 and out and task ~= "" then
  local nextTask, e, n = BPMSRunManualTask(task, tonumber(sys.user_id), {auto="1"})
end
```

#### Пример 23. Программное подтверждение UserTask

Технически task-механизм общий; применять только в доверенном сценарии.

```lua
local nextTask, errText, errNum =
  BPMSRunManualTask(var.user_task_uuid, tonumber(sys.user_id), {decision="approve"})
if errNum ~= 0 then error(errText) end
```

#### Пример 24. Завершить с массивом

Структурированное значение в input.

```lua
local nextTask, errText, errNum = BPMSRunManualTask(
  var.task_uuid, tonumber(sys.user_id),
  {items={{id=1},{id=2},{id=3}}}
)
```

### Переменные `var`, `sys`, `request`

#### Пример 25. Изменить переменную процесса

var автоматически считывается после Lua-точки.

```lua
var.status = "approved"
var.comment = "Обработано автоматически"
```

#### Пример 26. Взять текущего пользователя

sys.user_id хранится строкой.

```lua
local userId = tonumber(sys.user_id)
var.executor_id = tostring(userId)
```

#### Пример 27. Взять внутренний instance ID

Полезно для parent_id.

```lua
local parentId = tonumber(sys.instance_id)
local out, instance, task, errText, errNum =
  BPMSStartProcess2("child", tonumber(sys.user_id), {}, parentId)
```

#### Пример 28. Получить язык

Поле доступно при HTTP-контексте.

```lua
local lang = sys.lang or "ru"
var.notification_lang = lang
```

#### Пример 29. Получить IP

X-Real-Ip переносится в sys.

```lua
if sys.x_real_ip and sys.x_real_ip ~= "" then
  var.client_ip = sys.x_real_ip
end
```

#### Пример 30. GET параметр запроса

request.get содержит query/form параметры.

```lua
if request and request.get then
  var.source = request.get.source or "unknown"
end
```

#### Пример 31. action_entity_id

Используем сущность действия процесса.

```lua
if sys.action_entity_id then
  var.entity_id = tostring(sys.action_entity_id)
end
```

#### Пример 32. next_task_uuid

Переопределение возвращаемого task в сценарии, где это предусмотрено моделью.

```lua
sys.next_task_uuid = var.preferred_task_uuid
```

#### Пример 33. next_task_hide

Скрыть следующую задачу в поддерживаемом сценарии.

```lua
sys.next_task_hide = true
```

#### Пример 34. Безопасное число

Переменные часто приходят строками.

```lua
local amount = tonumber(var.amount or "0") or 0
if amount > 100000 then
  var.route = "large"
end
```

#### Пример 35. Структура в var

Записываем Lua-таблицу в struct-переменную.

```lua
var.payload = {
  id = var.id,
  status = "ready",
  meta = {source = "bpm"}
}
```

### Frontend

#### Пример 36. bpRun минимальный

Самый короткий вызов с фронта.

```javascript
this.appComponent.bpRun('process_code', {}, data => {
  console.log(data);
});
```

#### Пример 37. bpRun с записью

Передача полей выбранного item.

```javascript
this.appComponent.bpRun('process_code', {
  id: item.id,
  title: item.title
}, data => console.log('BP result:', data));
```

#### Пример 38. bpRun после сохранения

Запускаем процесс после создания записи.

```javascript
this.appComponent.bpRun('publish_request', {
  id: saved.id,
  status: saved.status
}, data => {
  if (data && data.ok) this.reload();
});
```

#### Пример 39. bpRun с массивом

Передача списка объектов.

```javascript
this.appComponent.bpRun('mass_process', {
  ids: selected.map(x => x.id)
}, data => console.log(data));
```

### REST API

#### Пример 40. REST start

HTTP запуск по processCode.

```text
POST /restapi/bpms/start
Content-Type: application/json

{
  "processCode":"process_code",
  "input":{"id":125,"title":"Заявка"}
}
```

#### Пример 41. REST UserTask submit

Завершение по UUID задачи.

```text
POST /restapi/bpms/runUserTaskByTask/
Content-Type: application/json

{
  "task":"TASK-UUID",
  "input":{"decision":"approve"}
}
```

#### Пример 42. Получить HTML-форму UserTask

Форма запрашивается по task.

```text
GET /restapi/bpms/ShowUserTaskForm/TASK-UUID
```

#### Пример 43. Получить Angular-форму UserTask

Вариант для Angular-формы.

```text
GET /restapi/bpms/ShowUserTaskFormAngular/TASK-UUID
```

#### Пример 44. Форма экземпляра

Запрос по instance UUID.

```text
GET /restapi/bpms/ShowInstanceForm/INSTANCE-UUID
```

#### Пример 45. Проверка finished

При старте и submit смотрите instanceIsFinished.

```text
if (result.ok && result.instanceIsFinished) {
  console.log('Процесс завершён', result.output);
} else {
  console.log('Следующая задача', result.task);
}
```

## 11. Ошибки и обработка

| Вызов               | errNum | Смысл                                                                                                                  | Действие                                                 |
|---------------------|--------|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| `BPMSStartProcess*` | 0      | Обычно успех. При неверных типах аргументов старый контракт может вернуть пустые значения без корректного кода ошибки. | Проверять `output ~= nil` и валидировать типы до вызова. |
| `BPMSStartProcess*` | 1      | Ошибка создания экземпляра.                                                                                            | Логировать `errText`, не продолжать цепочку.             |
| `BPMSRunManualTask` | 0      | Успех.                                                                                                                 | Использовать возвращённый `newTask`.                     |
| `BPMSRunManualTask` | 2      | Ошибка привязки параметров или выполнения.                                                                             | Проверить task/userId/input и текст ошибки.              |
| `BPMSRunManualTask` | 3      | Не удалось определить точку по task.                                                                                   | Проверить UUID и что задача существует.                  |
| `BPMSRunManualTask` | 4      | Не прошла проверка обязательных переменных точки.                                                                      | Передать недостающие значения.                           |

**Универсальный start wrapper**

    local function startProcess(code, input, userId)
      userId = userId or tonumber(sys.user_id)
      assert(type(code) == "string" and code ~= "", "processCode required")
      assert(type(userId) == "number", "userId must be number")
      assert(type(input) == "table", "input must be table")

      local output, instance, task, errText, errNum = BPMSStartProcess(code, userId, input)
      if errNum ~= 0 or output == nil then
        return nil, errText ~= "" and errText or "BPM start failed"
      end

      return {output=output, instance=instance, task=task}, nil
    end

## 12. Подводные камни

- ### 1. task важнее pointCode

  Для продолжения текущей задачи храните UUID `task`. Именно он используется для поиска текущей BPM-точки.

- ### 2. UserTask имеет акторов

  Открытие пользовательской формы связано с actor-доступом. Не проектируйте UI так, будто любой пользователь может открыть произвольный task UUID.

- ### 3. Проверка required-переменных

  Перед исполнением задачи вход сверяется с требованиями текущей точки. Пустой `{}` подходит только если обязательных значений нет.

- ### 4. Типы sys.user_id / sys.instance_id

  В системном контексте они строковые. Перед передачей в BPM-функции используйте `tonumber()`.

- ### 5. Выходные переменные

  В API старта возвращаются именно глобальные output-переменные процесса; не ожидайте в `output` каждую внутреннюю переменную.

- ### 6. Старые endpoint'ы

  Некоторые структуры запросов содержат поля, которые текущая реализация фактически не использует. Для новых интеграций предпочитайте минимальный контракт `task + input`.

## 13. Шпаргалка

**Минимум, который стоит запомнить**

    -- START
    local out, instance, task, errText, errNum =
      BPMSStartProcess("process_code", tonumber(sys.user_id), {id = var.id})

    -- CHILD START
    local out2, childInstance, childTask, errText2, errNum2 =
      BPMSStartProcess2("child_process", tonumber(sys.user_id), {id = var.id}, tonumber(sys.instance_id))

    -- CONTINUE TASK
    local nextTask, taskErr, taskErrNum =
      BPMSRunManualTask(task, tonumber(sys.user_id), {decision = "approve"})

    -- PROCESS VARIABLES
    var.status = "done"
    local instanceId = tonumber(sys.instance_id)
    local userId = tonumber(sys.user_id)

DamuBPM · BPM + Lua practical reference · Вернуться на главную
