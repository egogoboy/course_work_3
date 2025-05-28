from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/groups", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def groups_page(request: Request):
    return templates.TemplateResponse("admin/group/groups.html", {"request": request})

@router.get("/groups/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def group_create_page(request: Request):
    return templates.TemplateResponse("admin/group/create_group.html", {"request": request})

@router.get("/groups/edit/{group_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def group_edit_page(group_id: int,
                    request: Request):
    return templates.TemplateResponse("admin/group/edit_group.html", {"request": request, "group_id": group_id})
