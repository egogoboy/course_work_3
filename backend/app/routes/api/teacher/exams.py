from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.db_models.exam import Exam
from crud.exam import crudExam
from models.schemas.exam import ExamIn
from database.database import get_db
from security.rbac import get_current_user, teacher_only, admin_and_teacher


router = APIRouter()


@router.post('/create', 
             dependencies=[Depends(teacher_only)])
async def create_exam_endpoint(exam: ExamIn,
                               db: Session = Depends(get_db),
                               current_user = Depends(get_current_user)):
    created_exam = await crudExam.create_exam(exam, current_user.id, db)

    return created_exam


@router.delete("/{exam_id}", 
               dependencies=[Depends(teacher_only)])
async def delete_exam_endpoint(exam_id: int,
                       db: Session = Depends(get_db)):
    return await crudExam.delete_exam(exam_id, db)


@router.get("/", 
            dependencies=[Depends(admin_and_teacher)])
async def get_all_exams_endpoint(status: str = "all",
                                 db: Session = Depends(get_db)):
    return await crudExam.get_all_exams(db)


@router.put("/{exam_id}",
            dependencies=[Depends(teacher_only)])
async def edit_exam_endpoint(exam_id: int,
                              new_data: ExamIn,
                              db: Session = Depends(get_db)):
    return await crudExam.update_exam(exam_id, new_data, db)


@router.get("/{exam_id}/users",
            dependencies=[Depends(admin_and_teacher)])
async def get_exam_students_endpoint(exam_id: int,
                                     db: Session = Depends(get_db)):
    return await crudExam.get_exam_students(exam_id, db)
