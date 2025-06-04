from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)

    student = relationship("User")
    exam = relationship("Exam")
