from fastapi import APIRouter, Depends, Request, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sequrity.auth import authenticate_user, get_db
from models.schemas.user import UserLogin

from sequrity.rbac import get_current_user


router = APIRouter()


@router.get("/me")
async def get_current_user_info(request: Request,
                                current_user=Depends(get_current_user)):
    # Выведем заголовки запроса
    print("Headers:", request.headers)

    # Выведем cookie (там может быть токен)
    print("Cookies:", request.cookies)

    # Выведем, если есть, Authorization header
    auth = request.headers.get("Authorization")
    print("Authorization header:", auth)
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
