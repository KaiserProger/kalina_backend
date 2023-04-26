from abc import ABC, abstractmethod
from app.domain.entities.user import User
from app.schemas.user import UserDTO
from .user_repository import UserRepositoryProto

from fastapi import Depends


class CabinetServiceProto(ABC):

    @abstractmethod
    def __init__(self, user_repo: UserRepositoryProto = Depends()) -> None:
        ...

    @abstractmethod
    async def get_user_cabinet(self, user: User) -> UserDTO:
        ...
