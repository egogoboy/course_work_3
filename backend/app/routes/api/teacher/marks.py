from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.schemas.mark import MarkCreate, MarkUpdate
from sequrity.auth import get_db
from sequrity.rbac import teacher_only
from crud.mark import set_mark, update_mark


router = APIRouter(prefix="/marks")


@router.post("/",
             dependencies=[Depends(teacher_only)])
async def set_mark_endpoint(mark: MarkCreate,
                            db: Session = Depends(get_db)):
    return await set_mark(mark, db)


@router.patch("/",
             dependencies=[Depends(teacher_only)])
async def update_mark_endpoint(mark: MarkUpdate,
                               db: Session = Depends(get_db)):
    return await update_mark(mark, db)
