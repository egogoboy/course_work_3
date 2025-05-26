from typing import List, Union
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from utils.exceptions import AuthenticationRequiredException
from models.db_models.exam import Exam
from models.db_models.group import Group
from models.schemas.exam import ExamOut, ExamCreate
from models.schemas.common import APIResponse
from sequrity.rbac import get_current_user, teacher_only
from sequrity.auth import get_db
from crud.exam.exam import create_exam

router = APIRouter()

@router.post('/create', 
             response_model=APIResponse[ExamOut],
             dependencies=[Depends(teacher_only)])
async def create_exam_endpoint(exam: ExamCreate,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    created_exam = await create_exam(exam, db, current_user.id)
    return APIResponse(data=created_exam)


@router.get('/',
            response_model=APIResponse[List[ExamOut]])
async def get_exams(db: Session = Depends(get_db),
                    current_user = Depends(get_current_user)):
    exams = []
    if current_user.role == "teacher":
        exams = db.query(Exam).filter(Exam.user_id == current_user.id)
    elif current_user.role == "student":
        exams = db.query(Exam).join(Exam.groups).filter(Group.id == current_user.group_id)
    elif current_user.role == "admin":
        exams = db.query(Exam).all()

    return APIResponse(data=[ExamOut.model_validate(exam) for exam in exams])
