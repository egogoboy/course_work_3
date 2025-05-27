from fastapi import FastAPI
from routes.users import router as user_router
from routes.admin.user_routes import router as admin_user_router
from routes.admin.group_routes import router as admin_group_router
from routes.exams import router as exam_router
from database.startup import init_db

app = FastAPI()
init_db()
app.include_router(user_router, prefix="/auth")
app.include_router(admin_user_router, prefix="/adm/users")
app.include_router(admin_group_router, prefix="/adm/groups")
app.include_router(exam_router, prefix="/exam")
