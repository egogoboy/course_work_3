from functools import wraps
from typing import Optional
from fastapi import Depends, Request
from jose import JWTError, jwt

from sqlalchemy.orm import Session

from sequrity.auth import get_db
from models.db_models.user import User
from sequrity.config import SECRET_KEY, ALGORITHM
from utils.exceptions.auth import AuthenticationRequiredException
from utils.exceptions.rbac import NotEnoughRightsException

async def get_current_user(
    request: Request,
    db: Session = Depends(get_db)):
    credentials_exception = AuthenticationRequiredException()

    token: Optional[str] = None

    # 1) Пытаемся взять токен из cookie
    token = request.cookies.get("access_token")
    if token and token.startswith("Bearer "):
        token = token[len("Bearer "):]

    # 2) Если в cookie токена нет, смотрим в заголовках Authorization
    if not token:
        auth_header = request.headers.get("Authorization")
        if auth_header and auth_header.lower().startswith("bearer "):
            token = auth_header[7:]  # отрезаем "Bearer "

    if not token:
        raise credentials_exception

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception

    return user

class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    async def __call__(self, user: User = Depends(get_current_user)):
        if user.role not in self.allowed_roles:
            raise NotEnoughRightsException


def role_checker(roles: list[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, user: User = Depends(get_current_user), **kwargs):
            if user.role not in roles:
                raise NotEnoughRightsException
            return await func(*args, user=user, **kwargs)
        return wrapper
    return decorator


admin_only = RoleChecker(['admin'])
teacher_only = RoleChecker(['teacher'])
student_only = RoleChecker(['student'])
