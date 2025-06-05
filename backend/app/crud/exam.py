from sqlalchemy.orm import Session
from models.db_models.user import User
from models.db_models.task import Task
from utils.exceptions.exam import ExamNotFoundException
from models.schemas.exam import ExamCreate, ExamOut
from models.schemas.user import UserOut
from models.db_models.exam import Exam


class crudExam:
    @staticmethod
    async def create_exam(exam_data: ExamCreate,
                    user_id: int,
                    db: Session):
        new_exam = Exam(
            title=exam_data.title,
            body=exam_data.body,
            subject_id=exam_data.subject_id,
            user_id=user_id,
            group_id=exam_data.group_id,
            start_time=exam_data.start_time,
            end_time=exam_data.end_time
        )

        db.add(new_exam)
        db.commit()
        db.refresh(new_exam)

        return ExamOut.model_validate(new_exam)



    @staticmethod
    async def get_all_exams(db: Session):
        groups = db.query(Exam).all()

        return list(ExamOut.model_validate(group) for group in groups)


    @staticmethod
    async def get_current_exam(exam_id: int,
                               db: Session):
        exam = db.query(Exam).filter(Exam.id == exam_id).first()

        if exam is None:
            raise ExamNotFoundException

        return ExamOut.model_validate(exam)


    @staticmethod
    async def get_filter_exams(current_user: UserOut,
                               db: Session,
                               status: str = "all"):
        exams = None

        if current_user.role == "student":
            exams = db.query(Exam).filter(Exam.group_id == current_user.group_id)
        elif current_user.role == "teacher":
            exams = db.query(Exam).filter(Exam.user_id == current_user.id)

        if exams is None:
            raise ExamNotFoundException

        if status != "all":
            exams = exams.filter(Exam.status == status)

        return list(ExamOut.model_validate(exam) for exam in exams)


    @staticmethod
    async def delete_exam(exam_id: int,
                          db: Session):
        exam = db.query(Exam).filter(Exam.id == exam_id).first()
        if not exam:
            raise ExamNotFoundException
        db.delete(exam)

        exam_tasks = db.query(Task).filter(Task.exam_id == exam.id).all()
        for task in exam_tasks:
            db.delete(task)

        db.commit()
        return ExamOut.model_validate(exam)


    @staticmethod
    async def update_exam(id: int,
                   new_group_data: ExamCreate,
                   db: Session):
        current_group = db.query(Exam).filter(Exam.id == id).first()

        if not current_group:
            raise ExamNotFoundException

        for field, value in new_group_data.model_dump(exclude_unset=True).items():
            setattr(current_group, field, value)

        db.commit()
        db.refresh(current_group)

        return ExamOut.model_validate(current_group)


    @staticmethod
    async def get_exam_students(exam_id: int,
                            db: Session):
        exam = db.query(Exam).filter(Exam.id == exam_id).first()

        if not exam:
            raise ExamNotFoundException

        users = db.query(User).filter(User.group_id == exam.group_id).all()

        return list(UserOut.model_validate(user) for user in users)
