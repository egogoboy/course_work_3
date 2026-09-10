from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import admin_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/subjects", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subjects_page(request: Request):
    return templates.TemplateResponse(request, "admin/subject/subjects.html")

@router.get("/subjects/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subject_create_page(request: Request):
    return templates.TemplateResponse(request, "admin/subject/create_subject.html")

@router.get("/subjects/edit/{subject_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(admin_only)])
def subject_edit_page(subject_id: int,
                    request: Request):
    return templates.TemplateResponse(request, "admin/subject/edit_subject.html")
