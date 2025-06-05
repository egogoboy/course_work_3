from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.mark import crudMark
from database.database import get_db
from security.rbac import all_users


router = APIRouter(prefix="/marks")


@router.get("/",
            dependencies=[Depends(all_users)])
async def get_mark_endpoint(exam_id: int,
                   student_id: int,
                   db: Session = Depends(get_db)):
    return await crudMark.get_mark(exam_id, student_id, db)
