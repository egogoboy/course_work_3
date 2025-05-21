from abc import ABC, abstractmethod
from enum import Enum
from sqlalchemy import Column, Integer, String

from database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)


class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


class Permissions(str, Enum):
    view_profile = "view_profile"
    view_exams = "view_exams"
    view_students = "view_students"
    view_users = "view_users"

    create_exam = "create_exam"
    create_user = "create_user"

    edit_exam = "edit_exam"

    delete_user = "delete_user"
    delete_exam = "delete_exam"


# Plymorphism trought base class
class UserBase(ABC):
    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    @abstractmethod
    def get_permissions(self) -> list[Permissions]:
        pass


class Student(UserBase):
    def get_permissions(self):
        return [Permissions.view_profile, 
                Permissions.view_exams]


class Teacher(UserBase):
    def get_permissions(self):
        return [Permissions.view_profile, 
                Permissions.create_exam, 
                Permissions.view_students]


class Admin(UserBase):
    def get_permissions(self):
        return [Permissions.view_users,
                Permissions.create_user, 
                Permissions.delete_user, 
                Permissions.edit_exam, 
                Permissions.delete_exam]
