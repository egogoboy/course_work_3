from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.group import create_group, get_all_groups
from models.schemas.common import APIResponse
from models.schemas.group import GroupCreate, GroupOut
from sequrity.auth import get_db
from sequrity.rbac import admin_only


router = APIRouter()


@router.post("/create_group",
             response_model=APIResponse[GroupOut],
             dependencies=[Depends(admin_only)])
async def create_group_endpoint(group: GroupCreate,
                       db: Session = Depends(get_db)):
    created_group = create_group(group, db)
    return APIResponse(data=created_group)


@router.get("/groups",
            response_model=APIResponse[List[GroupOut]],
            dependencies=[Depends(admin_only)])
async def get_all_groups_endpoint(db: Session = Depends(get_db)):
    return APIResponse(data=get_all_groups(db))
