from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

from models.schemas.mark import MarkCreate

class Mark(Base):
    __tablename__ = "marks"

    id = Column(Integer, primary_key=True)
    mark = Column(Integer)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False)

    student = relationship("User")
    exam = relationship("Exam")


    @classmethod
    def from_schemas(cls, mark_in: MarkCreate):
        return cls(
            mark = mark_in.mark,
            student_id = mark_in.student_id,
            exam_id = mark_in.exam_id
        )
