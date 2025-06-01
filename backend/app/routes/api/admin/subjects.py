from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.subject import create_subject, get_all_subjects, delete_subject, update_subject
from models.schemas.subject import SubjectCreate
from sequrity.auth import get_db
from sequrity.rbac import admin_only, admin_and_teacher


router = APIRouter()


@router.post("/create", 
             dependencies=[Depends(admin_only)])
async def create_subject_endpoint(subject: SubjectCreate,
                       db: Session = Depends(get_db)):
    print(subject)
    return await create_subject(subject, db)


@router.delete("/{subject_id}", 
               dependencies=[Depends(admin_only)])
async def delete_subject_endpoint(subject_id: int,
                       db: Session = Depends(get_db)):
    return await delete_subject(subject_id, db)


@router.get("/", 
            dependencies=[Depends(admin_and_teacher)])
async def get_all_subjects_endpoint(db: Session = Depends(get_db)):
    return await get_all_subjects(db)


@router.put("/{subject_id}",
            dependencies=[Depends(admin_only)])
async def edit_subject_endpoint(subject_id: int,
                              new_data: SubjectCreate,
                              db: Session = Depends(get_db)):
    return await update_subject(subject_id, new_data, db)
