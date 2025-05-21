from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class UserLogin(BaseModel):
    username: str
    password: str


class UserCreate(UserLogin):
    username: str
    password: str
    role: Role


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
