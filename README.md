# quiz
This test task

## Getting started:
### Как начать?

Running containers with docker-compose | Запускаем контейнеры с помощью docker-compose

```
docker-compose up -d
```

Making migrations | Делаем миграции

```
sudo docker-compose exec web alembic upgrade head
```

## Request example: 
method[POST] http://127.0.0.1:8008/quiz


In the body of the request, the number of questions for the quiz. | В теле запроса, - колличество вопросов для викториты. 
```
{
  "questions_num": 1
}
```
Под капотом идет запрос к API https://jservice.io/api/random?count=1.


<code>"questions_num"</code> from the request body matches the parameter <code>count</code> для https://jservice.io/api/random

<code>"questions_num"</code> из тела запроса соответствует параметру <code>count</code> для https://jservice.io/api/random

## Response example

The response will be the record that was created last. | В ответе будет запись которая была созданна последней.

```
{
    "id": 53043,
    "question": "This sitcom was well into its first season when Jaleel White joined it as Steve Urkel",
    "answer": "<i>Family Matters</i>",
    "created_at": "2022-12-30T19:00:08.346000+00:00",
    "date_added": "2023-05-20T16:49:51.595678"
}
```

if the database is empty then /quiz will return an empty object | Если база данных будет пуста то /quiz вернет пустой объект.

```
{}
```

Bye! Пока!
