from fastapi import APIRouter

from routes.api.teacher import exams


router = APIRouter(prefix = "/teacher", tags=["teacher"])


router.include_router(exams.router, prefix="/exams")
