from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from rbac import role_checker
from schemas import UserCreate, UserLogin, TokenResponse
from auth import authenticate_user, register_user, get_db

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
@role_checker(["admin"])
async def register(user: UserCreate, 
                   db: Session = Depends(get_db)):
    return register_user(user, db)


@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(user, db)
