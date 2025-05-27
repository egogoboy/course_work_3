from fastapi import APIRouter

from routes.api.admin import groups, users


router = APIRouter(prefix = "/admin", tags=["admin"])


router.include_router(groups.router, prefix="/groups")
router.include_router(users.router, prefix="/users")
