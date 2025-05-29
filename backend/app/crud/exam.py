from sqlalchemy.orm import Session
from utils.exceptions.exam import ExamNotFoundException
from models.schemas.exam import ExamCreate, ExamOut
from models.db_models.exam import Exam


async def create_exam(exam_data: ExamCreate,
                user_id: int,
                db: Session):
    new_exam = Exam(
        title=exam_data.title,
        body=exam_data.body,
        subject_id=exam_data.subject_id,
        user_id=user_id,
        group_id=exam_data.group_id,
        start_time=exam_data.start_time,
        end_time=exam_data.end_time
    )

    db.add(new_exam)
    db.commit()
    db.refresh(new_exam)

    return ExamOut.model_validate(new_exam)



async def get_all_exams(db: Session):
    groups = db.query(Exam).all()

    return list(ExamOut.model_validate(group) for group in groups)


async def get_current_exam(exam_id: int,
                           db: Session):
    group = db.query(Exam).filter(Exam.id == exam_id).first()

    if group is None:
        raise ExamNotFoundException

    return ExamOut.model_validate(group)


async def delete_exam(exam_id: int,
                      db: Session):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise ExamNotFoundException
    db.delete(exam)
    db.commit()
    return ExamOut.model_validate(exam)


async def update_exam(id: int,
               new_group_data: ExamCreate,
               db: Session):
    current_group = db.query(Exam).filter(Exam.id == id).first()

    if not current_group:
        raise ExamNotFoundException

    for field, value in new_group_data.model_dump(exclude_unset=True).items():
        setattr(current_group, field, value)

    db.commit()
    db.refresh(current_group)

    return ExamOut.model_validate(current_group)
