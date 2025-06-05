from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from security.rbac import teacher_only
from crud.answers import crudAnswer


router = APIRouter(prefix="/results")


@router.get("/{exam_id}/{user_id}",
            dependencies=[Depends(teacher_only)])
async def get_user_answers_endpoint(user_id: int,
                                    exam_id: int,
                                    db : Session = Depends(get_db)):
    return await crudAnswer.get_answers(exam_id, user_id, db)
