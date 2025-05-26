from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db_models.exam_group import exam_group
from database.database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    users= relationship("User", back_populates="group")
    subjects = relationship("GroupSubject", back_populates="group")
    exams = relationship("Exam", secondary=exam_group, back_populates="groups")
