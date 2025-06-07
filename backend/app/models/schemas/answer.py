from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class ValidTypeEnum(str, Enum):
    not_checked = "not checked"
    valid = "valid"
    not_valid = "not valid"

class AnswerBase(BaseModel):
    exam_id: int
    task_id: int
    answer_text: str

class AnswerIn(AnswerBase):
    user_id: int

class AnswerCreate(AnswerIn):
    valid: ValidTypeEnum = Field(default=ValidTypeEnum.not_checked)

    @classmethod
    def from_in(cls, answer_in: AnswerIn, valid: Optional[ValidTypeEnum] = None):
        return cls(
            user_id=answer_in.user_id,
            task_id=answer_in.task_id,
            answer_text=answer_in.answer_text,
            exam_id=answer_in.exam_id,
            valid=valid or ValidTypeEnum.not_checked
        )

class AnswerOut(AnswerCreate):
    id: int

    class Config:
        orm_mode = True


class AnswerBulkIn(BaseModel):
    answers: List[AnswerIn]
