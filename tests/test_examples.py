import importlib

from fastapi.testclient import TestClient


def test_example_1_first_app():
    app = importlib.import_module("examples.01_first_app").app
    client = TestClient(app)
    assert client.get("/").json()["message"] == "Привет FastAPI"
    assert client.get("/page").status_code == 200


def test_example_2_request_methods():
    app = importlib.import_module("examples.02_requests").app
    client = TestClient(app)
    assert client.get("/users").status_code == 200
    assert client.post("/users").status_code == 200
    assert client.put("/users/5").json()["id"] == 5
    assert client.delete("/users/5").status_code == 200


def test_example_3_responses():
    app = importlib.import_module("examples.03_responses").app
    client = TestClient(app)
    assert client.get("/json").json()["message"] == "Ответ в формате JSON"
    assert client.get("/text").text == "Обычный текстовый ответ"
    assert "HTML" in client.get("/html").text


def test_example_4_file_download():
    app = importlib.import_module("examples.04_files").app
    client = TestClient(app)
    response = client.get("/download")
    assert response.status_code == 200
    assert "пример файла" in response.text


def test_example_5_path_parameters():
    app = importlib.import_module("examples.05_path_parameters").app
    client = TestClient(app)
    assert client.get("/users/15").json()["user_id"] == 15
    assert client.get("/users/admin").status_code == 200
