from fastapi import APIRouter, FastAPI

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from database.startup import init_db

from routes.api.router import router as api_router
from routes.frontend.router import router as frontend_router

app = FastAPI()

# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


init_db()
app.include_router(api_router)
app.include_router(frontend_router)
