# DamuBPM CRUD + JIT

> Интерактивная техническая инструкция по построению CRUD-страниц DamuBPM на Angular-логике, HTML-шаблонах и JIT.

[← Главная](index.html)

---

## Содержание

1. [Архитектура страницы](#архитектура-страницы)
2. [Минимальная структура класса](#минимальная-структура-класса)
3. [Жизненный цикл CRUD-страницы](#жизненный-цикл-crud-страницы)
4. [QueryOptions и загрузка данных](#queryoptions-и-загрузка-данных)
5. [Получение метаданных полей](#получение-метаданных-полей)
6. [Фильтры](#фильтры)
7. [Таблица PrimeNG](#таблица-primeng)
8. [Сортировка](#сортировка)
9. [Пагинация](#пагинация)
10. [Выбор строк](#выбор-строк)
11. [Массовые действия](#массовые-действия)
12. [Создание записи](#создание-записи)
13. [Удаление записей](#удаление-записей)
14. [Переход к детализации](#переход-к-детализации)
15. [JIT-режим](#jit-режим)
16. [Модальные страницы](#модальные-страницы)
17. [Печать](#печать)
18. [Настройка колонок](#настройка-колонок)
19. [Архивные записи](#архивные-записи)
20. [Каталог методов](#каталог-методов)
21. [Типовой HTML-шаблон](#типовой-html-шаблон)
22. [Шаблон новой CRUD-страницы](#шаблон-новой-crud-страницы)
23. [Типовые ошибки](#типовые-ошибки)
24. [Checklist](#checklist)

---

# Архитектура страницы

CRUD-страница в DamuBPM строится не как статическая Angular-таблица, а как страница, управляемая метаданными сущности и запросами DamuBPM.

Основные элементы:

```text
DamuBPM Entity
    ↓
get_filter_cols_by_code
    ↓
fields[]
    ↓
QueryOptions
    ↓
dbQueryService.getQuery(...)
    ↓
table.items
    ↓
filtered[]
    ↓
PrimeNG p-table
```

Дополнительно страница использует:

- `entity_id` — ID сущности DamuBPM;
- `entity_code` — код сущности;
- `table_code` — код таблицы;
- `query_code` — код запроса;
- `fields` — метаданные колонок;
- `filtered` — строки таблицы;
- `query_options` — параметры запроса;
- `tools` — кнопки процессов над сущностью;
- `acts_many` — массовые действия;
- `static_filters` — статические фильтры;
- `checked_rows` — выбранные строки;
- `DATA/data` — входные JIT-параметры.

---

# Минимальная структура класса

```javascript
const vm = this;
const { QueryOptions } = Models;
const { first } = rxjs;
const DATA = data;

return class GenClass extends vm.constructor {

    entity_id = '3352';
    entity_code = 'its_d_ga_mnr';
    page_id = '12583';

    table_code = this.entity_code;
    query_code = this.entity_code;

    query_options = new QueryOptions();

    fields = [];
    filtered = [];
    tools = [];
    acts_many = [];

    checked_rows = [];
    selected_all_rows = false;

    static_filters = [];

    page = 1;
    perpage = 15;

    table;

    ngOnInit() {
        if (this.only_jit_page) {
            this.restartAll();
        }
    }
}
```

---

# Жизненный цикл CRUD-страницы

Типичная цепочка запуска:

```text
ngOnInit()
   ↓
restartAll()
   ↓
getTableFields()
   ↓
update()
   ↓
setQueryOptions()
   ↓
getTableSort()
   ↓
dbQueryService.getQuery()
   ↓
filtered = table.items
   ↓
HTML / p-table
```

Основной метод инициализации:

```javascript
restartAll() {
    this.perpage_vars.push(1000);

    if (data && data.static_filters) {
        this.static_filters = data.static_filters;
    }

    this.getTableFields(this.table_code);
    this.getTools();
}
```

Важно: `getTableFields()` после загрузки метаданных вызывает `update()`.

---

# QueryOptions и загрузка данных

`QueryOptions` — центральный объект управления выборкой.

```javascript
this.query_options = new QueryOptions(
    this.query_code_new ||
    (data && data.query_code) ||
    this.query_code ||
    this.table_code
);
```

Основные параметры:

```javascript
this.query_options.page = params.page || 1;
this.query_options.perpage = params.perpage || 15;
```

JIT может передавать дополнительные параметры:

```javascript
if (data && data.flt) this.query_options.flt = data.flt;
if (data && data.flteq) this.query_options.flteq = data.flteq;
if (data && data.fltin) this.query_options.fltin = data.fltin;
if (data && data.limit) this.query_options.perpage = data.limit;
if (data && data.param1) this.query_options.param1 = data.param1;
if (data && data.param2) this.query_options.param2 = data.param2;
if (data && data.func22) this.query_options.func22 = data.func22;
```

## Виды фильтрации

| Свойство | Использование |
|---|---|
| `flt` | строковый поиск |
| `flteq` | точное равенство |
| `fltin` | поиск по списку значений |
| `func22` | диапазоны, даты, специальные условия |
| `param1` | параметр запроса |
| `param2` | второй параметр запроса |
| `orderBy` | поле сортировки |
| `orderAsc` | направление сортировки |
| `page` | номер страницы |
| `perpage` | количество записей |

---

# Получение метаданных полей

Поля страницы загружаются через запрос:

```javascript
getTableFields(code) {
    let q_opt = new QueryOptions('get_filter_cols_by_code');
    q_opt.param1 = code;

    return this.dbQueryService.getQuery(q_opt)
        .pipe(first())
        .subscribe(tableFields => {
            this.fields = tableFields.items || [];
            this.update();
        });
}
```

`fields` содержит метаданные, например:

```text
alias
title
_data_type_code
_def_sel_query_code
_ui_comp_code
is_advanced
sort
_fixed
_static_fixed
```

Именно по этим метаданным HTML автоматически решает, какой компонент использовать.

---

# Фильтры

## Строковые поля

```javascript
this.query_options.flt[field.alias] = field.value;
```

HTML:

```html
<input
    pInputText
    [(ngModel)]="field.value"
    (change)="onSubmitFieldFilter()"
    class="p-inputtext-sm"
    placeholder="{{ 'Все' | translate }}"
/>
```

---

## Boolean

```javascript
this.query_options.flteq[field.alias] = value;
```

HTML:

```html
<p-triStateCheckbox
    [(ngModel)]="field.value"
    (ngModelChange)="onSubmitFieldFilter()"
    [inputId]="field.alias"
></p-triStateCheckbox>
```

Преимущество `p-triStateCheckbox`:

```text
null → Все
true → Да
false → Нет
```

---

## Reference

Для reference-полей используется `fltin`.

```javascript
this.query_options.fltin[field.alias] = field.value?.split(',');
```

HTML:

```html
<prime-select-multi
    [(ngModel)]="field.value"
    (ngModelChange)="onSubmitFieldFilter()"
    [dropdown]="false"
    [query-code]="field._def_sel_query_code"
    [disabled]="field.is_advanced == 1"
    [showClear]="false"
    [limit]="35"
></prime-select-multi>
```

---

## Даты

Используются:

```text
date
datetime
timestamp
current_datetime
current_and_on_update_datetime
```

Фильтр передается через `func22`:

```javascript
this.query_options.func22[field.alias] = value;
```

HTML:

```html
<prime-date
    selectionMode="range"
    [readonlyInput]="true"
    [(ngModel)]="field.value"
    (ngModelChange)="onSubmitFieldFilter()"
    [showTime]="false"
    [showClear]="true"
></prime-date>
```

---

## Числовой диапазон

```javascript
filt.value = (filt.from || filt.to || 0)
    + '|'
    + (filt.to || filt.from || 10000000);

this.query_options.func22[filt.alias] = filt.value;
```

Пример:

```text
100|500
```

означает диапазон от `100` до `500`.

---

# Таблица PrimeNG

Основной компонент:

```html
<p-table
    #main_table
    [columns]="fields"
    [value]="filtered"
    [contextMenu]="cm"
    [(contextMenuSelection)]="current_item"
    dataKey="id"
>
```

Колонки генерируются динамически:

```html
<ng-container *ngFor="let field of fields">
    <th *ngIf="field.is_advanced != 1">
        {{ field.title | translate }}
    </th>
</ng-container>
```

Строки:

```html
<ng-template pTemplate="body" let-rowData let-fields="columns">
    <tr [pContextMenuRow]="rowData">
        <ng-container *ngFor="let field of fields">
            <td
                *ngIf="field.is_advanced != 1"
                [ngSwitch]="field._data_type_code"
            >
                ...
            </td>
        </ng-container>
    </tr>
</ng-template>
```

---

# Отображение типов данных

## Boolean

```html
<span *ngSwitchCase="'boolean'">
    <i
        class="pi"
        [ngClass]="{
            'pi-check-square': rowData[field.alias] == 1,
            'pi-stop': rowData[field.alias] != 1
        }"
    ></i>
</span>
```

## Double / Number

```html
<span *ngSwitchCase="'double'">
    <span [innerHtml]="rowData[field.alias]"></span>
</span>
```

## Audio

```html
<span *ngSwitchCase="'audio'">
    <audio controls [src]="rowData[field.alias]"></audio>
</span>
```

---

# Сортировка

Метод:

```javascript
sortByField(field) {
    field.sort = field.sort != 0 && field.sort != 1
        ? 0
        : field.sort == 0
            ? 1
            : null;

    this.update();
}
```

Логика:

```text
null → ASC → DESC → null
```

При формировании `QueryOptions`:

```javascript
if (item.sort == 0 || item.sort == 1) {
    this.query_options.orderAsc = item.sort;
    this.query_options.orderBy = item.alias;
}
```

---

# Пагинация

HTML:

```html
<pagination
    [perpage-vars]="perpage_vars"
    [row-count]="table?.allCount"
    [page]="query_options.page"
    [perpage]="query_options.perpage"
    [show-gotopage]="false"
    [show-perpage]="true"
    (pageChanged)="changePage($event)"
    (perPageChanged)="changePerPage($event)"
></pagination>
```

## changePage

```javascript
changePage(page) {
    let q_params = {
        ...this.route.snapshot.queryParams
    };

    q_params.page = page;
    q_params.perpage = this.query_options.perpage;

    if (!this.only_jit_page) {
        this.router.navigate([], {
            relativeTo: this.route,
            queryParams: q_params,
            queryParamsHandling: 'merge'
        });
    } else {
        this.update(q_params);
    }
}
```

---

# Выбор строк

## Одна строка

```javascript
setChecked(checked, id) {
    if (checked) {
        this.checked_rows.push(id);
    } else {
        let index = this.checked_rows.indexOf(id);

        if (index != -1) {
            this.checked_rows.splice(index, 1);
        }
    }

    this.selected_all_rows =
        this.checked_rows.length == this.table?.allCount;

    this.acts_many_menu = this.setActManyMenu();
}
```

HTML:

```html
<p-checkbox
    [(ngModel)]="rowData.table_row_checked"
    (onChange)="setChecked(rowData.table_row_checked,rowData.id)"
    [binary]="true"
></p-checkbox>
```

---

## Выбрать все

```javascript
setCheckedAll() {
    this.checked_rows = [];

    for (let item of this.filtered) {
        item.table_row_checked = this.selected_all_rows;

        if (item.table_row_checked) {
            this.checked_rows.push(item.id);
        }
    }

    this.acts_many_menu = this.setActManyMenu();
}
```

---

# Массовые действия

Массовые действия загружаются запросом:

```javascript
getActsMany() {
    let q_opt = new QueryOptions('entity_acts_many');
    q_opt.param1 = this.entity_id;

    return this.dbQueryService.getQuery(q_opt)
        .pipe(first())
        .subscribe(resp => {
            this.acts_many = resp.items || [];
            this.acts_many_menu = this.setActManyMenu();
        });
}
```

Запуск действия:

```javascript
doAct(act) {
    let ids = this.checked_rows.join();

    if (!this.checked_rows.length) {
        ids = this.current_item.id;
    }

    let options = Object.assign({}, this.query_options);

    this.appComponent.bpRun(
        act.code,
        {
            url: `?code=${options.code}&ids=${ids}`
        },
        () => this.update()
    );
}
```

---

# Tools сущности

```javascript
getTools() {
    let tool_q_opt =
        new QueryOptions('bp_processes_tools_by_entity_id');

    tool_q_opt.perpage = 100;
    tool_q_opt.page = 1;
    tool_q_opt.param1 = this.entity_id;

    return this.dbQueryService.getQuery(tool_q_opt)
        .pipe(first())
        .subscribe(resp => {
            if (resp && resp.items) {
                this.tools = resp.items;
            }
        });
}
```

HTML:

```html
<p-button
    *ngFor="let tool of tools"
    (click)="appComponent.bpRun(tool.code,{},bindCallBack)"
    [label]="tool.title | translate"
    [icon]="tool.icon || tool.icon_value"
></p-button>
```

---

# Создание записи

Запись создается через DamuBPM API:

```javascript
add() {
    let apiAddress = environment.apiUrl + '/update_v_1_1';

    const body = JSON.stringify({
        items: [{
            table_name: this.entity_code,
            action: 'insert',
            values: [{
                sys$uuid: uuid.v4(),
                id: 0
            }]
        }]
    });

    this.httpClient.post(apiAddress, body)
        .subscribe(resp => {
            if (resp['error'] == 0) {
                resp.items.forEach(item => {
                    if (item.table_name == this.entity_code) {
                        this.router.navigate([
                            this.entity_code + 'details',
                            item.last_insert_id
                        ]);
                    }
                });
            } else {
                this.alertService.error(
                    'Ошибка' + resp['error_text']
                );
            }
        });
}
```

Формат API-запроса:

```json
{
  "items": [
    {
      "table_name": "entity_code",
      "action": "insert",
      "values": [
        {
          "sys$uuid": "uuid",
          "id": 0
        }
      ]
    }
  ]
}
```

---

# Удаление записей

```javascript
deleteChecked() {
    let values = this.checked_rows.map(id => ({ id }));

    let body = JSON.stringify({
        items: [{
            table_name: this.table_code,
            action: 'delete',
            values
        }]
    });

    this.httpClient
        .post(
            environment.apiUrl + '/update_v_1_1',
            body
        )
        .subscribe(resp => {
            if (resp['error'] == 0) {
                this.alertService.info('Удалено');
                this.update();
            } else {
                this.alertService.error(
                    'Ошибка' + resp['error_text']
                );
            }
        });
}
```

Формат:

```json
{
  "items": [
    {
      "table_name": "entity_code",
      "action": "delete",
      "values": [
        { "id": 10 },
        { "id": 11 },
        { "id": 12 }
      ]
    }
  ]
}
```

---

# Переход к детализации

```javascript
goToDetail(item) {
    this.router.navigate([
        item.angular_detail_page_url$
            ? item.angular_detail_page_url$
            : 'its_d_ga_mnrdetails/' + item.id
    ]);
}
```

Рекомендуемый универсальный вариант:

```javascript
goToDetail(item) {
    const url = item.angular_detail_page_url$
        || this.entity_code + 'details/' + item.id;

    this.router.navigate([url]);
}
```

---

# JIT-режим

Определение JIT:

```javascript
get only_jit_page() {
    return DATA && Object.keys(DATA).length > 0;
}
```

Аналогичный getter:

```javascript
get hide_if_jit_data() {
    return DATA && Object.keys(DATA).length > 0;
}
```

В обычном Angular-режиме параметры берутся из `route`.

В JIT-режиме параметры приходят непосредственно через `data`.

Пример JIT DATA:

```javascript
{
    query_code: 'its_d_ga_mnr',
    param1: '100',
    limit: 20,
    flteq: {
        status: '1'
    },
    static_filters: []
}
```

---

# JIT сохранение встроенной страницы

```javascript
saveJitPage(item, main_table) {
    item.jit_page.save(resp => {

        for (const field of this.fields) {
            if (field.alias in item.jit_page.detail) {
                item[field.alias] =
                    item.jit_page.detail[field.alias];
            }
        }

        this.alertService.success(
            'Успешное сохранение',
            {
                position:
                    Models.AlertPosition.BottomRight
            }
        );

        this.closeJitPage(item, main_table);
        this.update();
    });
}
```

---

# Модальные страницы

Страница детализации может быть открыта внутри `DialogTemplateComponent`.

```javascript
openPagesAsModal(page, detail) {
    let jit_page = null;

    let buttons = [
        {
            title: 'Save',
            class: 'p-button-primary',
            click: () => {
                jit_page.save();
                this.dialog_ref.close();
            }
        },
        {
            title: 'Cancel',
            class: 'p-button-secondary',
            click: () => {
                this.dialog_ref.close();
            }
        }
    ];

    this.dialog_ref = this.dialogService.open(
        Components.DialogTemplateComponent,
        {
            header: this.modal_title,
            style: {
                width: '75%',
                'min-height': '75vh'
            },
            data: {
                buttons,
                data: { detail },
                type: 'pages',
                code: page,
                getJitComponent: jitPageDetail => {
                    jit_page = jitPageDetail;
                }
            }
        }
    );

    this.dialog_ref.onClose.subscribe(() => {
        this.update();
    });
}
```

---

# Печать

```javascript
print() {
    let options = Object.assign({}, this.query_options);

    let url = '?' + this.query_options.url.replace(
        /&((perpage|page|loader)=[^&]+)+/gi,
        ''
    );

    if (this.checked_rows.length > 0) {
        this.appComponent.bpRun(
            'exp_template',
            {
                no_autoprint: 1,
                url:
                    `?code=${options.code}` +
                    `&ids=${this.checked_rows.join()}`,
                entity_id: this.entity_id
            }
        );

        return;
    }

    this.appComponent.bpRun(
        'exp_template',
        {
            no_autoprint: 1,
            url,
            entity_id: this.entity_id
        }
    );
}
```

---

# Настройка колонок

## Скрытие / отображение

```javascript
addRemoveField(field) {
    field.is_advanced = field.is_advanced == 1
        ? 0
        : 1;
}
```

---

## Перемещение влево

```javascript
fieldOrderLeft(index) {
    for (let i = index - 1; i >= 0; i--) {
        let field = this.fields[i + 1];

        this.fields.splice(i + 1, 1);
        this.fields.splice(i, 0, field);

        if (this.fields[i + 1].is_advanced != 1) {
            break;
        }
    }

    this.saveFieldsOrder();
}
```

---

## Перемещение вправо

```javascript
fieldOrderRight(index) {
    for (let i = index + 1;
         i < this.fields.length;
         i++) {

        let field = this.fields[i - 1];

        this.fields.splice(i - 1, 1);
        this.fields.splice(i, 0, field);

        if (this.fields[i - 1].is_advanced != 1) {
            break;
        }
    }

    this.saveFieldsOrder();
}
```

---

## Сохранение порядка

```javascript
saveFieldsOrder() {
    let order = this.fields.map(
        field => field.alias
    );

    localStorage.setItem(
        this.table_code + '.fields.order',
        order.join(',')
    );
}
```

---

# Архивные записи

Архив загружается через отдельный query code:

```javascript
let q_opt =
    new QueryOptions(this.table_code + '$archive');

q_opt.param1 = item.initial_req_uuid;
```

Загрузка:

```javascript
this.dbQueryService.getQuery(q_opt)
    .pipe(first())
    .subscribe(table => {
        if (table && table.items) {
            for (let arch of table.items) {
                this.archives.push(arch);
            }
        }
    });
```

---

# Каталог методов

| Метод | Назначение |
|---|---|
| `ngOnInit()` | запуск страницы |
| `ngOnDestroy()` | отписка от route subscriptions |
| `restartAll()` | полная инициализация |
| `setQueryOptions()` | сбор QueryOptions |
| `update()` | обновление данных |
| `getTableFields()` | получение метаданных колонок |
| `getTableSort()` | загрузка строк |
| `getTools()` | кнопки процессов сущности |
| `getActsMany()` | массовые действия |
| `setActManyMenu()` | контекстное меню |
| `doAct()` | запуск массового процесса |
| `setChecked()` | выбор строки |
| `setCheckedAll()` | выбрать все |
| `confirmDeleteChecked()` | подтверждение удаления |
| `deleteChecked()` | удаление записей |
| `changePage()` | переключение страницы |
| `changePerPage()` | изменение размера страницы |
| `add()` | создание записи |
| `sortByField()` | сортировка |
| `toggleField()` | скрыть/показать колонку |
| `addRemoveField()` | скрыть/показать колонку |
| `chooseFieldForFilter()` | реакция фильтра |
| `resetStaticFilter()` | сброс фильтра |
| `addNewStaticFilter()` | добавление фильтра |
| `deleteStaticFilter()` | удаление фильтра |
| `clearStaticFilter()` | очистка фильтров |
| `onSubmitStaticFilter()` | применение статических фильтров |
| `onSubmitFieldFilter()` | применение фильтров таблицы |
| `goToDetail()` | открытие детализации |
| `openInNewWindow()` | открытие новой вкладки |
| `openPagesAsModal()` | детализация в modal |
| `closeJitPage()` | закрытие встроенного JIT |
| `saveJitPage()` | сохранение JIT-формы |
| `print()` | печать/экспорт |
| `upFold()` | показать архив |
| `fieldOrderLeft()` | колонка влево |
| `fieldOrderRight()` | колонка вправо |
| `saveFieldsOrder()` | сохранить порядок колонок |
| `bindCallBack()` | callback после BP |
| `log()` | отладочный вывод |

---

# Типовой HTML-шаблон

```html
<div class="flex justify-content-between align-items-center my-3">

    <h3>{{ pageTitle }}</h3>

    <div>
        <p-button
            *ngFor="let tool of tools"
            (click)="appComponent.bpRun(tool.code,{},bindCallBack)"
            [label]="tool.title | translate"
        ></p-button>

        <p-button
            *ngFor="let act of acts_many"
            *ngIf="checked_rows.length"
            (click)="doAct(act)"
            [label]="act.title | translate"
            [badge]="checked_rows.length"
        ></p-button>
    </div>
</div>

<p-table
    #main_table
    [columns]="fields"
    [value]="filtered"
    dataKey="id"
>

    <ng-template pTemplate="header">

        <tr>
            <th style="width:48px">Выбор</th>

            <ng-container *ngFor="let field of fields">
                <th *ngIf="field.is_advanced != 1">
                    <a
                        href="javascript:void(0)"
                        (click)="sortByField(field)"
                    >
                        {{ field.title | translate }}
                    </a>
                </th>
            </ng-container>
        </tr>

        <tr>
            <th>
                <p-checkbox
                    [(ngModel)]="selected_all_rows"
                    (onChange)="setCheckedAll()"
                    [binary]="true"
                ></p-checkbox>
            </th>

            <ng-container *ngFor="let field of fields">
                <th *ngIf="field.is_advanced != 1">

                    <div [ngSwitch]="field._data_type_code">

                        <prime-select-multi
                            *ngSwitchCase="'reference'"
                            [(ngModel)]="field.value"
                            (ngModelChange)="onSubmitFieldFilter()"
                            [query-code]="field._def_sel_query_code"
                        ></prime-select-multi>

                        <p-triStateCheckbox
                            *ngSwitchCase="'boolean'"
                            [(ngModel)]="field.value"
                            (ngModelChange)="onSubmitFieldFilter()"
                        ></p-triStateCheckbox>

                        <input
                            *ngSwitchDefault
                            pInputText
                            [(ngModel)]="field.value"
                            (change)="onSubmitFieldFilter()"
                        />

                    </div>
                </th>
            </ng-container>
        </tr>

    </ng-template>

    <ng-template
        pTemplate="body"
        let-rowData
        let-rowIndex="rowIndex"
    >
        <tr>
            <td>
                <p-checkbox
                    [(ngModel)]="rowData.table_row_checked"
                    (onChange)="setChecked(rowData.table_row_checked,rowData.id)"
                    [binary]="true"
                ></p-checkbox>
            </td>

            <ng-container *ngFor="let field of fields">
                <td
                    *ngIf="field.is_advanced != 1"
                    (click)="goToDetail(rowData)"
                >
                    {{ rowData[field.alias] }}
                </td>
            </ng-container>
        </tr>
    </ng-template>

    <ng-template pTemplate="summary">
        <pagination
            [perpage-vars]="perpage_vars"
            [row-count]="table?.allCount"
            [page]="query_options.page"
            [perpage]="query_options.perpage"
            (pageChanged)="changePage($event)"
            (perPageChanged)="changePerPage($event)"
        ></pagination>
    </ng-template>

</p-table>
```

---

# Шаблон новой CRUD-страницы

```javascript
const vm = this;
const { QueryOptions } = Models;
const { first } = rxjs;
const DATA = data;

return class GenClass extends vm.constructor {

    entity_id = 'ENTITY_ID';
    entity_code = 'ENTITY_CODE';
    page_id = 'PAGE_ID';

    table_code = this.entity_code;
    query_code = this.entity_code;

    fields = [];
    filtered = [];
    tools = [];
    acts_many = [];
    static_filters = [];
    checked_rows = [];

    selected_all_rows = false;

    table;
    query_options = new QueryOptions();

    perpage = 15;
    perpage_vars = [];

    get only_jit_page() {
        return DATA && Object.keys(DATA).length > 0;
    }

    ngOnInit() {
        if (this.only_jit_page) {
            this.restartAll();
        }
    }

    restartAll() {
        if (data?.static_filters) {
            this.static_filters = data.static_filters;
        }

        this.getTableFields(this.table_code);
        this.getTools();
    }

    getTableFields(code) {
        let q = new QueryOptions(
            'get_filter_cols_by_code'
        );

        q.param1 = code;

        this.dbQueryService.getQuery(q)
            .pipe(first())
            .subscribe(resp => {
                this.fields = resp.items || [];
                this.update();
            });
    }

    update(params = {}) {
        this.setQueryOptions(params);
        this.getTableSort();
    }

    setQueryOptions(params) {
        this.query_options =
            new QueryOptions(
                data?.query_code ||
                this.query_code ||
                this.table_code
            );

        this.query_options.page =
            params.page || 1;

        this.query_options.perpage =
            params.perpage || this.perpage;
    }

    getTableSort() {
        this.dbQueryService
            .getQuery(this.query_options)
            .pipe(first())
            .subscribe(table => {
                this.table = table;
                this.filtered = table?.items || [];
                this.getActsMany();
            });
    }
}
```

---

# Типовые ошибки

## 1. Приоритет операторов в number filter

Исходная конструкция вида:

```javascript
if ((filt.from || filt.to) &&
    filt._data_type_code == 'double' ||
    filt._data_type_code == 'number')
```

фактически вычисляется как:

```text
(A && B) || C
```

Безопаснее:

```javascript
if (
    (filt.from || filt.to) &&
    (
        filt._data_type_code == 'double' ||
        filt._data_type_code == 'number'
    )
) {
    ...
}
```

---

## 2. Неявный `event`

Если метод использует:

```javascript
target: event.target
```

то лучше передавать событие явно:

```html
(click)="confirmDeleteChecked($event)"
```

```javascript
confirmDeleteChecked(event) {
    this.confirmationService.confirm({
        target: event.target,
        ...
    });
}
```

---

## 3. Дублирование ID в checked_rows

Лучше защититься:

```javascript
if (
    checked &&
    !this.checked_rows.includes(id)
) {
    this.checked_rows.push(id);
}
```

---

## 4. selected_all_rows и allCount

Если включить «выбрать все», текущая реализация реально выбирает только строки текущего `filtered`, а сравнивает количество с `table.allCount`.

Если нужна логика «вся база», ее следует реализовывать отдельно на backend/query уровне.

---

## 5. Форматирование значений изменяет модель

В `getTableSort()` форматирование выполняется прямо над значением:

```javascript
filt[field.alias] = helper.formatPrice(...)
```

После этого числовое значение превращается в отображаемую строку.

Для сложных CRUD-сценариев предпочтительнее форматировать только в HTML через pipe или отдельное display-поле.

---

## 6. JIT и Router работают по-разному

Обычная страница:

```text
router.navigate()
route.queryParams
```

JIT:

```text
DATA/data
update(params)
```

Поэтому почти каждый метод изменения фильтров и страницы должен учитывать `only_jit_page`.

---

# Рекомендуемая структура CRUD-страницы

```text
1. Constants / entity config
2. Page state
3. JIT getters
4. Angular lifecycle
5. Initialization
6. QueryOptions
7. Data loading
8. Metadata loading
9. Filters
10. Selection
11. CRUD
12. Business processes
13. Navigation
14. JIT/modal
15. Table settings
16. Helpers
```

---

# Checklist

Перед публикацией новой CRUD-страницы проверить:

- [ ] указан правильный `entity_id`;
- [ ] указан правильный `entity_code`;
- [ ] указан правильный `page_id`;
- [ ] задан `table_code`;
- [ ] задан `query_code`;
- [ ] `get_filter_cols_by_code` возвращает поля;
- [ ] `fields` содержит `_data_type_code`;
- [ ] reference-поля содержат `_def_sel_query_code`;
- [ ] `restartAll()` вызывает `getTableFields()`;
- [ ] `getTableFields()` вызывает `update()`;
- [ ] `update()` формирует `QueryOptions`;
- [ ] `getTableSort()` получает строки;
- [ ] `table.items` безопасно преобразуется в `[]`;
- [ ] работает сортировка;
- [ ] работают строковые фильтры;
- [ ] работают reference-фильтры;
- [ ] работают boolean-фильтры;
- [ ] работают диапазоны дат;
- [ ] работает пагинация;
- [ ] работает `perpage`;
- [ ] работают checkbox строк;
- [ ] работает «выбрать все»;
- [ ] загружаются `acts_many`;
- [ ] загружаются `tools`;
- [ ] `bpRun` вызывает callback обновления;
- [ ] работает переход на detail;
- [ ] проверен `angular_detail_page_url$`;
- [ ] работает JIT-режим;
- [ ] работает modal detail;
- [ ] работает сохранение JIT-формы;
- [ ] работает `/update_v_1_1` insert;
- [ ] работает `/update_v_1_1` delete;
- [ ] ошибки API показываются пользователю;
- [ ] порядок колонок сохраняется в `localStorage`;
- [ ] фильтры сохраняются только там, где это необходимо;
- [ ] subscriptions очищаются в `ngOnDestroy()`;
- [ ] нет неявного глобального `event`;
- [ ] проверены приоритеты `&&` / `||`;

---

# Короткая формула DamuBPM CRUD

```text
Entity metadata
     +
QueryOptions
     +
dbQueryService
     +
PrimeNG table
     +
update_v_1_1
     +
bpRun
     +
JIT data
     =
DamuBPM CRUD Page
```

---

# Главный принцип

Не привязывать CRUD-страницу к конкретному набору HTML-полей.

Лучший подход DamuBPM:

```text
метаданные сущности
        ↓
fields[]
        ↓
динамический Angular template
        ↓
QueryOptions
        ↓
универсальная CRUD-страница
```

Так одна и та же архитектура может использоваться для десятков сущностей, меняя в основном:

```javascript
entity_id
entity_code
page_id
query_code
```

и, при необходимости, добавляя бизнес-специфичные действия.

---

[← Главная](index.html)

