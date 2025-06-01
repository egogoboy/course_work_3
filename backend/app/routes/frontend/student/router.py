from fastapi import APIRouter

from routes.frontend.student.base import router as base_router
from routes.frontend.student.exams import router as exam_router


router = APIRouter(prefix="/student")

router.include_router(base_router)
router.include_router(exam_router)
