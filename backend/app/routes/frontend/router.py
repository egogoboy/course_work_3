from fastapi import APIRouter

from routes.frontend import exams, users


router = APIRouter(tags=["frontend"])


router.include_router(exams.router, prefix="/exams")
router.include_router(users.router)
