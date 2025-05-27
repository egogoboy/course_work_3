from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def exams_page(request: Request):
    return templates.TemplateResponse("exams.html", {"request": request})
