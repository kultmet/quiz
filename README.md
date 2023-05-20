# quiz
## This test task

## Getting started:
### Как начать?

Локальный запуск
```
uvicorn main:app --reload
```

```
docker-compose up -d
```



для того чтоб прошли миграции, обязательно нужно в docker-compose  вывести порт, вот так вот
ports:
    - 5432:5432


миграции 
alembic revision --autogenerate -m 'initial'
alembic upgrade head
alembic downgrade base

Для того чтобы вавести обьект записи из базы данных, нужно воспользоваться Pydentic схемой вот так
"QuestionResponse.from_orm(obj)" а список сгенерировать через генератор списка


