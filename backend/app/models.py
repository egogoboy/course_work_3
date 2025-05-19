from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional
from pydantic import BaseModel


class Role(str, Enum):
    student = "student"
    teacher = "teacher"
    admin = "admin"


# Полиморфизм через базовый класс
class UserBase(ABC):
    def __init__(self, username: str, role: Role):
        self.username = username
        self.role = role

    @abstractmethod
    def get_permissions(self) -> list[str]:
        pass


class Student(UserBase):
    def get_permissions(self):
        return ["view_profile", "view_exams"]


class Teacher(UserBase):
    def get_permissions(self):
        return ["view_profile", "create_exam", "view_students"]


class Admin(UserBase):
    def get_permissions(self):
        return ["create_user", "delete_user", "edit_exam", "delete_exam"]
