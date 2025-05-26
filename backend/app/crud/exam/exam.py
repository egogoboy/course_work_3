from fastapi import Depends
from sqlalchemy.orm import Session
from models.schemas.exam import ExamCreate, ExamOut
from sequrity.auth import get_db
from models.db_models.exam import Exam


async def create_exam(exam_data: ExamCreate,
                db: Session,
                user_id: int):
    new_exam = Exam(
        title=exam_data.title,
        body=exam_data.body,
        subject_id=exam_data.subject_id,
        user_id=user_id
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return ExamOut.model_validate(new_exam)
