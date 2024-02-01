from fastapi import APIRouter, Depends, HTTPException

from exceptions import MethodNotAllowedForEmployer
from resume.dao import ResumeDAO
from resume.schemas import SCreateUpdateResume, SResume
from users.dependencies import get_current_user
from users.models import User

router = APIRouter(
    prefix="/resumes",
    tags=["Резюме"],
)


@router.post("/create/")
async def create_resume(
        user_data: SCreateUpdateResume,
        user: User = Depends(get_current_user)
) -> SResume:
    if user.user_type == "employer":
        raise MethodNotAllowedForEmployer
    user_data = user_data.model_dump()
    user_data["user_id"] = user.id
    return await ResumeDAO.add(**user_data)


@router.get("/list/")
async def get_resumes() -> list[SResume]:
    return await ResumeDAO.get_objects()


@router.get("/{resume_id}/")
async def get_resume(resume_id: int) -> None | SResume:
    return await ResumeDAO.get_object_or_none(id=int(resume_id))


@router.put("/{resume_id}/update/")
async def update_resume(
        resume_id: int,
        user_data: SCreateUpdateResume,
        user: User = Depends(get_current_user)
) -> SResume:
    resume = await ResumeDAO.get_object_or_none(id=resume_id)
    if resume.user_id != user.id:
        raise HTTPException(status_code=403)
    return await ResumeDAO.update(
        resume_id,
        **user_data.model_dump()
    )


@router.delete("/{resume_id}/delete/")
async def delete_resume(resume_id: int, user: User = Depends(get_current_user)):
    resume = await ResumeDAO.get_object_or_none(id=resume_id)
    if resume.user_id != user.id:
        raise HTTPException(status_code=403)
    await ResumeDAO.delete(resume_id)
