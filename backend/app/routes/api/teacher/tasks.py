import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.db_models.task import Task
from models.schemas.task import TaskBulkCreate, TaskOut
from crud.task import add_tasks, delete_task, get_exam_tasks
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


@router.get("/{exam_id}",
            response_model=list[TaskOut],
            dependencies=[Depends(teacher_only)])
async def get_exam_tasks_endpoint(exam_id: int,
                         db: Session = Depends(get_db)):
    
    tasks = await get_exam_tasks(exam_id, db)

    return list(TaskOut.model_validate(task) for task in tasks)


@router.delete("/{task_id}",
            response_model=TaskOut,
            dependencies=[Depends(teacher_only)])
async def delete_task_endpoint(task_id: int,
                         db: Session = Depends(get_db)):
    return await delete_task(task_id, db)
