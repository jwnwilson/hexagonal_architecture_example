from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Dict

if TYPE_CHECKING:
    from app.domain.user_domain import UserDTO, UserCreateDTO


class UserDataAdapter(ABC):
    def __init__(self, config: Dict):
        raise NotImplementedError

    @abstractmethod
    def read(self, record_id: int) -> 'UserDTO':
        raise NotImplementedError

    @abstractmethod
    def create(self, user_data: 'UserCreateDTO') -> 'UserDTO':
        raise NotImplementedError