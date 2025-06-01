from fastapi import APIRouter

from routes.frontend.admin.base import router as base_router
from routes.frontend.admin.users import router as users_router
from routes.frontend.admin.groups import router as groups_router
from routes.frontend.admin.subjects import router as subjects_router

router = APIRouter(prefix = "/admin", tags=["admin"])

router.include_router(base_router)
router.include_router(users_router)
router.include_router(groups_router)
router.include_router(subjects_router)
