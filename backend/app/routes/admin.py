from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.schemas.schemas import TokenResponse
from models.schemas.common import APIResponse
from utils.exceptions import UserNotFoundException
from crud.crud import get_user_by_id
from models.db_models.user import User
from models.schemas.user import UserCreate, UserOut
from sequrity.auth import get_db, create_user
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/users", 
            response_model=APIResponse[Union[list[UserOut], None]], 
            dependencies=[Depends(admin_only)])
async def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return APIResponse(data=[UserOut.model_validate(user) for user in users])


@router.get("/user/{user_id}", 
            response_model=APIResponse[Union[UserOut, None]], 
            dependencies=[Depends((admin_only))])
async def get_user(user_id: int, 
                   db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)

    if user is None:
        raise UserNotFoundException

    return APIResponse(data=user)


@router.post("/delete_user/{user_id}", 
             response_model=APIResponse[Union[UserOut, None]], 
             dependencies=[Depends(admin_only)])
def delete_user(user_id: int, 
                db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if user is None:
        raise UserNotFoundException
    db.delete(user)
    db.commit()

    return APIResponse(data=user)


@router.post("/register", 
             response_model=APIResponse[Union[TokenResponse]],
             dependencies=[Depends(admin_only)])
async def register(user: UserCreate, 
                   db: Session = Depends(get_db)):
    return APIResponse(data=create_user(user, db))
