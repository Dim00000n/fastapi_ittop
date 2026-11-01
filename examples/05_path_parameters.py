# Пример к статье 5 — Параметры пути
# Значения из URL можно передавать прямо в функцию

from fastapi import FastAPI, Path

app = FastAPI()


# Более конкретный путь ставим выше общего
@app.get("/users/admin")
def admin():
    return {"message": "Это страница администратора"}


@app.get("/users/{user_id}")
def get_user(user_id: int = Path(gt=0, description="Положительный ID пользователя")):
    return {"user_id": user_id}

# Запуск:
# uvicorn examples.05_path_parameters:app --reload
