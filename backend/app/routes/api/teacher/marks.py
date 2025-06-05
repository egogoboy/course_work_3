from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.schemas.mark import MarkCreate, MarkUpdate
from database.database import get_db
from security.rbac import teacher_only
from crud.mark import crudMark


router = APIRouter(prefix="/marks")


@router.post("/",
             dependencies=[Depends(teacher_only)])
async def set_mark_endpoint(mark: MarkCreate,
                            db: Session = Depends(get_db)):
    return await crudMark.set_mark(mark, db)


@router.patch("/",
             dependencies=[Depends(teacher_only)])
async def update_mark_endpoint(mark: MarkUpdate,
                               db: Session = Depends(get_db)):
    return await crudMark.update_mark(mark, db)


@router.get("/{exam_id}",
             dependencies=[Depends(teacher_only)])
async def get_exam_marks_endpoint(exam_id: int,
                                  db: Session = Depends(get_db)):
    return await crudMark.get_exam_marks(exam_id, db)
