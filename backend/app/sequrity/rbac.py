from functools import wraps
from fastapi import Depends, Request
from fastapi.responses import RedirectResponse
from jose import JWTError, jwt

from starlette.status import HTTP_303_SEE_OTHER

from models.db_models.user import User
from models.schemas.user import UserOut
from database.database import SessionLocal
from sequrity.config import SECRET_KEY, ALGORITHM, oauth2_scheme 
from utils.exceptions.auth import AuthenticationRequiredException
from utils.exceptions.rbac import NotEnoughRightsException

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserOut:
    credentials_exception = AuthenticationRequiredException()

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    db = SessionLocal()
    user = db.query(User).filter(User.username == username).first()
    db.close()
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


admin_only = RoleChecker(["admin"])
teacher_only = RoleChecker(['teacher'])
