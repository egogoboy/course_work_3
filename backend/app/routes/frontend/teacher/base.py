from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import teacher_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse(request, "teacher/dashboard.html")
