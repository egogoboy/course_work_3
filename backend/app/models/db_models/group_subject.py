from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base

class GroupSubject(Base):
    __tablename__ = "group_subjects"

    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    group = relationship("Group", back_populates="subjects")
    subject = relationship("Subject", back_populates="group_links")
