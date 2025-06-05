from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.task import TaskBulkCreate, TaskOut
from crud.task import crudTask
from database.database import get_db
from security.rbac import teacher_only

router = APIRouter()

@router.post("/{exam_id}/create", 
             response_model=dict, 
             dependencies=[Depends(teacher_only)])
async def create_task_endpoint(exam_id: int,
                               data: TaskBulkCreate,
                               db: Session = Depends(get_db)):
    return await crudTask.add_tasks(exam_id, data, db)


@router.get("/{task_id}",
            response_model=TaskOut,
            dependencies=[Depends(teacher_only)])
async def get_current_task_endpoint(task_id: int,
                                    db: Session = Depends(get_db)):
    return await crudTask.get_current_task(task_id, db)


@router.delete("/{task_id}",
            response_model=TaskOut,
            dependencies=[Depends(teacher_only)])
async def delete_task_endpoint(task_id: int,
                         db: Session = Depends(get_db)):
    return await crudTask.delete_task(task_id, db)
