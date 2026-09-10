from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import admin_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse(request, "admin/dashboard.html")
