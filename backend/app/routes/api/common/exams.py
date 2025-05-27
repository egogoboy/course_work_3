from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.db_models.exam import Exam
from models.schemas.exam import ExamOut
from sequrity.rbac import get_current_user
from sequrity.auth import get_db

router = APIRouter()


@router.get('/')
async def get_exams(db: Session = Depends(get_db),
                    current_user = Depends(get_current_user)):
    exams = []
    if current_user.role == "teacher":
        exams = db.query(Exam).filter(Exam.user_id == current_user.id)
    elif current_user.role == "student":
        exams = db.query(Exam).filter(Exam.group_id == current_user.group_id)
    elif current_user.role == "admin":
        exams = db.query(Exam).all()

    return (ExamOut.model_validate(exam) for exam in exams)
