from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True)
    title= Column(String)
    body = Column(String)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    subject = relationship("Subject", back_populates="exams")
    user = relationship("User", back_populates="exams")
    tasks = relationship("Task", back_populates="exam")
