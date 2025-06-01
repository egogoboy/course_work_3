from fastapi import APIRouter

from routes.api.student.exams import router as exam_router
from routes.api.student.answers import router as answer_router

router = APIRouter(prefix = "/student", tags=["student"])


router.include_router(exam_router, prefix="/exams")
router.include_router(answer_router, prefix="/answers")
