from typing import Literal
from models.schemas.user_base import UserBase

class AdminLogin(UserBase):
    password: str


class AdminCreate(AdminLogin):
    role: Literal["admin"]
