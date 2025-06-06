from pydantic import BaseModel

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    pass

class GroupOut(GroupCreate):
    id: int

    class Config:
        from_attributes = True
