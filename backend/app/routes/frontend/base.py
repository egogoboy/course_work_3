from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates


router = APIRouter()


@router.get("/", 
            response_class=HTMLResponse)
#             dependencies=[Depends(admin_only)])
async def dashboard_page(request: Request):
    return templates.TemplateResponse("admin/dashboard.html", {"request": request})

@router.get("/users", 
            response_class=HTMLResponse)
#             dependencies=[Depends(admin_only)])
def users_page(request: Request):
    return templates.TemplateResponse("admin/users.html", {"request": request})


@router.get("/groups", 
            response_class=HTMLResponse)
#             dependencies=[Depends(admin_only)])
def groups_page(request: Request):
    return templates.TemplateResponse("admin/groups.html", {"request": request})

@router.get("/groups/create", 
            response_class=HTMLResponse)
#             dependencies=[Depends(admin_only)])
def group_create_page(request: Request):
    return templates.TemplateResponse("admin/create_group.html", {"request": request})

@router.get("/exams", 
            response_class=HTMLResponse)
#             dependencies=[Depends(admin_only)])
def exams_page(request: Request):
    return templates.TemplateResponse("admin/exams.html", {"request": request})
