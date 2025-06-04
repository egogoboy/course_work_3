from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.answer import AnswerOut
from crud.answers import set_correctly
from sequrity.auth import get_db
from sequrity.rbac import teacher_only


router = APIRouter(prefix="/answers")


@router.patch("/{ans_id}",
              response_model=AnswerOut,
              dependencies=[Depends(teacher_only)])
async def set_correctly_endpoint(ans_id: int,
                                 correct: bool,
                                 db: Session = Depends(get_db)):
    
    return await set_correctly(ans_id, correct, db)
