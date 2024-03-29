from abc import ABC, abstractmethod

from fastapi import Depends

from src.auth.jwt import JWTInteractor


class TokenAuthEncoderProto(ABC):

    @abstractmethod
    def __init__(self, jwt_interactor: JWTInteractor = Depends()) -> None:
        ...

    @abstractmethod
    async def __call__(self, phone: str, admin: bool) -> str:
        ...
