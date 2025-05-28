from fastapi import APIRouter

from routes.frontend.teacher.base import router as base_router


router = APIRouter(prefix="/teacher")

router.include_router(base_router)
