# Проект Api Yatube

## Описание
Проект Api Yatube представляет собой API для социальной платформы, где пользователи могут публиковать посты, оставлять комментарии, подписываться на других пользователей и т.д. API предоставляет возможности для создания, чтения, обновления и удаления данных, связанных с постами, комментариями, группами и подписчиками.

API разработан с использованием Django и Django REST Framework.

## Установка
1. Склонируйте репозиторий на локальную машину.
2. Установите виртуальное окружение и активируйте его.
3. Установите зависимости, указанные в файле requirements.txt.
4. Выполните миграции для создания базы данных.
5. Запустите локальный сервер.

Пример команд для установки:
```
git clone https://github.com/slavajet/api_final_yatube.git
cd api_yatube_final
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
## Примеры
### Пример запросов к API:

1. Создание нового поста:
POST /api/v1/posts/
Content-Type: application/json
Authorization: Token your_token
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
2. Получение списка постов:
GET /api/v1/posts/
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

3. Обновление поста:
PUT /api/v1/posts/{post_id}/
Content-Type: application/json
Authorization: Token your_token

payload
```
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
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
4. Удаление поста:
DELETE /api/v1/posts/{post_id}/
Authorization: Token your_token

5. Создание нового комментария к посту:
POST /api/v1/posts/{post_id}/comments/
Content-Type: application/json
Authorization: Token your_token

payload
```
{
  "text": "string"
}
```
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
6. Получение комментария к посту:
GET /api/v1/posts/{post_id}/comments/{id}/
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```
7. Подписка на пользователя:
POST /api/v1/follow/
Authorization: Token your_token


8. Получение списка подписчиков пользователя:
GET /api/v1/users/{user_id}/followers/
Authorization: Token your_token


**Примечание:** В примерах запросов замените `{post_id}`, `{user_id}` и `your_token` на соответствующие значения.

