from datetime import datetime

from pydantic import BaseModel, Field


class SCreateUpdateVacancy(BaseModel):
    name: str = Field(min_length=5, max_length=50)
    company_name: str = Field(min_length=5, max_length=100)
    about: str = Field(min_length=20, max_length=500)
    is_active: bool


class SVacancy(SCreateUpdateVacancy):
    id: int
    created_at: datetime
    user_id: int
