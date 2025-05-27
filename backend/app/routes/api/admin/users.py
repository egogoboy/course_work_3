from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user import update_user
from models.schemas.schemas import TokenResponse
from models.schemas.common import APIResponse
from models.schemas.user import UserCreate, UserOut, UserUpdate
from utils.exceptions.user import UserNotFoundException
from crud.user import get_user_by_id
from models.db_models.user import User
from sequrity.auth import get_db, create_user
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/users", 
            response_model=APIResponse[Union[list[UserOut], None]], 
            dependencies=[Depends(admin_only)])
async def get_all_users_endpoint(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return APIResponse(data=[UserOut.model_validate(user) for user in users])


@router.get("/user/{user_id}", 
            response_model=APIResponse[Union[UserOut, None]], 
            dependencies=[Depends((admin_only))])
async def get_user_endpoint(user_id: int, 
                   db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)

    if user is None:
        raise UserNotFoundException

    return APIResponse(data=user)


@router.post("/delete_user/{user_id}", 
             response_model=APIResponse[Union[UserOut, None]], 
             dependencies=[Depends(admin_only)])
def delete_user_endpoint(user_id: int, 
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
async def register_user_endpoint(user: UserCreate, 
                   db: Session = Depends(get_db)):
    return APIResponse(data=create_user(user, db))


@router.put("/edit/{user_id}",
             response_model=APIResponse[Union[UserOut, None]],
             dependencies=[Depends(admin_only)])
async def edit_user_endpoint(user_id: int,
                             new_user_data: UserUpdate,
                             db: Session = Depends(get_db)):
    updated_user = update_user(user_id, new_user_data, db)

    if updated_user is None:
        raise UserNotFoundException

    return APIResponse(data=UserOut.model_validate(updated_user, from_attributes=True))
