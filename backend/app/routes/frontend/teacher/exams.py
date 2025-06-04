from fastapi import APIRouter, Depends, Request
from starlette.responses import HTMLResponse

from core.templates import templates
from sequrity.rbac import teacher_only


router = APIRouter(prefix="/exams")


@router.get("/", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exams_page(request: Request,
               status: str = "all"): return templates.TemplateResponse("teacher/exam/exams.html", {"request": request})

@router.get("/create", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_create_page(request: Request):
    return templates.TemplateResponse("teacher/exam/create_exam.html", {"request": request})


@router.get("/edit/{exam_id}", 
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_edit_page(exam_id: int,
                    request: Request):
    return templates.TemplateResponse("teacher/exam/edit_exam.html", {"request": request, "exam_id": exam_id})


@router.get("/{exam_id}/results",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def exam_results_page(exam_id: int,
                      request: Request):
    return templates.TemplateResponse("teacher/exam/exam_results.html", {"request": request, "exam_id": exam_id})


@router.get("/{exam_id}/results/{user_id}",
            response_class=HTMLResponse,
            dependencies=[Depends(teacher_only)])
def user_results_page(exam_id: int,
                      user_id: int,
                      request: Request):
    return templates.TemplateResponse("teacher/exam/user_results.html", 
                                      {"request": request, "exam_id": exam_id, "user_id": user_id})
