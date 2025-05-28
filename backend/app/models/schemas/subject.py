from pydantic import BaseModel

class SubjectCreate(BaseModel):
    name: str

class SubjectOut(SubjectCreate):
    id: int

    class Config:
        from_attributes = True
