from sqlalchemy import Boolean, Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from database.database import Base

class StudentAnswer(Base):
    __tablename__ = "student_answers"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    
    answer_text = Column(Text, nullable=True)
    correct = Column(Boolean)

    task = relationship("Task")
    student = relationship("User")
