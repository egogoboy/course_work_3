from sqlalchemy.orm import Session

from models.db_models.user import User
from models.schemas.user import UserUpdate

def update_user(user_id: int, 
                update_data: UserUpdate, 
                db: Session):

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return None

    for field, value in update_data.model_dump(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user


def get_user_by_id(user_id: int, 
                   db: Session):
    return db.query(User).filter(User.id == user_id).first()
