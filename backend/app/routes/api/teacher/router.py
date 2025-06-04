from fastapi import APIRouter

from routes.api.teacher import exams, tasks, exam_results, answers, marks


router = APIRouter(prefix = "/teacher", tags=["teacher"])


router.include_router(exams.router, prefix="/exams")
router.include_router(tasks.router, prefix="/tasks")
router.include_router(exam_results.router)
router.include_router(exam_results.router)
router.include_router(answers.router)
router.include_router(marks.router)
