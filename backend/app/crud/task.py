from models.db_models.task import Task
from models.schemas.task import TaskCreate
from sqlalchemy.orm import Session
import json

async def create_task(task_data: TaskCreate, db: Session):
    task = Task(
        title=task_data.title,
        body=task_data.body,
        answer_type=task_data.answer_type,
        exam_id=task_data.exam_id,
        options=json.dumps(task_data.options) if task_data.options else None,
        correct_option=task_data.correct_option
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    return task
