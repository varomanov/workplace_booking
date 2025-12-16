## Основные команды
1. Создать миграцию
```
alembic revision --autogenerate -m "message"
```

2. Обновить объекты БД до последней версии
```
alembic upgrade heads
```

3. Удалить последнюю миграцию из БД
```
alembic downgrade -1
```

4. Удаление миграции из проекта
```
Вручную удалить версии-файлы из /migrations/versions/
```