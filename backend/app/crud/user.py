from sqlalchemy.orm import Session

from sequrity.auth import get_password_hash
from utils.exceptions.user import UserNotFoundException
from models.db_models.user import User
from models.schemas.user import UserOut, UserUpdate
from utils.log import MessageLogger, consoleLog

@MessageLogger
async def update_user(user_id: int, 
                update_data: UserUpdate, 
                db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise UserNotFoundException

    update_dict = update_data.model_dump(exclude_unset=True)

    if "password" in update_dict:
        raw_password = update_dict.pop("password")
        user.password = get_password_hash(raw_password)

    for field, value in update_dict.items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)

    consoleLog(f"User {user_id} has been updated succesfully")
    consoleLog(f"New data: {update_dict}")

    return UserOut.model_validate(user)


def get_user_by_id(user_id: int, 
                   db: Session):
    return db.query(User).filter(User.id == user_id).first()
