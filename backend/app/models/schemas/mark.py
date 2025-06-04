from pydantic import BaseModel


class MarkBase(BaseModel):
    mark: int

            
class MarkCreate(MarkBase):
    exam_id: int
    student_id: int


class MarkUpdate(MarkCreate):
    pass


class MarkOut(MarkCreate):
    id: int

    class Config:
        from_attributes = True
