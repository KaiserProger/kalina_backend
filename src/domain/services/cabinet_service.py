from app.domain.entities.user import User
from app.domain.interfaces.cabinet_service import CabinetServiceProto
from app.domain.interfaces.user_repository import UserRepositoryProto
from app.schemas.user import UserDTO


class CabinetService(CabinetServiceProto):
    def __init__(self, user_repo: UserRepositoryProto) -> None:
        self.user_repo = user_repo

    async def get_user_cabinet(self, user: User) -> UserDTO:
        return UserDTO.from_orm(await self.user_repo.
                                read_by_id(user.phone))  # type: ignore
