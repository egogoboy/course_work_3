from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ExamBase(BaseModel):
    title: str
    body: str


class ExamCreate(ExamBase):
    subject_id: int
    group_id: int
    start_time: datetime
    end_time: datetime

class ExamOut(ExamCreate):
    id: int
    user_id: int
    status: str

    model_config = ConfigDict(from_attributes=True)
