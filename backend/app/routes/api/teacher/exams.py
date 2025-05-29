from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.exam import create_exam, get_all_exams, delete_exam, get_current_exam, update_exam
from models.schemas.exam import ExamCreate
from sequrity.auth import get_db
from sequrity.rbac import get_current_user, teacher_only, admin_and_teacher


router = APIRouter()


@router.post('/create', 
             dependencies=[Depends(teacher_only)])
async def create_exam_endpoint(exam: ExamCreate,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    created_exam = await create_exam(exam, current_user.id, db)
    return created_exam


@router.delete("/{exam_id}", 
               dependencies=[Depends(teacher_only)])
async def delete_exam_endpoint(exam_id: int,
                       db: Session = Depends(get_db)):
    return await delete_exam(exam_id, db)


@router.get("/", 
            dependencies=[Depends(admin_and_teacher)])
async def get_all_exams_endpoint(db: Session = Depends(get_db)):
    return await get_all_exams(db)


@router.get("/{exam_id}", 
            dependencies=[Depends(teacher_only)])
async def get_current_exams_endpoint(exam_id: int,
                                      db: Session = Depends(get_db)):
    return await get_current_exam(exam_id, db)

@router.put("/{exam_id}",
            dependencies=[Depends(teacher_only)])
async def edit_exam_endpoint(exam_id: int,
                              new_data: ExamCreate,
                              db: Session = Depends(get_db)):
    return await update_exam(exam_id, new_data, db)
