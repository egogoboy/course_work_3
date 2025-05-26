from datetime import time
from pydantic import BaseModel, ConfigDict

class ExamBase(BaseModel):
    title: str
    body: str


class ExamCreate(ExamBase):
    subject_id: int
    group_id: int
    status: str
    created_at: time


class ExamOut(ExamBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)
