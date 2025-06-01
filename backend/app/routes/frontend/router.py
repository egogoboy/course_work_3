from fastapi import APIRouter

from routes.frontend.auth import router as auth_router
from routes.frontend.student.router import router as student_router
from routes.frontend.admin.router import router as admin_router
from routes.frontend.teacher.router import router as teacher_router


router = APIRouter(tags=["frontend"])


router.include_router(auth_router)
router.include_router(student_router)
router.include_router(admin_router)
router.include_router(teacher_router)
