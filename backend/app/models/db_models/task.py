from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    exam_id = Column(Integer, ForeignKey("exams.id"))

    exam = relationship("Exam", back_populates="tasks")
