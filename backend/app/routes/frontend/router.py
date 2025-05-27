from fastapi import APIRouter

from routes.frontend import exams, users, base


router = APIRouter(tags=["frontend"])


router.include_router(exams.router, prefix="/exams")
router.include_router(users.router)
router.include_router(base.router, prefix="/admin")
