from fastapi import FastAPI
from sqlalchemy import engine
from database import Base
from users import router as user_router
from startup import init_db

app = FastAPI()
init_db()
app.include_router(user_router, prefix="/auth")
