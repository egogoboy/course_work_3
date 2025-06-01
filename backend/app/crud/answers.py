from sqlalchemy.orm import Session
from models.db_models.exam import Exam
from models.db_models.answer import Answer
from models.schemas.answer import AnswerBulkCreate, AnswerOut
from utils.exceptions.exam import ExamNotFoundException
from utils.exceptions.answer import AnswerNotFoundException


async def add_answers(exam_id: int,
                      data: AnswerBulkCreate,
                      db: Session):
    exam = db.query(Exam).filter(Exam.id == exam_id).first()

    if not exam:
        raise ExamNotFoundException

    for answer in data.answers:
        db_ans = Answer(
            exam_id=exam_id,
            user_id=answer.user_id,
            task_id=answer.task_id,
            answer_text=answer.answer_text
        )
        db.add(db_ans) 

    db.commit()
    print("Succesfully added answers")
    return {"detail": f"{len(data.answers)} ответов добавлено."}


async def get_answers(exam_id: int,
                      user_id: int,
                      db: Session):
    answers = db.query(Answer).filter(Answer.user_id == user_id).filter(Answer.exam_id == exam_id).all()

    if not answers:
        raise AnswerNotFoundException

    return [AnswerOut.model_validate(answer, from_attributes=True) for answer in answers]
