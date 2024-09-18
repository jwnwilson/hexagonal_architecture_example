import json
from typing import Dict, Optional, TYPE_CHECKING
import uuid
from app.ports.user_ports import UserDataAdapter
from app.domain.user_domain import UserDTO, UserCreateDTO


class FileUserDataAdapter(UserDataAdapter):
    def __init__(self, config: Optional[Dict] = None):
        self.config = config

    def read(self, record_id: int) -> 'UserDTO':
        with open(f"file_data/{record_id}.json", "r") as fp:
            user_data = json.load(fp)
        return UserDTO(id=record_id, **user_data)
    
    def create(self, user_data: 'UserCreateDTO') -> 'UserDTO':
        id = uuid.uuid4()
        with open(f"file_data/{id}.json", "w") as fp:
            json.dump(user_data.model_dump(), fp)
        return UserDTO(
            id=id,
            name=user_data.name,
            address=user_data.address
        )