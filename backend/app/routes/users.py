from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sequrity.rbac import role_checker
from sequrity.auth import authenticate_user, register_user, get_db
from models.schemas import UserCreate, UserLogin, TokenResponse

router = APIRouter()


@router.post("/register", response_model=TokenResponse)
@role_checker(["admin"])
async def register(user: UserCreate, 
                   db: Session = Depends(get_db)):
    return register_user(user, db)


@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    return authenticate_user(user, db)
