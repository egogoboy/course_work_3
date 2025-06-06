from pydantic import BaseModel

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    pass

class SubjectOut(SubjectCreate):
    id: int

    class Config:
        from_attributes = True
