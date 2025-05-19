from fastapi import FastAPI
from users import router as user_router

app = FastAPI()
app.include_router(user_router, prefix="/auth")
