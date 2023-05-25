## Описание

Проект представляет собой API для приложения [Yatube](git@github.com:Safarrush/hw05_final.git) - социальной сети для чтения и публикации постов и комментариев к ним.

Ключевые моменты:

Применены вьюсеты.

Для аутентификации использованы JWT-токены.

У неаутентифицированных пользователей есть доступ к API только для чтения. Исключение — эндпоинт /follow/, доступ к нему предоставляется только аутентифицированным пользователям. 

Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

## Технологии
Python 3.7, Django 2.2, Django REST Framework 3.12, Pillow 8.3, Requests 2.26, Thumbnail 12.7

## Установка

### 1) Склонировать репозиторий:
Клонировать репозиторий (git clone) и перейти в него в командной строке (cd)

### 2) Создать и активировать виртуальное окружение для проекта
```
python3 -m venv venv
source venv/scripts/activate
```
### 3) Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
python3 pip install -r requirements.txt
```
### 4) Сделать миграции
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### 5) Запустить сервер
```
python3 manage.py runserver
```
## Примеры

Для доступа к API необходимо получить JWT-токен: выполнить POST-запрос localhost:8000/api/v1/token/, передав поля username и password.

При дальнейшей отправке запросов токен передается в заголовке Authorization: Bearer <токен>

Примеры обращения к методам и ответов:

### 1) 

/api/v1/posts/ (GET, POST) 

ответ API на GET-запрос: 

 
```
{ 
  "count": 123, 
  "next": "http://api.example.org/accounts/?offset=400&limit=100", 
  "previous": "http://api.example.org/accounts/?offset=200&limit=100", 
  "results": [ 
    { 
      "id": 0, 
      "author": "string", 
      "text": "string", 
      "pub_date": "2021-10-14T20:41:29.648Z", 
      "image": "string", 
      "group": 0 
    } 
  ] 
} 
```

POST-запрос: 
 
```
{ 
  "text": "string", 
  "image": "string", 
  "group": 0 
} 
```
ответ API на POST-запрос: 
 
```
{ 
  "id": 0, 
  "author": "string", 
  "text": "string", 
  "pub_date": "2019-08-24T14:15:22Z", 
  "image": "string", 
  "group": 0 
} 
```
### 2) 

/api/v1/groups/ (GET) 

ответ API на GET-запрос: 
 
```
[ 
  { 
    "id": 0, 
    "title": "string", 
    "slug": "string", 
    "description": "string" 
  } 
] 
```
Автор:
----------
Рушан - tg @safa_ru
