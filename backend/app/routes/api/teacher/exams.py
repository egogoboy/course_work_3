from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.db_models.exam import Exam
from crud.exam import create_exam, get_all_exams, delete_exam, get_exam_students, update_exam
from models.schemas.exam import ExamCreate
from security.auth import get_db
from security.rbac import get_current_user, teacher_only, admin_and_teacher


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
async def get_all_exams_endpoint(status: str = "all",
                                 db: Session = Depends(get_db)):
    return await get_all_exams(db)


@router.put("/{exam_id}",
            dependencies=[Depends(teacher_only)])
async def edit_exam_endpoint(exam_id: int,
                              new_data: ExamCreate,
                              db: Session = Depends(get_db)):
    return await update_exam(exam_id, new_data, db)


@router.put("/admin/fix-exam-status")
def fix_exam_status(db: Session = Depends(get_db)):
    updated_count = db.query(Exam).filter(Exam.status == "not started") \
        .update({Exam.status: "not_started"}, synchronize_session=False)
    db.commit()
    return {"updated": updated_count}


@router.get("/{exam_id}/users",
            dependencies=[Depends(admin_and_teacher)])
async def get_exam_students_endpoint(exam_id: int,
                                     db: Session = Depends(get_db)):
    print(await get_exam_students(exam_id, db))
    return await get_exam_students(exam_id, db)
