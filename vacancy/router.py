from fastapi import APIRouter, Depends

from exceptions import MethodNotAllowedForWorker
from users.dependencies import get_current_user
from users.models import User
from vacancy.dao import VacancyDAO
from vacancy.schemas import SCreateUpdateVacancy, SVacancy

router = APIRouter(
    prefix="/vacancies",
    tags=["Вакансии"],
)


@router.post("/create/")
async def create_vacancy(
        user_data: SCreateUpdateVacancy,
        user: User = Depends(get_current_user)
) -> SVacancy:
    # if user.is_worker:
    #     raise MethodNotAllowedForWorker
    user_data = user_data.model_dump()
    user_data["user_id"] = user.id
    return await VacancyDAO.add(**user_data)


@router.get("/list/")
async def get_vacancies() -> list[SVacancy]:
    return await VacancyDAO.get_objects()


@router.get("/{vacancy_id}/")
async def get_vacancy(vacancy_id: int) -> None | SVacancy:
    return await VacancyDAO.get_object_or_none(id=int(vacancy_id))


@router.put("/{vacancy_id}/update/")
async def update_vacancy(
        vacancy_id: int,
        user_data: SCreateUpdateVacancy,
        user: User = Depends(get_current_user)
) -> SVacancy:
    # if user.is_worker:
    #     raise MethodNotAllowedForWorker
    return await VacancyDAO.update(
        vacancy_id,
        **user_data.model_dump()
    )


@router.delete("/{vacancy_id}/delete/")
async def delete_vacancy(vacancy_id: int, user: User = Depends(get_current_user)):
    # if user.is_worker:
    #     raise MethodNotAllowedForEmployer
    await VacancyDAO.delete(vacancy_id)
