from typing import List
from pydantic import BaseModel

class AnswerBase(BaseModel):
    exam_id: int
    task_id: int
    answer_text: str


class AnswerCreate(AnswerBase):
    user_id: int


class AnswerOut(AnswerBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class AnswerBulkCreate(BaseModel):
    answers: List[AnswerCreate]
