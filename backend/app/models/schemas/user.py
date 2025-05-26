from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

class UserLogin(UserBase):
    password: str

class UserCreate(UserLogin):
    role: str

class UserOut(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True  # instread orm_mode in Pydantic v2
