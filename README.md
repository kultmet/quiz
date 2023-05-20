# quiz
## This test task

## Getting started:
### Как начать?

Запускаем контейнеры с помощью docker-compose

```
docker-compose up -d
```

Делаем миграции

```
sudo docker-compose exec web alembic upgrade head
```

## Request example: 
##    method[POST] http://127.0.0.1:8008/quiz
В теле запроса, - колличество вопросов для викториты. 
```
{
  "questions_num": 1
}
```
Под капотом идет запрос к API https://jservice.io/api/random?count=1.
<code>"questions_num"</code> из тела запроса соответствует параметру <code>count</code> для https://jservice.io/api/random

## Response example
В ответе будет запись которая была созданна последней.

```
{
    "id": 53043,
    "question": "This sitcom was well into its first season when Jaleel White joined it as Steve Urkel",
    "answer": "<i>Family Matters</i>",
    "created_at": "2022-12-30T19:00:08.346000+00:00",
    "date_added": "2023-05-20T16:49:51.595678"
}
```