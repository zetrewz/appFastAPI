from pydantic import BaseModel, EmailStr, Field


class SUserLogin(BaseModel):
    email: EmailStr = Field(
        examples=["Type a valid e-mail"]
    )
    password: str = Field(
        min_length=1,
        max_length=10,
        examples=["Type a valid password"]
    )


class SUserRegister(SUserLogin):
    pass


class SUser(BaseModel):
    id: int
    email: EmailStr
    user_type: str
    is_active: bool
