from fastapi import APIRouter

from routes.frontend.teacher.base import router as base_router
from routes.frontend.teacher.exams import router as exam_router
from routes.frontend.teacher.tasks import router as task_router


router = APIRouter(prefix="/teacher")

router.include_router(base_router)
router.include_router(exam_router)
router.include_router(task_router)
