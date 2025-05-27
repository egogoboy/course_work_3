from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sequrity.auth import authenticate_user, get_db
from models.schemas.user import UserLogin

from sequrity.rbac import get_current_user


router = APIRouter()


@router.get("/me")
async def get_current_user_info(current_user=Depends(get_current_user)):
    return current_user


@router.post("/login")
async def login(user: UserLogin, 
                db: Session = Depends(get_db)):
    return authenticate_user(user, db)
