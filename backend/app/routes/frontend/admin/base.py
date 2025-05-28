from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request})
