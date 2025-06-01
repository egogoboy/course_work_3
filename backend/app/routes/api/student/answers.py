from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.answers import add_answers, get_answers
from sequrity.auth import get_db
from sequrity.rbac import get_current_user, student_only
from models.schemas.answer import AnswerBulkCreate, AnswerOut


router = APIRouter()


@router.post("/{exam_id}",
            dependencies=[Depends(student_only)])
async def put_answers_endpoint(exam_id: int,
                               answers_data: AnswerBulkCreate,
                               db: Session = Depends(get_db)):
    return await add_answers(exam_id, answers_data, db)


@router.get("/{exam_id}",
            dependencies=[Depends(student_only)],
            response_model=list[AnswerOut])
async def get_answers_endpoint(exam_id: int,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    return await get_answers(exam_id, current_user.id,db)
