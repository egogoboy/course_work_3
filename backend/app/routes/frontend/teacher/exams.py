from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import teacher_only


router = APIRouter()


@router.get("/exams", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exams_page(request: Request):
    return templates.TemplateResponse("teacher/exam/exams.html", {"request": request})

@router.get("/exams/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_create_page(request: Request):
    return templates.TemplateResponse("teacher/exam/create_exam.html", {"request": request})

@router.get("/exams/edit/{exam_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_edit_page(exam_id: int,
                    request: Request):
    return templates.TemplateResponse("teacher/exam/edit_exam.html", {"request": request, "exam_id": exam_id})
