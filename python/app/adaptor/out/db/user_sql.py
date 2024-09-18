from typing import TYPE_CHECKING, Dict, Optional
from sqlalchemy.sql import text
from app.ports.user_ports import UserDataAdapter
from app.domain.user_domain import UserCreateDTO, UserDTO
from .session import session, engine
from .models import User

if TYPE_CHECKING:
    from app.domain.user_domain import UserDTO


class SQLAlchemyUserDataAdapter(UserDataAdapter):
    def __init__(self, config: Optional[Dict] = None):
        self.config = config
        self.session = session

    def read(self, record_id: int) -> 'UserDTO':
        user_model = self.session.query(User).filter(User.id == record_id).first()
        if not user_model:
            raise ValueError(f"User with id {record_id} not found")
        return UserDTO(
            id=user_model.id,
            name=user_model.name,
            address=user_model.address
        )
    
    def create(self, user_data: UserCreateDTO) -> UserDTO:
        user_model = User(**user_data.model_dump())
        self.session.add(user_model)
        self.session.commit()
        return UserDTO(
            id=user_model.id,
            name=user_model.name,
            address=user_model.address
        )

