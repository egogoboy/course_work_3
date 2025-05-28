from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from core.templates import templates


router = APIRouter()


@router.get("/exams", response_class=HTMLResponse)
async def exams_page(request: Request):
    return templates.TemplateResponse("admin/exam/exams.html", {"request": request})
