from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import student_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/home",
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse(request, "student/dashboard.html")
