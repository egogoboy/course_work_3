from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sequrity.auth import authenticate_user, get_db
from models.schemas.common import APIResponse
from models.schemas.user import UserLogin, UserOut
from models.schemas.schemas import TokenResponse

from sequrity.rbac import get_current_user


router = APIRouter()


@router.get("/me", response_model=APIResponse[UserOut])
async def get_current_user_info(current_user=Depends(get_current_user)):
    return APIResponse(data=current_user)


@router.post("/login", 
             response_model=APIResponse[Union[TokenResponse]])
async def login(user: UserLogin, 
                db: Session = Depends(get_db)):
    return APIResponse(data=authenticate_user(user, db))
