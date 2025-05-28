from fastapi import APIRouter

from routes.frontend.user.base import router as base_router


router = APIRouter(prefix="/student")

router.include_router(base_router)
