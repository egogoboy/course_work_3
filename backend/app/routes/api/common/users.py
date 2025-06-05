from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from security.auth import authenticate_user
from database.database import get_db
from models.schemas.user import UserLogin

from security.rbac import get_current_user


router = APIRouter()


@router.get("/me")
async def get_current_user_info(request: Request,
                                current_user=Depends(get_current_user)):

    auth = request.headers.get("Authorization")
    return current_user


@router.post("/login")
async def login(user: UserLogin, 
                db: Session = Depends(get_db)):

    result = authenticate_user(user, db)

    res = JSONResponse(content={
            "message": "Login successful", 
            "role": result.role})

    res.set_cookie(
        key="access_token",
        value=f"Bearer {result.access_token}",
        httponly=True,
        samesite="lax",
        max_age=3600,
        path="/"
    )

    return res
