from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ExamBase(BaseModel):
    title: str
    body: str


class ExamIn(ExamBase):
    subject_id: int
    group_id: int
    start_time: datetime
    end_time: datetime


class ExamCreate(ExamIn):
    user_id: int

    @classmethod
    def from_in(cls, exam_in: ExamIn, user_id: int):
        return cls(
            title=exam_in.title,
            body=exam_in.body,
            subject_id=exam_in.subject_id,
            user_id=user_id,
            group_id=exam_in.group_id,
            start_time=exam_in.start_time,
            end_time=exam_in.end_time
        )

class ExamOut(ExamCreate):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)
