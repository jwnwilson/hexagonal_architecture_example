from typing import Optional
from uuid import UUID
from pydantic import BaseModel

from app.ports.user_ports import UserDataAdapter


class UserDTO(BaseModel):
    id: UUID
    name: Optional[str]
    address: Optional[str]


class UserCreateDTO(BaseModel):
    name: Optional[str]
    address: Optional[str]


class UserEntity:
    def __init__(self, db: UserDataAdapter):
        # Set DB adapter using dependency injection pattern
        # This adapter could be changed later
        self.db: UserDataAdapter = db

    def get_user(self, user_id: int) -> UserDTO:
        # user entity returns user data as DTO
        user_data: UserDTO = self.db.read(user_id)
        return user_data
    
    def create_user(self, user_data: UserCreateDTO) -> UserDTO:
        # Imagine this is complex calculation that is critical to the business
        if not user_data.name:
            user_data.name = 'Noel'
        if not user_data.address:
            user_data.address = 'London'
        # save output to unknown storage
        user_data: UserDTO = self.db.create(user_data)
        return user_data