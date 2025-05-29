from models.db_models.exam import Exam
from models.db_models.task import Task
from models.schemas.task import TaskBulkCreate, TaskCreate
from utils.exceptions.exam import ExamNotFoundException
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


async def add_tasks(exam_id: int,
                    data: TaskBulkCreate,
                    db: Session):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()

    if not exam:
        raise ExamNotFoundException

    for task in data.tasks:
        db_task = Task(
            exam_id=exam_id,
            title=task.title,
            body=task.body,
            answer_type=task.answer_type,
            options=json.dumps(task.options) if task.options else None,
            correct_option=task.correct_option
        )
        db.add(db_task) 

    db.commit()
    return {"detail": f"{len(data.tasks)} заданий добавлено."}
