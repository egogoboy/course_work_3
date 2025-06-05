from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.group import create_group, get_all_groups, delete_group, update_group, get_current_group
from models.schemas.group import GroupCreate
from database.database import get_db
from security.rbac import admin_only, admin_and_teacher


router = APIRouter()


@router.post("/create", 
             dependencies=[Depends(admin_only)])
async def create_group_endpoint(group: GroupCreate,
                       db: Session = Depends(get_db)):
    return await create_group(group, db)


@router.delete("/{group_id}", 
               dependencies=[Depends(admin_only)])
async def delete_group_endpoint(group_id: int,
                       db: Session = Depends(get_db)):
    return await delete_group(group_id, db)


@router.get("/", 
            dependencies=[Depends(admin_and_teacher)])
async def get_all_groups_endpoint(db: Session = Depends(get_db)):
    return await get_all_groups(db)


@router.get("/{group_id}", 
            dependencies=[Depends(admin_and_teacher)])
async def get_current_groups_endpoint(group_id: int,
                                      db: Session = Depends(get_db)):
    return await get_current_group(group_id, db)

@router.put("/{group_id}",
            dependencies=[Depends(admin_only)])
async def edit_group_endpoint(group_id: int,
                              new_data: GroupCreate,
                              db: Session = Depends(get_db)):
    return await update_group(group_id, new_data, db)
