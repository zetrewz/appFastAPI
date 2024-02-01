from fastapi import HTTPException, status


class MainException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistException(MainException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь с такими данными уже существует"


class UserDoesNotExist(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Пользователь с такими данными не существует"


class DisabledUserException(MainException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Пользователь не доступен"


class IncorrectEmailOrPasswordException(MainException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Неверная почта или пароль"


class TokenAbsentException(MainException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен доступа отсутствует"


class TokenExpiredException(MainException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Время сессии истекло, залогиньтесь снова"


class IncorrectTokenFormatException(MainException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный токен доступа"


class ObjectDoesNotExist(MainException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "Такого объекта не существует"


class MethodNotAllowedForWorker(MainException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Данный метод только для работодателей"


class MethodNotAllowedForEmployer(MainException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Данный метод только для работников"


class ApplicationAlreadyExistsException(MainException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = "Вы уже откликались на данную вакансию"
