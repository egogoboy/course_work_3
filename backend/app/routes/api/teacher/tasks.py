from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.task import TaskCreate, TaskOut
from crud.task import create_task
from sequrity.auth import get_db
from sequrity.rbac import teacher_only

router = APIRouter()

@router.post("/{exam_id}/create", 
             response_model=TaskOut, 
             dependencies=[Depends(teacher_only)])
async def create_task_endpoint(exam_id: int,
                               task: TaskCreate,
                               db: Session = Depends(get_db)):
    task.exam_id = exam_id
    return await create_task(task, db)
