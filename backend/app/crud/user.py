from sqlalchemy.orm import Session

from security.auth import create_access_token, get_password_hash
from utils.exceptions.user import UserAlreadyExistsException, UserNotFoundException
from models.db_models.user import User
from models.schemas.user import UserCreate, UserOut, UserUpdate
from models.schemas.schemas import TokenResponse
from utils.log import MessageLogger, consoleLog


class crudUser:
    @staticmethod
    async def is_existing_user(user: UserCreate,
                               db: Session):
        user = db.query(User).filter(User.username == user.username).first()

        return (user is not None)


    @staticmethod
    @MessageLogger
    async def update_user(user_id: int, 
                          update_data: UserUpdate, 
                          db: Session):
        user = await crudUser._get_user_from_db(user_id, db)

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


    @staticmethod
    def get_user_by_id(user_id: int, 
                       db: Session):
        return db.query(User).filter(User.id == user_id).first()


    @staticmethod
    def create_user(user_data: UserCreate, db: Session):
        existing_user = db.query(User).filter(User.username == user_data.username).first()
        if existing_user:
            raise UserAlreadyExistsException

        hashed_password = get_password_hash(user_data.password)
        user_data.password = hashed_password
        new_user = User.from_schemas(user_data)

        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        db.commit()

        token = create_access_token(data={"sub": new_user.username, "role": new_user.role})
        return TokenResponse(
            access_token=token,
            token_type="bearer",
            role=user_data.role
        )


    @staticmethod
    async def _get_user_from_db(user_id: int,
                          db: Session):
        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise UserNotFoundException

        return user
