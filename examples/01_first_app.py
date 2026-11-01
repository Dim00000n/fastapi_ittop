# Пример к статье 1 — Что такое FastAPI
# Создаем приложение и первый адрес

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Привет FastAPI"}


@app.get("/page", response_class=HTMLResponse)
def page():
    return "<h1>Моя первая страница на FastAPI</h1>"

# Запуск из папки проекта:
# uvicorn examples.01_first_app:app --reload
