from sqlalchemy.orm import Session

from models.schemas.mark import MarkCreate, MarkOut, MarkUpdate
from models.db_models.mark import Mark
from utils.exceptions.mark import MarkNotFoundException


async def get_exam_marks_from_db(exam_id,
                                 db: Session):
    marks = db.query(Mark).filter(Mark.exam_id == exam_id).all()

    if not marks:
        raise MarkNotFoundException

    return marks


async def get_mark_from_db(exam_id: int,
                           student_id: int,
                           db: Session):
    mark = db.query(Mark).filter((Mark.student_id == student_id) & (Mark.exam_id == exam_id)).first()

    if not mark:
        raise MarkNotFoundException

    return mark


async def update_mark(new_mark_data: MarkUpdate,
                      db: Session):
    mark = await get_mark_from_db(new_mark_data.exam_id, new_mark_data.student_id, db)

    setattr(mark, "mark", new_mark_data.mark)

    db.commit()
    db.refresh(mark)

    return MarkOut.model_validate(mark)


async def set_mark(mark: MarkCreate,
                   db: Session):
    db_mark = Mark(
        mark=mark.mark,
        student_id=mark.student_id,
        exam_id=mark.exam_id
    )

    db.add(db_mark)
    db.commit()
    db.refresh(db_mark)

    return MarkOut.model_validate(db_mark)


async def get_mark(exam_id: int,
                   student_id: int,
                   db: Session):
    mark = await get_mark_from_db(exam_id, student_id, db)

    return MarkOut.model_validate(mark, from_attributes=True)


async def get_exam_marks(exam_id: int,
                         db: Session):
    marks = await get_exam_marks_from_db(exam_id, db)

    return list(MarkOut.model_validate(mark) for mark in marks)
