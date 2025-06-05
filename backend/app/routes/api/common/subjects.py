from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.subject import crudSubject
from database.database import get_db
from security.rbac import all_users


router = APIRouter()


@router.get("/{subject_id}", 
            dependencies=[Depends(all_users)])
async def get_current_subjects_endpoint(subject_id: int,
                                      db: Session = Depends(get_db)):
    return await crudSubject.get_current_subject(subject_id, db)
