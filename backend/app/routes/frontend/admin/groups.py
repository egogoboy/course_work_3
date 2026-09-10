from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import admin_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/groups", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def groups_page(request: Request):
    return templates.TemplateResponse(request, "admin/group/groups.html")

@router.get("/groups/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def group_create_page(request: Request):
    return templates.TemplateResponse(request, "admin/group/create_group.html")

@router.get("/groups/edit/{group_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def group_edit_page(group_id: int,
                    request: Request):
    return templates.TemplateResponse(request, "admin/group/edit_group.html")
