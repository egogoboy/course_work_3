from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: str
