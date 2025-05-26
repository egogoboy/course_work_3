from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
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
