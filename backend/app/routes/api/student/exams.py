from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.exam import crudExam
from models.schemas.exam import ExamCreate
from database.database import get_db
from security.rbac import get_current_user, student_only


router = APIRouter()


@router.post('/create', 
             dependencies=[Depends(student_only)])
async def create_exam_endpoint(exam: ExamCreate,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    created_exam = await crudExam.create_exam(exam, current_user.id, db)

    return created_exam


@router.delete("/{exam_id}", 
               dependencies=[Depends(student_only)])
async def delete_exam_endpoint(exam_id: int,
                       db: Session = Depends(get_db)):
    return await crudExam.delete_exam(exam_id, db)


@router.get("/{exam_id}", 
            dependencies=[Depends(student_only)])
async def get_current_exams_endpoint(exam_id: int,
                                      db: Session = Depends(get_db)):
    return await crudExam.get_current_exam(exam_id, db)


@router.put("/{exam_id}",
            dependencies=[Depends(student_only)])
async def edit_exam_endpoint(exam_id: int,
                              new_data: ExamCreate,
                              db: Session = Depends(get_db)):
    return await crudExam.update_exam(exam_id, new_data, db)
