from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.task import TaskBulkCreate, TaskOut
from crud.task import add_tasks, delete_task, get_current_task
from crud.answers import set_correctly
from sequrity.auth import get_db
from sequrity.rbac import teacher_only

router = APIRouter()

@router.post("/{exam_id}/create", 
             response_model=dict, 
             dependencies=[Depends(teacher_only)])
async def create_task_endpoint(exam_id: int,
                               data: TaskBulkCreate,
                               db: Session = Depends(get_db)):
    return await add_tasks(exam_id, data, db)


@router.get("/{task_id}",
            response_model=TaskOut,
            dependencies=[Depends(teacher_only)])
async def get_current_task_endpoint(task_id: int,
                                    db: Session = Depends(get_db)):
    return await get_current_task(task_id, db)


@router.delete("/{task_id}",
            response_model=TaskOut,
            dependencies=[Depends(teacher_only)])
async def delete_task_endpoint(task_id: int,
                         db: Session = Depends(get_db)):
    return await delete_task(task_id, db)
