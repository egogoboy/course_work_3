from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import admin_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/users", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def users_page(request: Request):
    return templates.TemplateResponse(request, "admin/user/users.html")


@router.get("/users/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def user_create_page(request: Request):
    return templates.TemplateResponse(request, "admin/user/create_user.html")


@router.get("/users/edit/{user_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def user_edit_page(user_id: int,
                     request: Request):
    return templates.TemplateResponse(request, "admin/user/edit_user.html")
