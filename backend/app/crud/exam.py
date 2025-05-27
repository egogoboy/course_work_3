from sqlalchemy.orm import Session
from utils.exceptions.exam import ExamNotFoundException
from models.schemas.exam import ExamCreate, ExamOut
from models.db_models.exam import Exam


async def create_exam(exam_data: ExamCreate,
                user_id: int,
                db: Session):
    new_exam = Exam(
        title=exam_data.title,
        body=exam_data.body,
        subject_id=exam_data.subject_id,
        user_id=user_id,
        group_id=exam_data.group_id
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return ExamOut.model_validate(new_exam)


async def delete_exam(exam_id: int,
                      db: Session):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise ExamNotFoundException
    db.delete(exam)
    db.commit()
    return ExamOut.model_validate(exam)
