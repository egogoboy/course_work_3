from sqlalchemy.orm import relationship
from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String

from models.schemas.user import UserCreate

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
 
    group_id = Column(Integer, ForeignKey("groups.id"), nullable=True)

    exams = relationship("Exam", back_populates="user")
    group = relationship("Group", back_populates="users")
    results = relationship("Result", back_populates="user")


    @classmethod
    def from_schemas(cls, user_in: UserCreate):
        return cls(
            username=user_in.username,
            hashed_password=user_in.password,
            role=user_in.role,
            group_id=user_in.group_id
        )
