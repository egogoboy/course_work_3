from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.answer import AnswerOut
from crud.answers import crudAnswer
from database.database import get_db
from security.rbac import teacher_only


router = APIRouter(prefix="/answers")


@router.patch("/{ans_id}",
              response_model=AnswerOut,
              dependencies=[Depends(teacher_only)])
async def set_correctly_endpoint(ans_id: int,
                                 correct: bool,
                                 db: Session = Depends(get_db)):
    
    return await crudAnswer.set_correctly(ans_id, correct, db)
