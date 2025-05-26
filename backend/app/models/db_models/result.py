from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database.database import Base

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    answer = Column(String)
    score = Column(Integer)

    user= relationship("User", back_populates="results")
    task = relationship("Task")
