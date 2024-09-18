import os
from typing import Generator
from fastapi import FastAPI, Depends, HTTPException

from app.domain.user_domain import UserCreateDTO, UserDTO, UserEntity
from app.ports.user_ports import UserDataAdapter
from app.adaptor.out.db.user_sql import SQLAlchemyUserDataAdapter
from app.adaptor.out.file.user_file import FileUserDataAdapter

app = FastAPI(
    title="Hex Example API",
    version="0.1.0",
    description="",
    openapi_url="/openapi.json",
    docs_url="/",
)


def user_data_adaptor() -> Generator[UserDataAdapter, None, None]:
    if os.environ.get("DB_TYPE") == "SQL":
        yield SQLAlchemyUserDataAdapter()
    if os.environ.get("DB_TYPE") == "file":
        yield FileUserDataAdapter()


@app.post("/", include_in_schema=True)
def create_user(user_data: UserCreateDTO, user_data_adaptor: UserDataAdapter = Depends(user_data_adaptor)) -> UserDTO:
    user = UserEntity(user_data_adaptor).create_user(user_data)
    return user


@app.get("/{user_id}", include_in_schema=True)
def get_user(user_id: str, user_data_adaptor: UserDataAdapter = Depends(user_data_adaptor)) -> UserDTO:
    try:
        user = UserEntity(user_data_adaptor).get_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user
