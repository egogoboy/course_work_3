from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from security.auth import get_db
from crud.exam import delete_exam

router = APIRouter()

@router.delete("/{exam_id}")
async def delete_exam_endpoint(exam_id: int,
                               db: Session = Depends(get_db)):
    return await delete_exam(exam_id, db)
