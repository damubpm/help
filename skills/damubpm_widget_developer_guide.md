# DamuBPM JIT Widget Developer Guide

Интерактивное руководство по разработке JIT-виджетов DamuBPM на Angular-логике и HTML.

> Основано на изученных JIT Logic и HTML-шаблонах DamuBPM.

---

## Содержание

1. [Архитектура JIT-виджета](#1-архитектура-jit-виджета)
2. [Минимальный виджет](#2-минимальный-виджет)
3. [Жизненный цикл](#3-жизненный-цикл)
4. [Запуск бизнес-процессов](#4-запуск-бизнес-процессов)
5. [REST API](#5-rest-api)
6. [QueryOptions](#6-queryoptions)
7. [Работа с данными](#7-работа-с-данными)
8. [Router](#8-router)
9. [Формы](#9-формы)
10. [Angular Template](#10-angular-template)
11. [RxJS](#11-rxjs)
12. [WebSocket](#12-websocket)
13. [Runtime API](#13-runtime-api)
14. [Безопасность](#14-безопасность)
15. [Готовый шаблон виджета](#15-готовый-шаблон-виджета)
16. [Правила разработки](#16-правила-разработки)

---

# 1. Архитектура JIT-виджета

DamuBPM JIT Widget состоит минимум из двух частей:

1. **Logic / JavaScript**
2. **HTML Template**

Ключевой принцип JIT:

```javascript
const vm = this;

const { first } = rxjs;
const { forkJoin } = rx;
const { map, take } = rxjs;
const { QueryOptions } = Models;
const { Validators } = forms;

return class GenClass extends vm.constructor {

    ngOnInit() {
    }

}
```

Главная конструкция:

```javascript
return class GenClass extends vm.constructor
```

JIT-класс не создаёт новый Angular Component через `@Component`.

Он расширяет уже подготовленный DamuBPM runtime-компонент и получает доступ к сервисам платформы через `this`.

Упрощённая архитектура:

```text
DamuBPM Angular Application
        |
        v
     JIT Engine
        |
        v
return class GenClass
    extends vm.constructor
        |
        v
 Angular Template
        |
        v
   Widget UI
```

В runtime доступны объекты вроде:

```text
appComponent
dbQueryService
accountService
router
route
formBuilder
websocketService
notificationService
alertService
scriptsService
Models
rx
rxjs
forms
uuid
```

---

# 2. Минимальный виджет

## Logic

```javascript
const vm = this;

const { first } = rxjs;
const { QueryOptions } = Models;

return class GenClass extends vm.constructor {

    loaded = false;
    loading = false;
    items = [];

    ngOnInit() {
        this.loadData();
    }

    loadData() {

        this.loading = true;

        const opt = new QueryOptions('users');

        opt.page = 1;
        opt.perpage = 20;

        this.dbQueryService.getQuery(opt)
            .pipe(first())
            .subscribe(resp => {

                this.items = resp.items || [];
                this.loading = false;

            });
    }

    ngAfterViewInit() {
        this.loaded = true;
    }

}
```

## HTML

```html
<div *ngIf="loaded">

    <h2>Пользователи</h2>

    <div *ngIf="loading">
        Загрузка...
    </div>

    <div *ngFor="let item of items">
        {{ item.title }}
    </div>

</div>
```

---

# 3. Жизненный цикл

## ngOnInit()

Используется для:

- инициализации состояния;
- создания форм;
- загрузки данных;
- создания подписок;
- чтения параметров URL;
- чтения `localStorage`.

```javascript
ngOnInit() {

    this.loadData();

}
```

---

## ngAfterViewInit()

DOM Angular уже создан.

```javascript
ngAfterViewInit() {

    this.loaded = true;

}
```

Подходит для:

- работы с DOM;
- canvas;
- сторонних JS-библиотек;
- поиска элементов;
- установки `loaded`.

---

## ngAfterViewChecked()

```javascript
ngAfterViewChecked() {

}
```

Вызывается часто.

Использовать только при необходимости.

---

## ngOnDestroy()

Используется для освобождения ресурсов:

```javascript
ngOnDestroy() {

    if (this.wsSub) {
        this.wsSub.unsubscribe();
    }

    if (this.timerSub) {
        this.timerSub.unsubscribe();
    }

}
```

Особенно важно очищать:

```text
rx.interval
rx.fromEvent
websocket subscriptions
router subscriptions
route.params
route.queryParams
```

---

# 4. Запуск бизнес-процессов

Основной метод:

```javascript
this.appComponent.bpRun()
```

Типовая форма:

```javascript
this.appComponent.bpRun(
    processCode,
    parameters,
    callback
);
```

Пример:

```javascript
this.appComponent.bpRun(
    'create_document',
    {
        title: this.title,
        amount: this.amount
    },
    data => {

        console.log(data);

    }
);
```

Пример из AI-виджета:

```javascript
this.appComponent.bpRun(
    'ollama_send',
    {
        txt: text,
        dialog_id: this.dialog_id
    },
    data => this.sendCallBack(data)
);
```

Рекомендуемый подход:

```text
Widget UI
   |
   v
appComponent.bpRun()
   |
   v
DamuBPM Business Process
```

Сложную серверную бизнес-логику лучше оставлять в BP.

---

# 5. REST API

## GET

```javascript
this.dbQueryService.restapiGet(
    service,
    params
)
```

Пример:

```javascript
this.dbQueryService.restapiGet(
    'alerts',
    {}
)
.pipe(first())
.subscribe(resp => {

    this.notifications = resp.alerts || [];

});
```

---

## POST

```javascript
this.dbQueryService.restapiPost(
    service,
    data
)
```

Пример:

```javascript
this.dbQueryService.restapiPost(
    'notifications_set_is_closed',
    {
        id: item.id
    }
)
.pipe(first())
.subscribe(resp => {

    console.log(resp);

});
```

---

# 6. QueryOptions

Для работы со списками сущностей используется:

```javascript
Models.QueryOptions
```

Подключение:

```javascript
const { QueryOptions } = Models;
```

Пример:

```javascript
const opt = new QueryOptions('users');

opt.page = 1;
opt.perpage = 20;

opt.flt = {
    title: this.searchText
};

this.dbQueryService.getQuery(opt)
    .subscribe(resp => {

        this.users = resp.items || [];

    });
```

---

## Параллельные запросы

```javascript
const { forkJoin } = rx;
```

Пример:

```javascript
forkJoin(

    this.dbQueryService.getQuery(optUsers),
    this.dbQueryService.getQuery(optPages),
    this.dbQueryService.getQuery(optWidgets)

)
.subscribe(resp => {

    this.users = resp[0].items || [];
    this.pages = resp[1].items || [];
    this.widgets = resp[2].items || [];

});
```

Используйте `forkJoin`, если запросы не зависят друг от друга.

---

# 7. Работа с данными

## getQuery()

Получение списка:

```javascript
this.dbQueryService.getQuery(opt)
```

---

## getDetail()

Получение записи:

```javascript
this.dbQueryService.getDetail(
    'users',
    id
)
.pipe(
    map(resp => resp['users'])
)
.subscribe(users => {

    this.user = users?.[0] || null;

});
```

---

## updateTable()

Обновление записей:

```javascript
this.dbQueryService.updateTable(
    'notifications',
    [{
        id: notification.id,
        is_closed: '1'
    }]
)
.subscribe(resp => {

    if (resp.error == 0) {

        notification.is_closed = 1;

    }

});
```

Можно передавать несколько строк:

```javascript
this.dbQueryService.updateTable(
    'orders',
    [
        {
            id: 100,
            status: 'done'
        },
        {
            id: 101,
            status: 'done'
        }
    ]
);
```

---

# 8. Router

## Переход программно

```javascript
this.router.navigate([
    '/users'
]);
```

Пример:

```javascript
openUser(user) {

    this.router.navigate([
        '/usersdetails/' + user.id
    ]);

}
```

---

## routerLink

```html
<a [routerLink]="'/users/' + user.id">
    {{ user.title }}
</a>
```

---

## Query Params

```html
<a
    [routerLink]="'/users'"
    [queryParams]="{
        dep_id: depId
    }">
    Пользователи
</a>
```

---

## Чтение queryParams

```javascript
this.route.queryParams
    .pipe(take(1))
    .subscribe(params => {

        if (params.search) {

            this.searchText = params.search;

        }

    });
```

---

## Route Params

```javascript
this.route.params
    .subscribe(params => {

        console.log(params.id);

    });
```

---

# 9. Формы

## Reactive Forms

Подключение:

```javascript
const { Validators } = forms;
```

Создание:

```javascript
this.form = this.formBuilder.group({

    title: [
        '',
        Validators.required
    ],

    code: ['']

});
```

HTML:

```html
<form
    [formGroup]="form"
    (submit)="save()">

    <input
        pInputText
        formControlName="title">

    <button type="submit">
        Сохранить
    </button>

</form>
```

---

## ngModel

```html
<input
    [(ngModel)]="searchText">
```

Textarea:

```html
<textarea
    [(ngModel)]="inputText"
    name="prompt"
    (keydown)="onKeydown($event)">
</textarea>
```

---

# 10. Angular Template

Подтверждённые конструкции.

## ngIf

```html
<div *ngIf="loaded">
</div>
```

---

## ngFor

```html
<div *ngFor="let item of items">

    {{ item.title }}

</div>
```

С индексом:

```html
<div
    *ngFor="
        let item of items;
        index as index
    ">
</div>
```

---

## Интерполяция

```html
{{ item.title }}
```

```html
{{ inputText?.length || 0 }}
```

---

## События

```html
(click)="save()"
```

```html
(submit)="send($event)"
```

```html
(keydown)="onKeydown($event)"
```

```html
(blur)="onBlur()"
```

---

## Property Binding

```html
[src]="imageUrl"
```

```html
[class]="itemClass"
```

```html
[href]="item.url"
```

```html
[innerHTML]="html"
```

---

## ngClass

```html
<div
    [ngClass]="{
        active: selected,
        disabled: loading
    }">
</div>
```

---

# ng-template

```html
<ng-template
    #itemTemplate
    let-item="$implicit">

    <div>
        {{ item.title }}
    </div>

</ng-template>
```

Использование:

```html
<ng-container
    [ngTemplateOutlet]="itemTemplate"
    [ngTemplateOutletContext]="{
        $implicit: item
    }">
</ng-container>
```

Это подходит для:

- деревьев;
- рекурсивных меню;
- карточек;
- универсальных шаблонов.

---

# Template Reference

```html
<input #searchInput>
```

```html
<button
    (click)="searchInput.focus()">

    Focus

</button>
```

---

# 11. RxJS

Подтверждены:

```text
rxjs.first
rxjs.map
rxjs.take

rx.forkJoin
rx.interval
rx.fromEvent
```

---

## first()

```javascript
observable
    .pipe(first())
    .subscribe(...);
```

---

## take()

```javascript
observable
    .pipe(take(1))
    .subscribe(...);
```

---

## map()

```javascript
observable
    .pipe(
        map(resp => resp.users)
    )
    .subscribe(...);
```

---

## interval()

```javascript
this.timerSub = rx.interval(
    60000
)
.subscribe(() => {

    this.refresh();

});
```

---

## fromEvent()

```javascript
this.mouseSub = rx.fromEvent(
    document,
    'mousemove'
)
.subscribe(event => {

    console.log(event);

});
```

---

# 12. WebSocket

Доступно:

```javascript
this.websocketService.messages
```

Пример:

```javascript
this.wsSub =
    this.websocketService.messages
        .subscribe(msg => {

            if (
                msg.data &&
                msg.type === 'url_notification'
            ) {

                this.refresh();

            }

        });
```

Обязательно очищать:

```javascript
ngOnDestroy() {

    if (this.wsSub) {
        this.wsSub.unsubscribe();
    }

}
```

---

## Browser Notification

```javascript
this.notificationService.create(
    'Уведомление!',
    {
        requireInteraction: true,
        body: 'Появились новые данные',
        icon: '/assets/img/peopleavatars/face_1.svg'
    }
)
.subscribe(result => {

    console.log(result);

});
```

---

# 13. Runtime API

## DamuBPM

```text
appComponent.bpRun()
appComponent.getGlobal()

appComponent.menu
appComponent.menu.top
appComponent.menu.middle
appComponent.menu.bottom
appComponent.menu.account
appComponent.menu.favorites

appComponent.params

appComponent.translateService
appComponent.translateService.getLangs()
appComponent.translateService.use()
appComponent.translateService.currentLang
```

---

## Database

```text
dbQueryService.restapiGet()
dbQueryService.restapiPost()
dbQueryService.getQuery()
dbQueryService.getDetail()
dbQueryService.updateTable()
```

---

## Account

```text
accountService.getSession()
accountService.logout()
```

---

## Navigation

```text
router.navigate()

route.params
route.queryParams
route.snapshot
```

---

## Forms

```text
formBuilder.group()

forms.Validators
Validators.required
```

---

## Notifications

```text
notificationService.create()

alertService.error()
alertService.info()
```

---

## WebSocket

```text
websocketService.messages
```

---

## Scripts

```text
scriptsService.loadUrl()
```

---

## Models

```text
Models.QueryOptions
Models.MenuItem.setMenu()
Models.MenuType
```

---

## RxJS

```text
rxjs.first
rxjs.map
rxjs.take

rx.forkJoin
rx.interval
rx.fromEvent
```

---

## Utilities

```text
uuid.v4()
```

---

# Browser API

Также можно использовать стандартный Browser API:

```text
fetch()
localStorage
document
window
location
setTimeout()
setInterval()
FormData
Web Crypto API
matchMedia()
```

---

# 14. Безопасность

## innerHTML

Осторожно:

```html
<div [innerHTML]="html"></div>
```

Если нужен обычный текст, предпочтительнее:

```html
{{ text }}
```

---

## eval

В runtime может использоваться:

```javascript
runEval(action) {

    return eval(action);

}
```

Но для новых виджетов лучше использовать явно определённые методы:

```html
(click)="myMethod()"
```

---

## Роли

UI:

```html
<button *ngIf="session_roles.admin">
    Администрирование
</button>
```

Это не заменяет серверную проверку прав.

---

## Подписки

Обязательно очищайте:

```text
interval
fromEvent
WebSocket
router
route
```

---

## CSS namespace

Хорошо:

```text
salesw-
docw-
aiw-
calendarw-
```

Плохо:

```text
.button
.card
.header
.item
```

---

## localStorage

Рекомендуемый формат:

```text
widget.<widget-code>.<key>
```

Например:

```javascript
localStorage.setItem(
    'widget.sales.period',
    this.period
);
```

---

# 15. Готовый шаблон виджета

## Logic

```javascript
const vm = this;

const { first, map, take } = rxjs;
const { forkJoin } = rx;
const { QueryOptions } = Models;
const { Validators } = forms;

return class GenClass extends vm.constructor {

    loaded = false;
    loading = false;

    items = [];

    form;

    ngOnInit() {

        this.form =
            this.formBuilder.group({

                search: ['']

            });

        this.loadData();

    }

    loadData() {

        this.loading = true;

        const opt =
            new QueryOptions(
                'users'
            );

        opt.page = 1;
        opt.perpage = 20;

        if (
            this.form.value.search
        ) {

            opt.flt = {

                title:
                    this.form.value.search

            };

        }

        this.dbQueryService
            .getQuery(opt)
            .pipe(first())
            .subscribe({

                next: resp => {

                    this.items =
                        resp.items || [];

                    this.loading = false;

                },

                error: err => {

                    this.loading = false;

                    this.alertService.error(
                        'Ошибка загрузки'
                    );

                }

            });

    }

    open(item) {

        this.router.navigate([
            '/usersdetails/' +
            item.id
        ]);

    }

    runProcess(item) {

        this.appComponent.bpRun(
            'my_process',
            {
                id: item.id
            },
            resp => {

                this.loadData();

            }
        );

    }

    ngAfterViewInit() {

        this.loaded = true;

    }

    ngOnDestroy() {

    }

}
```

---

## HTML

```html
<style>

.myw-root {
    padding: 20px;
}

.myw-toolbar {
    display: flex;
    gap: 10px;
    margin-bottom: 16px;
}

.myw-card {
    padding: 12px;
    border-bottom: 1px solid #ddd;
}

</style>


<div
    class="myw-root"
    *ngIf="loaded">

    <form
        class="myw-toolbar"
        [formGroup]="form"
        (submit)="loadData()">

        <input
            pInputText
            formControlName="search"
            placeholder="Поиск">

        <button type="submit">
            Найти
        </button>

    </form>


    <div *ngIf="loading">

        Загрузка...

    </div>


    <div
        class="myw-card"
        *ngFor="let item of items">

        <strong>

            {{ item.title }}

        </strong>

        <button
            type="button"
            (click)="open(item)">

            Открыть

        </button>

        <button
            type="button"
            (click)="runProcess(item)">

            Запустить BP

        </button>

    </div>

</div>
```

---

# 16. Правила разработки

## 1. Не создавать Angular Component вручную

Не нужно:

```typescript
@Component(...)
export class MyComponent {
}
```

Нужно:

```javascript
return class GenClass extends vm.constructor {
}
```

---

## 2. Хранить состояние в классе

```javascript
items = [];
loading = false;
selectedItem = null;
```

---

## 3. Использовать dbQueryService

Для REST:

```javascript
this.dbQueryService.restapiGet(...)
```

```javascript
this.dbQueryService.restapiPost(...)
```

Для сущностей:

```javascript
this.dbQueryService.getQuery(...)
```

```javascript
this.dbQueryService.getDetail(...)
```

```javascript
this.dbQueryService.updateTable(...)
```

---

## 4. Бизнес-логику запускать через BP

```javascript
this.appComponent.bpRun(...)
```

---

## 5. Использовать Angular Binding

Предпочтительнее:

```html
*ngIf
*ngFor
[(ngModel)]
[formGroup]
(click)
```

чем ручная работа через:

```javascript
document.querySelector()
```

---

## 6. Использовать DOM только при необходимости

Например:

- scroll;
- canvas;
- сторонняя библиотека;
- размеры DOM;
- специальные browser API.

---

## 7. Обрабатывать loading

```javascript
loading = false;
```

До запроса:

```javascript
this.loading = true;
```

После ответа:

```javascript
this.loading = false;
```

HTML:

```html
<div *ngIf="loading">
    Загрузка...
</div>
```

---

## 8. Обрабатывать ошибки

```javascript
error: err => {

    this.loading = false;

    this.alertService.error(
        'Ошибка загрузки'
    );

}
```

---

## 9. Освобождать ресурсы

```javascript
ngOnDestroy() {

    if (this.wsSub) {
        this.wsSub.unsubscribe();
    }

}
```

---

# Типовая структура JIT-класса

```javascript
return class GenClass extends vm.constructor {

    // STATE

    loading = false;
    items = [];
    selectedItem = null;


    // GETTERS

    get hasItems() {

        return this.items.length > 0;

    }


    // INIT

    ngOnInit() {

        this.load();

    }


    // DATA

    load() {

    }


    // EVENTS

    onSelect(item) {

        this.selectedItem = item;

    }


    // BUSINESS PROCESS

    run(item) {

    }


    // NAVIGATION

    open(item) {

    }


    // HELPERS

    formatTitle(item) {

        return item.title || '-';

    }


    // DESTROY

    ngOnDestroy() {

    }

}
```

---

# Самые важные методы

Для большинства JIT-виджетов достаточно знать:

```javascript
this.dbQueryService.getQuery()

this.dbQueryService.getDetail()

this.dbQueryService.updateTable()

this.dbQueryService.restapiGet()

this.dbQueryService.restapiPost()

this.appComponent.bpRun()

this.router.navigate()

this.formBuilder.group()

this.websocketService.messages.subscribe()

this.notificationService.create()

this.alertService.error()

this.scriptsService.loadUrl()

uuid.v4()
```

Основные Angular-конструкции:

```text
{{ expression }}

*ngIf
*ngFor

(click)
(submit)
(keydown)
(blur)

[(ngModel)]

[formGroup]
formControlName

[routerLink]
[queryParams]

[ngClass]
[class]
[src]
[href]
[innerHTML]

ng-template
ng-container
ngTemplateOutlet
ngTemplateOutletContext
```

---

# Итог

DamuBPM JIT Widget можно рассматривать как:

```text
DamuBPM Runtime
     +
Dynamic JavaScript Class
     +
Angular HTML Template
     =
DamuBPM Widget
```

Этого механизма достаточно для разработки:

- CRUD-интерфейсов;
- Dashboard;
- поисковых форм;
- административных панелей;
- карточек;
- таблиц;
- AI-виджетов;
- WebSocket-интерфейсов;
- уведомлений;
- BP Launcher;
- динамического меню;
- мобильных интерфейсов.

Максимально используй уже существующие стили из папки /css
