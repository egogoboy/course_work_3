from fastapi import FastAPI
from routes.users import router as user_router
from routes.admin import router as admin_table_router
from routes.exams import router as exam_router
from database.startup import init_db

app = FastAPI()
init_db()
app.include_router(user_router, prefix="/auth")
app.include_router(admin_table_router, prefix="/adm")
app.include_router(exam_router, prefix="/exam")
