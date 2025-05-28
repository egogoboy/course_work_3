from fastapi import APIRouter

from routes.frontend import users
from routes.frontend.admin.router import router as admin_router


router = APIRouter(tags=["frontend"])


router.include_router(users.router)
router.include_router(admin_router, prefix="/admin")
