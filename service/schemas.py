from datetime import datetime

from pydantic import BaseModel


class SApply(BaseModel):
    resume_id: int
    vacancy_id: int


class SApplication(SApply):
    id: int
    applied_at: datetime
