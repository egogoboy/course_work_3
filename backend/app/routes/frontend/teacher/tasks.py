from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import teacher_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/tasks/{exam_id}/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def tasks_create_page(request: Request):
    return templates.TemplateResponse(request, "teacher/task/create_tasks.html")


@router.get("/tasks/{exam_id}/edit", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def tasks_edit_page(request: Request):
    return templates.TemplateResponse(request, "teacher/task/edit_tasks.html")
