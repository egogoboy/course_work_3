from fastapi import APIRouter

from routes.frontend.admin.base import router as base_router
from routes.frontend.admin.users import router as users_router
from routes.frontend.admin.groups import router as groups_router
from routes.frontend.admin.exams import router as exams_router

router = APIRouter(prefix = "admin", tags=["admin"])

router.include_router(base_router)
router.include_router(users_router)
router.include_router(groups_router)
router.include_router(exams_router)
