from fastapi import FastAPI
from routes.users import router as user_router
from database.startup import init_db

app = FastAPI()
init_db()
app.include_router(user_router, prefix="/auth")
