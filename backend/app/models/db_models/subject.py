from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.schemas.subject import SubjectCreate
from database.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    exams = relationship("Exam", back_populates="subject")
    group_links = relationship("GroupSubject", back_populates="subject")


    @classmethod
    def from_schemas(cls, subject_in: SubjectCreate):
        return cls(
            name = subject_in.name
        )
