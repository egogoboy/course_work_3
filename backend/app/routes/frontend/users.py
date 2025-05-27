from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from core.templates import templates

router = APIRouter()


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
