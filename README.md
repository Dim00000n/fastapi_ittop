# Практика по FastAPI

Учебный проект по первым пяти статьям руководства FastAPI на Metanit. В папке examples лежат отдельные примеры к каждой статье. В main.py находится API для работы с пользователями.

## Что есть в проекте

1. Первое приложение и маршруты
2. Обработка GET / POST / PUT / DELETE запросов
3. Ответы JSON / обычный текст / HTML
4. Отправка файла через FileResponse
5. Параметры пути и их проверка
6. API пользователей: создание / просмотр / изменение / удаление
7. Swagger UI с настройками оформления

## Установка

Нужен Python 3.10 или новее.

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

## Запуск основного API

```bash
uvicorn main:app --reload
```

Открыть Swagger UI:

http://127.0.0.1:8000/docs

Там можно выполнять запросы и проверять API прямо из браузера.

## Ручки пользователей

| Метод | Адрес | Что делает |
|---|---|---|
| POST | /users | Создать пользователя |
| GET | /users | Получить всех пользователей |
| GET | /users/{user_id} | Получить одного пользователя |
| PUT | /users/{user_id} | Изменить пользователя |
| DELETE | /users/{user_id} | Удалить пользователя |

Пример тела для POST и PUT:

```json
{
  "name": "Alex",
  "email": "alex@example.com",
  "age": 20
}
```

## Запуск примеров из статей

Запускать из корневой папки проекта. Например:

```bash
uvicorn examples.01_first_app:app --reload
uvicorn examples.02_requests:app --reload
uvicorn examples.03_responses:app --reload
uvicorn examples.04_files:app --reload
uvicorn examples.05_path_parameters:app --reload
```

## Проверка

```bash
pytest -q
```

## Важно

В основном API пользователи пока хранятся в обычном словаре Python. Поэтому после перезапуска приложения список пользователей очищается. Это простой учебный вариант без базы данных.

## Материалы

- [Metanit — Что такое FastAPI](https://metanit.com/python/fastapi/1.1.php)
- [Metanit — Класс FastAPI и обработка запроса](https://metanit.com/python/fastapi/1.2.php)
- [Metanit — Отправка ответа](https://metanit.com/python/fastapi/1.3.php)
- [Metanit — Отправка файлов с сервера](https://metanit.com/python/fastapi/1.4.php)
- [Metanit — Параметры пути](https://metanit.com/python/fastapi/1.5.php)
- [FastAPI — Configure Swagger UI](https://fastapi.tiangolo.com/how-to/configure-swagger-ui/)
