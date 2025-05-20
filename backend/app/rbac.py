from functools import wraps
from fastapi import Depends
from jose import JWTError, jwt

from models import User
from database import SessionLocal
from config import SECRET_KEY, ALGORITHM, oauth2_scheme 
from exceptions import AuthenticationRequiredException, NotEnoughRightsException

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
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


def role_checker(roles: list[str]):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, user: User = Depends(get_current_user), **kwargs):
            if user.role not in roles:
                raise NotEnoughRightsException
            return await func(*args, user=user, **kwargs)
        return wrapper
    return decorator
