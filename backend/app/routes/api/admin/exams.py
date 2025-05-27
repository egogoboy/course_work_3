from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from sequrity.auth import get_db
from crud.exam import delete_exam

router = APIRouter()

@router.post("/delete")
async def delete_exam_endpoint(exam_id: int,
                               db: Session = Depends(get_db)):
    return delete_exam(exam_id, db)
