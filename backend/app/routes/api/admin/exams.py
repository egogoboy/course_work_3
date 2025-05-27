from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.schemas.common import APIResponse
from models.schemas.exam import ExamOut
from sequrity.auth import get_db
from crud.exam import delete_exam

router = APIRouter()

@router.post("/delete",
             response_model=APIResponse[ExamOut])
async def delete_exam_endpoint(exam_id: int,
                               db: Session = Depends(get_db)):
    return APIResponse(data=delete_exam(exam_id, db))
