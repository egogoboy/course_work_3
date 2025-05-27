from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

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

    status = Column(String, default="not started") # not_started in_progress finished

    subject = relationship("Subject", back_populates="exams")
    user = relationship("User", back_populates="exams")
    tasks = relationship("Task", back_populates="exam")

    group = relationship("Group", back_populates="exams")
