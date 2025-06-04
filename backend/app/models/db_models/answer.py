from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id", ondelete="CASCADE"))
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"))
    answer_text = Column(String)
    valid = Column(String, default="not checked")

    user = relationship("User")
    task = relationship("Task")
    exam = relationship("Exam")


    def set_valid(self, is_valid: bool):
        print(is_valid)
        if is_valid:
            self.valid = "valid"
        else:
            self.valid = "not valid"

        print(self.valid)
