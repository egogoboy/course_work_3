from fastapi import APIRouter

from routes.api.common.router import router as common_router
from routes.api.admin.router import router as admin_router
from routes.api.teacher.router import router as teacher_router
from routes.api.student.router import router as student_router


router = APIRouter(prefix = "/api", tags=["api"])


router.include_router(common_router)
router.include_router(admin_router)
router.include_router(teacher_router)
router.include_router(student_router)
