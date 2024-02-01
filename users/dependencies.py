from fastapi import Request, Depends
from jose import jwt, JWTError

from config import settings
from exceptions import TokenAbsentException, TokenExpiredException, IncorrectTokenFormatException, UserDoesNotExist
from users.dao import UserDAO


def get_user_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException

    try:
        decoded_token = jwt.decode(
            token, settings.SECRET_KEY, settings.ALGORITHM
        )
    except jwt.ExpiredSignatureError:
        raise TokenExpiredException
    except JWTError:
        raise IncorrectTokenFormatException

    return decoded_token


async def get_current_user(token: dict = Depends(get_user_token)):
    user = await UserDAO.get_object_or_none(id=int(token.get("sub")))
    if user is None:
        raise UserDoesNotExist

    return user
