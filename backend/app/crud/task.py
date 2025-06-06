from models.db_models.exam import Exam
from models.db_models.task import Task
from models.schemas.task import TaskBulkCreate, TaskCreate, TaskOut
from utils.exceptions.task import TaskNotFoundException
from utils.exceptions.exam import ExamNotFoundException
from sqlalchemy.orm import Session
import json


class crudTask:
    @staticmethod
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


    @staticmethod
    async def add_tasks(in_exam_id: int,
                        data: TaskBulkCreate,
                        db: Session):
        exam = db.query(Exam).filter(Exam.id == in_exam_id).first()

        print(in_exam_id)

        if not exam:
            raise ExamNotFoundException

        for task in data.tasks:
            db_task = Task(
                title=task.title,
                body=task.body,
                exam_id=in_exam_id,
                answer_type=task.answer_type,
                options=json.dumps(task.options) if task.options else None,
                correct_option=task.correct_option
            )
            print(db_task.exam_id)
            db.add(db_task) 

        db.commit()
        print(data.tasks)
        return {"detail": f"{len(data.tasks)} заданий добавлено."}


    @staticmethod
    async def get_current_task(task_id: int,
                               db: Session):
        task = await crudTask._get_task_from_db(task_id, db)

        return TaskOut.model_validate(task)


    @staticmethod
    async def get_current_task_answer(task_id: int,
                               db: Session):
        task = await crudTask._get_task_from_db(task_id, db)

        return task.get_correct_answer_text()


    @staticmethod
    async def get_exam_tasks(exam_id: int,
                             db: Session):
        existing_exam = db.query(Exam).filter(Exam.id == exam_id).first()

        if not existing_exam:
            raise ExamNotFoundException

        return db.query(Task).filter(Task.exam_id == exam_id).all()


    @staticmethod
    async def delete_task(task_id: int,
                          db: Session):

        task = await crudTask._get_task_from_db(task_id, db)

        db.delete(task)
        db.commit()
        return TaskOut.model_validate(task)


    @staticmethod
    async def _get_task_from_db(task_id: int,
                               db: Session):
        task = db.query(Task).filter(Task.id == task_id).first()

        if not task:
            raise TaskNotFoundException

        return task


    @staticmethod
    async def _get_exam_tasks_from_db(exam_id: int,
                                     db: Session):
        tasks = db.query(Task).filter(Task.exam_id == exam_id).all()

        if not tasks:
            raise TaskNotFoundException

        return tasks
