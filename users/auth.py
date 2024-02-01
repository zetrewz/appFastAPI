from datetime import datetime, timedelta

from fastapi import Response
from jose import jwt
from passlib.context import CryptContext

from config import settings
from exceptions import UserDoesNotExist
from users.dao import UserDAO
from users.models import User
from users.schemas import SUserLogin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(response: Response, data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=1)
    to_encode["exp"] = expire
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, settings.ALGORITHM
    )
    response.set_cookie("access_token", encoded_jwt, httponly=True, max_age=60 * 60 * 24)
    return encoded_jwt


async def authenticate(user_data: SUserLogin) -> User:
    user = await UserDAO.get_object_or_none(email=user_data.email)
    if not user or not verify_password(user_data.password, user.hashed_password):
        raise UserDoesNotExist
    return user
