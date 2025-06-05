from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.schemas.task import TaskOut
from crud.task import get_exam_tasks
from database.database import get_db
from security.rbac import all_users

router = APIRouter()

@router.get("/{exam_id}",
            response_model=list[TaskOut],
            dependencies=[Depends(all_users)])
async def get_exam_tasks_endpoint(exam_id: int,
                         db: Session = Depends(get_db)):
    
    tasks = await get_exam_tasks(exam_id, db)

    return list(TaskOut.model_validate(task) for task in tasks)
