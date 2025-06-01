from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.subject import get_current_subject
from sequrity.auth import get_db
from sequrity.rbac import all_users


router = APIRouter()


@router.get("/{subject_id}", 
            dependencies=[Depends(all_users)])
async def get_current_subjects_endpoint(subject_id: int,
                                      db: Session = Depends(get_db)):
    return await get_current_subject(subject_id, db)
