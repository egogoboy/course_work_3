from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from security.rbac import student_only


router = APIRouter()


@router.get("/home",
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse("student/dashboard.html", {"request": request})
