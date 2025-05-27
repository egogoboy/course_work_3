from pathlib import Path
from fastapi.templating import Jinja2Templates
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # exam-system/
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")
TEMPLATES_DIR = os.path.join(FRONTEND_DIR, "templates")

templates = Jinja2Templates(directory=TEMPLATES_DIR)
