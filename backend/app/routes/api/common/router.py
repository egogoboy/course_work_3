from fastapi import APIRouter

from routes.api.common import exams, users, tasks, subjects, marks


router = APIRouter(prefix = "/common", tags=["common"])


router.include_router(exams.router, prefix="/exams")
router.include_router(tasks.router, prefix = "/tasks")
router.include_router(subjects.router, prefix = "/subjects")
router.include_router(users.router)
router.include_router(marks.router)
