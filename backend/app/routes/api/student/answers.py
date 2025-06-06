from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.answers import crudAnswer
from database.database import get_db
from security.rbac import get_current_user, student_only
from models.schemas.answer import AnswerBulkIn, AnswerOut


router = APIRouter()


@router.post("/{exam_id}",
            dependencies=[Depends(student_only)])
async def put_answers_endpoint(exam_id: int,
                               answers_data: AnswerBulkIn,
                               db: Session = Depends(get_db)):
    return await crudAnswer.add_answers(exam_id, answers_data, db)


@router.get("/{exam_id}",
            dependencies=[Depends(student_only)],
            response_model=list[AnswerOut])
async def get_answers_endpoint(exam_id: int,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    return await crudAnswer.get_answers(exam_id, current_user.id,db)
