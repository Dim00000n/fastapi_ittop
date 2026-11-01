# Пример к статье 4 — Отправка файлов с сервера
# FileResponse возвращает файл пользователю

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()
FILE_PATH = Path(__file__).parent / "public" / "example.txt"


@app.get("/download")
def download_file():
    return FileResponse(
        path=FILE_PATH,
        filename="example.txt",
        media_type="application/octet-stream",
    )

# Запуск:
# uvicorn examples.04_files:app --reload
# Открой /download чтобы скачать файл
