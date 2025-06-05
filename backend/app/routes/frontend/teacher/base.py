from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import teacher_only


router = APIRouter()


@router.get("/",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse("teacher/dashboard.html", {"request": request})
