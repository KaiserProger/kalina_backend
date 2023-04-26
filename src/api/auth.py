from fastapi import APIRouter, Depends

from app.auth.auth import PhoneAuthInteractor

from app.schemas.user import RegisterDTO, SignDTO, VerifyDTO


common_router = APIRouter()


@common_router.get("/landing")
async def landing():
    return [{}]


@common_router.post("/authorize", responses={
    422: {"description": "Invalid phone number"},
    404: {"description": "No user exists, code sent as int"},
    200: {"description": "Success, code has been sent as int"}
})
async def authorize(dto: SignDTO,
                    interactor: PhoneAuthInteractor = Depends()):
    return await interactor.add_entry(dto.phone)


@common_router.post("/authorize/confirm", responses={
    400: {"description": "Invalid code"},
    200: {"description": "Confirmed, sending token"},
    404: {"description": "User with phone doesn't exist, go to /authorize/finish"},
})
async def confirm_auth(dto: VerifyDTO,
                       interactor: PhoneAuthInteractor = Depends()) -> str:
    return await interactor.confirm(dto.phone, dto.code)


@common_router.post("/authorize/finish", responses={
    200: {"description": "Ok, take token"},
})
async def finish_register(dto: RegisterDTO,
                          interactor: PhoneAuthInteractor = Depends()):
    return await interactor.finish_register(dto.phone, dto.name)
