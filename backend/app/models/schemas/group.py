from pydantic import BaseModel

class GroupCreate(BaseModel):
    name: str

class GroupOut(GroupCreate):
    id: int

    class Config:
        from_attributes = True
