# Пример к статье 2 — Класс FastAPI и обработка запроса
# Здесь показаны основные HTTP-методы

from fastapi import FastAPI

app = FastAPI()


@app.get("/users")
def get_users():
    return {"action": "Получение списка пользователей"}


@app.post("/users")
def create_user():
    return {"action": "Создание пользователя"}


@app.put("/users/{user_id}")
def update_user(user_id: int):
    return {"action": "Изменение пользователя", "id": user_id}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"action": "Удаление пользователя", "id": user_id}

# Запуск:
# uvicorn examples.02_requests:app --reload
