from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

from models.schemas.exam import ExamCreate

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    title= Column(String)
    body = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))

    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)

    status = Column(String, default="not_started") # not_started in_progress finished

    subject = relationship("Subject", back_populates="exams")
    user = relationship("User", back_populates="exams")
    tasks = relationship("Task", back_populates="exam", cascade="all, delete-orphan")

    group = relationship("Group", back_populates="exams")


    @classmethod
    def from_schemas(cls, exam_in: ExamCreate):
        return cls(
            title=exam_in.title,
            body=exam_in.body,
            subject_id=exam_in.subject_id,
            user_id=exam_in.user_id,
            group_id=exam_in.group_id,
            start_time=exam_in.start_time,
            end_time=exam_in.end_time
        )
