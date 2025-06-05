import jwt
from datetime import datetime, timedelta, timezone
from jose import jwt
from passlib.context import CryptContext
from typing import Optional

from sqlalchemy.orm import Session

from utils.exceptions.auth import InvalidCredentialsException
from models.schemas.user import UserLogin
from models.db_models.user import User
from models.schemas.schemas import TokenResponse
from security.config import SECRET_KEY, ALGORITHM

ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    datetime.now(timezone.utc)
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def authenticate_user(user_data: UserLogin, db: Session):
    user = db.query(User).filter(User.username == user_data.username).first()

    if not user or not verify_password(user_data.password, user.hashed_password):
        raise InvalidCredentialsException

    if user.role == "student":
        token = create_access_token(data={"sub": user.username, "role": user.role, "group_id": user.group_id})
    else:
        token = create_access_token(data={"sub": user.username, "role": user.role})

    return TokenResponse(
        access_token=token,
        token_type="bearer",
        role=user.role
    )
