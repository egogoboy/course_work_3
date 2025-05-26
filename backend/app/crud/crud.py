from fastapi import Depends
from sqlalchemy.orm import Session
from models.db_models.user import User
from sequrity.auth import get_db

def get_user_by_id(user_id: int, 
                   db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()

