from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.schemas.group import GroupCreate
from database.database import Base

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    users= relationship("User", back_populates="group")
    subjects = relationship("GroupSubject", back_populates="group")
    exams = relationship("Exam", back_populates="group")

    @classmethod
    def from_schemas(cls, group_in: GroupCreate):
        return cls(
            name = group_in.name
        )
