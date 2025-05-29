from fastapi import APIRouter

from routes.api.teacher import exams, tasks


router = APIRouter(prefix = "/teacher", tags=["teacher"])


router.include_router(exams.router, prefix="/exams")
router.include_router(tasks.router, prefix="/tasks")
