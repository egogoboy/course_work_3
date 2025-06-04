from enum import Enum
from typing import List
from pydantic import BaseModel

class ValidTypeEnum(str, Enum):
    not_checked = "not checked"
    valid = "valid"
    not_valid = "not valid"

class AnswerBase(BaseModel):
    exam_id: int
    task_id: int
    answer_text: str


class AnswerCreate(AnswerBase):
    user_id: int


class AnswerOut(AnswerCreate):
    id: int
    valid: str

    class Config:
        orm_mode = True


class AnswerBulkCreate(BaseModel):
    answers: List[AnswerCreate]
