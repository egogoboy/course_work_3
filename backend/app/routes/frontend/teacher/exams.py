from core.templates import templates
from fastapi import APIRouter, Depends, Request
from security.rbac import teacher_only
from starlette.responses import HTMLResponse

router = APIRouter(prefix="/exams")


@router.get("/", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exams_page(request: Request,
               status: str = "all"): return templates.TemplateResponse(request, "teacher/exam/exams.html")

@router.get("/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_create_page(request: Request):
    return templates.TemplateResponse(request, "teacher/exam/create_exam.html")


@router.get("/edit/{exam_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_edit_page(exam_id: int,
                    request: Request):
    return templates.TemplateResponse(request, "teacher/exam/edit_exam.html")


@router.get("/{exam_id}/results",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_results_page(exam_id: int,
                      request: Request):
    return templates.TemplateResponse(request, "teacher/exam/exam_results.html")


@router.get("/{exam_id}/results/{user_id}",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def user_results_page(exam_id: int,
                      user_id: int,
                      request: Request):
    return templates.TemplateResponse(
        request, 
        "teacher/exam/user_results.html", 
        {"exam_id": exam_id, "user_id": user_id}
    )
