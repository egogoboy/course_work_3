from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.user import UserOut
from crud.exam import crudExam
from models.schemas.exam import ExamOut
from security.rbac import get_current_user, all_users
from database.database import get_db

router = APIRouter()


@router.get('/',
            dependencies=[Depends(all_users)])
async def get_exams(status: str = "all",
                    db: Session = Depends(get_db),
                    current_user = Depends(get_current_user)):
    current_user = UserOut.model_validate(current_user)
    exams = await crudExam.get_filter_exams(current_user, db, status)

    return (ExamOut.model_validate(exam) for exam in exams)


@router.get("/{exam_id}", 
            dependencies=[Depends(all_users)])
async def get_current_exams_endpoint(exam_id: int,
                                     db: Session = Depends(get_db)):
    return await crudExam.get_current_exam(exam_id, db)
