from sqlalchemy.orm import Session

from models.db_models.answer import Answer
from models.schemas.answer import AnswerOut
from utils.exceptions.answer import AnswerNotFoundException


async def get_user_answers(user_id: int,
                           exam_id: int,
                           db: Session):
    answers = db.query(Answer).filter(Answer.user_id == user_id).filter(Answer.exam_id == exam_id).all()

    if not answers:
        raise AnswerNotFoundException

    return list(AnswerOut.model_validate(answer) for answer in answers)
