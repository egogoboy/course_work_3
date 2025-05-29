from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from database.database import Base
import enum

class AnswerTypeEnum(enum.Enum):
    text = "text"
    choice = "choice"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    answer_type = Column(Enum(AnswerTypeEnum), nullable=False)

    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)
    exam = relationship("Exam", back_populates="tasks")

    options = Column(Text, nullable=True)
    correct_option = Column(Integer, nullable=True)
