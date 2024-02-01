from fastapi import APIRouter, Response, Depends

from exceptions import UserAlreadyExistException, DisabledUserException
from users.auth import get_password_hash, authenticate, create_access_token
from users.dao import UserDAO
from users.dependencies import get_current_user
from users.models import User

from users.schemas import SUserRegister, SUser, SUserLogin
from users.utils import UserTypeChoices

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)


@router.post("/register/", summary="Регистрация")
async def register(
        response: Response,
        user_data: SUserRegister,
        user_type: UserTypeChoices,
) -> SUser:
    existing_user = await UserDAO.get_object_or_none(email=user_data.email)
    if existing_user:
        raise UserAlreadyExistException

    hashed_password = get_password_hash(user_data.password)
    new_user = await UserDAO.add(
        email=user_data.email,
        hashed_password=hashed_password,
        user_type=user_type,
    )

    access_token = create_access_token(response, {"sub": str(new_user.id)})
    return new_user


@router.post("/login/", summary="Войти")
async def login(response: Response, user_data: SUserLogin) -> dict:
    user = await authenticate(user_data)
    if not user.is_active:
        raise DisabledUserException

    access_token = create_access_token(response, {"sub": str(user.id)})
    return {"access_token": access_token}


@router.get("/logout/", summary="Выйти")
async def logout(response: Response) -> str:
    response.delete_cookie("access_token")
    return "Ты вышел, congratulations"


@router.get("/users/", summary="Получить всех юзеров")
async def get_users() -> list[SUser]:
    return await UserDAO.get_objects()


@router.get("/user/", summary="Получить текущего юзера")
async def get_user(user: User = Depends(get_current_user)) -> SUser:
    return user
