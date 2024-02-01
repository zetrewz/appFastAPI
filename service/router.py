from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError

from exceptions import ApplicationAlreadyExistsException, MethodNotAllowedForEmployer
from service.dao import ApplicationDAO
from service.schemas import SApply, SApplication
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(
    prefix="/apply",
    tags=["Отклики"],
)


@router.post("/")
async def apply(
        user_data: SApply,
        user: User = Depends(get_current_user)
) -> SApplication:
    if user.user_type == "employer":
        raise MethodNotAllowedForEmployer
    try:
        return await ApplicationDAO.add(**user_data.model_dump())
    except IntegrityError:
        raise ApplicationAlreadyExistsException


@router.get("/list/r/{resume_id}/")
async def get_resume_applications(
        resume_id: int,
        user: User = Depends(get_current_user)
) -> list[SApplication]:
    return await ApplicationDAO.get_objects(resume_id=resume_id)


@router.get("/list/v/{vacancy_id}/")
async def get_vacancy_applications(
        vacancy_id: int,
        user: User = Depends(get_current_user)
) -> list[SApplication]:
    return await ApplicationDAO.get_objects(vacancy_id=vacancy_id)
