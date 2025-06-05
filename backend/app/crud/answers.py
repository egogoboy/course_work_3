from sqlalchemy.orm import Session
from crud.task import crudTask
from models.db_models.exam import Exam
from models.db_models.answer import Answer
from models.schemas.answer import AnswerBulkCreate, AnswerOut, ValidTypeEnum
from utils.exceptions.exam import ExamNotFoundException
from utils.exceptions.answer import AnswerNotFoundException


class crudAnswer:
    @staticmethod
    async def add_answers(exam_id: int,
                          data: AnswerBulkCreate,
                          db: Session):
        exam = db.query(Exam).filter(Exam.id == exam_id).first()

        if not exam:
            raise ExamNotFoundException

        for answer in data.answers:
            valid = ValidTypeEnum.not_checked
            task_answer = await crudTask.get_current_task_answer(answer.task_id, db)
            
            if task_answer is not None:
                if task_answer == answer.answer_text:
                    valid = ValidTypeEnum.valid
                else:
                    valid = ValidTypeEnum.not_valid

            db_ans = Answer(
                exam_id=exam_id,
                user_id=answer.user_id,
                task_id=answer.task_id,
                answer_text=answer.answer_text,
                valid=valid.value
            )
            db.add(db_ans) 

        db.commit()
        print("Succesfully added answers")
        return {"detail": f"{len(data.answers)} ответов добавлено."}


    @staticmethod
    async def get_answers(exam_id: int,
                          user_id: int,
                          db: Session):
        answers = db.query(Answer).filter(Answer.user_id == user_id).filter(Answer.exam_id == exam_id).all()

        if not answers:
            answers = await crudAnswer._create_empty_answers(exam_id, user_id, db)

        return [AnswerOut.model_validate(answer, from_attributes=True) for answer in answers]


    @staticmethod
    async def get_user_answers(user_id: int,
                               exam_id: int,
                               db: Session):
        answers = db.query(Answer).filter(Answer.user_id == user_id).filter(Answer.exam_id == exam_id).all()

        if not answers:
            raise AnswerNotFoundException

        return list(AnswerOut.model_validate(answer) for answer in answers)


    @staticmethod
    async def set_correctly(ans_id: int,
                            correctly: bool,
                            db: Session):
        answer = await crudAnswer._get_answer_from_db(ans_id, db)

        answer.set_valid(correctly)

        db.commit()

        return AnswerOut.model_validate(answer, from_attributes=True)


    @staticmethod
    async def _get_answer_from_db(ans_id: int,
                                 db: Session):
        answer = db.query(Answer).filter(Answer.id == ans_id).first()

        if not answer:
            raise AnswerNotFoundException

        return answer


    @staticmethod
    async def _create_empty_answers(exam_id: int,
                                   user_id: int,
                                   db: Session):
        tasks = await crudTask._get_exam_tasks_from_db(exam_id, db)
        
        for task in tasks:
            answer = Answer(
                exam_id=exam_id,
                user_id=user_id,
                task_id=task.id,
                answer_text="",
                valid="not valid"
            )
            db.add(answer)
        db.commit()

        answers = db.query(Answer).filter(Answer.exam_id == exam_id, Answer.user_id == user_id).all()

        return answers
