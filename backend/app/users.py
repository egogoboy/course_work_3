from fastapi import APIRouter, Depends
from schemas import UserCreate, UserLogin, TokenResponse, Role
from auth import get_password_hash, verify_password, create_access_token
from exceptions import UserAlreadyExistsException, InvalidCredentialsException

fake_users_db = {}  # Простая in-memory "БД"

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
def register(user: UserCreate):
    if user.username in fake_users_db:
        raise UserAlreadyExistsException()

    hashed_password = get_password_hash(user.password)
    fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_password,
        "role": user.role
    }

    token = create_access_token(data={"sub": user.username, "role": user.role})
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    db_user = fake_users_db.get(user.username)
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise InvalidCredentialsException()

    token = create_access_token(data={"sub": user.username, "role": db_user["role"]})
    return TokenResponse(access_token=token)
