from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from security.rbac import teacher_only


router = APIRouter()


@router.get("/tasks/{exam_id}/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def tasks_create_page(request: Request):
    return templates.TemplateResponse("teacher/task/create_tasks.html", {"request": request})


@router.get("/tasks/{exam_id}/edit", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def tasks_edit_page(request: Request):
    return templates.TemplateResponse("teacher/task/edit_tasks.html", {"request": request})
