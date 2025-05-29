import json
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.db_models.task import Task
from models.schemas.task import TaskBulkCreate, TaskOut
from crud.task import add_tasks
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
async def get_exam_tasks(exam_id: int,
                         db: Session = Depends(get_db),):
    tasks = db.query(Task).filter(Task.exam_id == exam_id).all()
    for task in tasks:
        print(task.title)
        print(task.body)
        print("options from DB type:", type(task.options), "value:", task.options)

    return list(TaskOut.model_validate(task) for task in tasks)


@router.post("/fix-options")
def fix_options(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    for task in tasks:
        if isinstance(task.options, list):
            continue
        try:
            task.options = json.loads(task.options)
        except:
            task.options = []
    db.commit()
    return {"message": "Fixed"}
