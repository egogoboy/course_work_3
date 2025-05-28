from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    password: str

class UserCreate(UserLogin):
    role: str
    group_id: Optional[int] = None

class UserOut(UserBase):
    id: int
    role: str
    group_id: Optional[int] = None

    class Config:
        from_attributes = True  # instread orm_mode in Pydantic v2

class UserUpdate(UserBase):
    category: Optional[int] = None
    role: Optional[str] = None
    group_id: Optional[int] = None  # если есть привязка к группе

    class Config:
        from_attributes = True
