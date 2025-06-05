from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from security.rbac import student_only


router = APIRouter()


@router.get("/exams", 
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
def exams_page(request: Request,
               status: str = ""):
    return templates.TemplateResponse("student/exam/exams.html", {"request": request})


@router.get("/exams/{exam_id}/exam_page", 
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
def exam_page(exam_id: int,
              request: Request):
    return templates.TemplateResponse("student/exam/exam-page.html", {"request": request})
