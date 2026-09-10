from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import student_only
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/exams", 
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
def exams_page(request: Request,
               status: str = ""):
    return templates.TemplateResponse(request, "student/exam/exams.html")


@router.get("/exams/{exam_id}/exam_page", 
            response_class=HTMLResponse,
            dependencies=[Depends(student_only)])
def exam_page(exam_id: int,
              request: Request):
    return templates.TemplateResponse(request, "student/exam/exam-page.html")
