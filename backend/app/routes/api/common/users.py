from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sequrity.auth import authenticate_user, get_db
from models.schemas.common import APIResponse
from models.schemas.user import UserLogin
from models.schemas.schemas import TokenResponse


router = APIRouter()


@router.post("/login", 
             response_model=APIResponse[Union[TokenResponse]])
async def login(user: UserLogin, 
                db: Session = Depends(get_db)):
    return APIResponse(data=authenticate_user(user, db))
