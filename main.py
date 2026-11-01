from fastapi import FastAPI, HTTPException, Path, Response, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="Users API",
    description="Учебный проект по первым пяти статьям FastAPI на Metanit",
    version="1.0.0",
    swagger_ui_parameters={
        "syntaxHighlight": {"theme": "obsidian"},
        "displayRequestDuration": True,
        "filter": True,
    },
)


class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=50, description="Имя пользователя")
    email: str = Field(min_length=5, max_length=100, description="Почта пользователя")
    age: int = Field(ge=1, le=120, description="Возраст пользователя")


class UserUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: str = Field(min_length=5, max_length=100)
    age: int = Field(ge=1, le=120)


class User(BaseModel):
    id: int
    name: str
    email: str
    age: int


# Пока храним пользователей в словаре
# После перезапуска приложения данные сбросятся
users: dict[int, User] = {}
next_user_id = 1


@app.get("/", tags=["Главная"])
def home():
    return {"message": "Users API работает", "docs": "/docs"}


@app.post(
    "/users",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    tags=["Пользователи"],
    summary="Создать пользователя",
)
def create_user(user_data: UserCreate):
    global next_user_id

    user = User(id=next_user_id, **user_data.model_dump())
    users[next_user_id] = user
    next_user_id += 1
    return user


@app.get(
    "/users",
    response_model=list[User],
    tags=["Пользователи"],
    summary="Получить всех пользователей",
)
def get_users():
    return list(users.values())


@app.get(
    "/users/{user_id}",
    response_model=User,
    tags=["Пользователи"],
    summary="Получить пользователя по ID",
)
def get_user(user_id: int = Path(gt=0, description="ID пользователя")):
    user = users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return user


@app.put(
    "/users/{user_id}",
    response_model=User,
    tags=["Пользователи"],
    summary="Изменить пользователя",
)
def update_user(
    user_data: UserUpdate,
    user_id: int = Path(gt=0, description="ID пользователя"),
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    updated_user = User(id=user_id, **user_data.model_dump())
    users[user_id] = updated_user
    return updated_user


@app.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Пользователи"],
    summary="Удалить пользователя",
)
def delete_user(user_id: int = Path(gt=0, description="ID пользователя")):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    del users[user_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
