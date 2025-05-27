from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.group import create_group, get_all_groups
from models.schemas.group import GroupCreate
from sequrity.auth import get_db
from sequrity.rbac import admin_only


router = APIRouter()


@router.post("/create", 
             dependencies=[Depends(admin_only)])
async def create_group_endpoint(group: GroupCreate,
                       db: Session = Depends(get_db)):
    created_group = create_group(group, db)
    return created_group


@router.get("/", 
            dependencies=[Depends(admin_only)])
async def get_all_groups_endpoint(db: Session = Depends(get_db)):
    return get_all_groups(db)
