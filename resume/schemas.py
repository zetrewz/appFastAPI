from pydantic import BaseModel, Field


class SCreateUpdateResume(BaseModel):
    first_name: str = Field(min_length=2, max_length=30)
    last_name: str = Field(min_length=2, max_length=30)
    work_name: str = Field(min_length=5, max_length=50)
    about: str = Field(min_length=20, max_length=500)


class SResume(SCreateUpdateResume):
    id: int
    user_id: int
