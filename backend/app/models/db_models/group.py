from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    users= relationship("User", back_populates="group")
    subjects = relationship("GroupSubject", back_populates="group")
    exams = relationship("Exam", back_populates="group")
