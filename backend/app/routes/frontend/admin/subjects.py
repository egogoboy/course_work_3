from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import admin_only


router = APIRouter()


@router.get("/subjects", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subjects_page(request: Request):
    return templates.TemplateResponse("admin/subject/subjects.html", {"request": request})

@router.get("/subjects/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subject_create_page(request: Request):
    return templates.TemplateResponse("admin/subject/create_subject.html", {"request": request})

@router.get("/subjects/edit/{subject_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subject_edit_page(subject_id: int,
                    request: Request):
    return templates.TemplateResponse("admin/subject/edit_subject.html", {"request": request, "subject_id": subject_id})
