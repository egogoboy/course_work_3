from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/users", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def users_page(request: Request):
    return templates.TemplateResponse("admin/user/users.html", {"request": request})


@router.get("/users/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def user_create_page(request: Request):
    return templates.TemplateResponse("admin/user/create_user.html", {"request": request})


@router.get("/users/edit/{user_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def user_edit_page(user_id: int,
                     request: Request):
    return templates.TemplateResponse("admin/user/edit_user.html", {"request": request, "user_id": user_id})
