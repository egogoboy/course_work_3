import os
from fastapi import FastAPI
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from apscheduler.schedulers.background import BackgroundScheduler

from database.startup import init_db
from routes.api.router import router as api_router
from routes.frontend.router import router as frontend_router
from fastapi import FastAPI
from utils.scheduler import update_exam_statuses

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # exam-system/
FRONTEND_DIR = BASE_DIR / "frontend"

templates = Jinja2Templates(directory=os.path.join(FRONTEND_DIR / "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR / "static")), name="static")

init_db()
app.include_router(api_router)
app.include_router(frontend_router)

scheduler = BackgroundScheduler()
scheduler.add_job(update_exam_statuses, "interval", seconds=30)  # каждые 30 секунд
scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
