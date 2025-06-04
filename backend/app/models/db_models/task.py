from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.database import Base
from models.types import JSONEncodedList
import enum

class AnswerTypeEnum(enum.Enum):
    text = "text"
    choice = "choice"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    answer_type = Column(Enum(AnswerTypeEnum, native_enym=False), nullable=False)

    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    exam = relationship("Exam", back_populates="tasks")

    options = Column(JSONEncodedList, nullable=True, default=list)
    correct_option = Column(Integer, nullable=True)


    def get_correct_answer_text(self) -> str | None:
        if self.answer_type != AnswerTypeEnum.choice:
            return None

        if not self.options or self.correct_option is None:
            return None

        try:
            return self.options[self.correct_option]
        except IndexError:
            return None
