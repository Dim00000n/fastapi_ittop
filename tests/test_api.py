from fastapi.testclient import TestClient

from main import app, users

client = TestClient(app)


def setup_function():
    users.clear()
    # Счетчик ID в main.py сбрасываем для независимости тестов
    import main
    main.next_user_id = 1


def test_create_user():
    response = client.post(
        "/users",
        json={"name": "Alex", "email": "alex@example.com", "age": 20},
    )
    assert response.status_code == 201
    assert response.json()["id"] == 1


def test_get_users():
    client.post("/users", json={"name": "Alex", "email": "alex@example.com", "age": 20})
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_user():
    client.post("/users", json={"name": "Alex", "email": "alex@example.com", "age": 20})
    response = client.put(
        "/users/1",
        json={"name": "Max", "email": "max@example.com", "age": 21},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Max"


def test_delete_user():
    client.post("/users", json={"name": "Alex", "email": "alex@example.com", "age": 20})
    response = client.delete("/users/1")
    assert response.status_code == 204
    assert client.get("/users/1").status_code == 404


def test_swagger_docs_open():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "swagger-ui" in response.text


def test_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404


def test_openapi_has_user_crud_routes():
    schema = client.get("/openapi.json").json()
    assert "post" in schema["paths"]["/users"]
    assert "put" in schema["paths"]["/users/{user_id}"]
    assert "delete" in schema["paths"]["/users/{user_id}"]
