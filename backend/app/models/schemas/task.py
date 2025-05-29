from pydantic import BaseModel
from typing import Optional, List
from enum import Enum

class AnswerType(str, Enum):
    text = "text"
    choice = "choice"

class TaskBase(BaseModel):
    title: str
    body: str
    answer_type: AnswerType

class TaskCreate(TaskBase):
    exam_id: Optional[int] = None
    options: Optional[List[str]] = None
    correct_option: Optional[int] = None

class TaskOut(TaskBase):
    id: int
    options: Optional[List[str]] = None

    class Config:
        from_attributes = True

class TaskBulkCreate(BaseModel):
    tasks: List[TaskCreate]
