from fastapi import APIRouter

from routes.api.common import exams, users


router = APIRouter(prefix = "/common", tags=["common"])


router.include_router(exams.router, prefix="/exams")
router.include_router(users.router)
