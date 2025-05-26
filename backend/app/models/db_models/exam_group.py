from sqlalchemy import Column, ForeignKey, Integer, Table

from database.database import Base

exam_group = Table(
    "exam_group",
    Base.metadata,
    Column("exam_id", Integer, ForeignKey("exams.id"), primary_key=True),
    Column("group_id", Integer, ForeignKey("groups.id"), primary_key=True)
)
