# Пример к статье 3 — Отправка ответа
# FastAPI умеет возвращать JSON, обычный текст и HTML

from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse

app = FastAPI()


@app.get("/json")
def json_answer():
    return JSONResponse(content={"message": "Ответ в формате JSON"})


@app.get("/text", response_class=PlainTextResponse)
def text_answer():
    return "Обычный текстовый ответ"


@app.get("/html", response_class=HTMLResponse)
def html_answer():
    return "<h2>Ответ в формате HTML</h2>"

# Запуск:
# uvicorn examples.03_responses:app --reload
