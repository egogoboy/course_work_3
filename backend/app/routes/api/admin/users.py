from typing import Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.user import update_user
from models.schemas.user import UserCreate, UserOut, UserUpdate
from utils.exceptions.user import UserNotFoundException
from crud.user import get_user_by_id, create_user
from models.db_models.user import User
from security.rbac import admin_only
from database.database import get_db


router = APIRouter()


@router.get("/", 
            dependencies=[Depends(admin_only)])
async def get_all_users_endpoint(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return (UserOut.model_validate(user) for user in users)


@router.get("/{user_id}", 
            dependencies=[Depends((admin_only))])
async def get_user_endpoint(user_id: int, 
                   db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)

    if user is None:
        raise UserNotFoundException

    return user

@router.delete("/{user_id}", 
             dependencies=[Depends(admin_only)])
def delete_user_endpoint(user_id: int, 
                db: Session = Depends(get_db)):
    user = get_user_by_id(user_id, db)
    if user is None:
        raise UserNotFoundException
    db.delete(user)
    db.commit()

    return user


@router.post("/create",
             dependencies=[Depends(admin_only)])
async def register_user_endpoint(user: UserCreate, 
                   db: Session = Depends(get_db)):
    return create_user(user, db)


@router.put("/{user_id}",
             dependencies=[Depends(admin_only)])
async def edit_user_endpoint(user_id: int,
                             new_user_data: UserUpdate,
                             db: Session = Depends(get_db)):
    return await update_user(user_id, new_user_data, db)
