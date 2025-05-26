from sqlalchemy.orm import Session

from models.schemas.group import GroupCreate, GroupOut
from utils.exceptions import GroupAlreadyExistsException
from models.db_models.group import Group


def create_group(group_data: GroupCreate,
                db: Session):
    existing_group = db.query(Group).filter(Group.name == group_data.name).first()

    if existing_group is not None:
        raise GroupAlreadyExistsException

    new_group = Group(
        name=group_data.name
    )

    db.add(new_group)
    db.commit()
    db.refresh(new_group)

    return GroupOut.model_validate(new_group)

def get_all_groups(db: Session):
    groups = db.query(Group).all()

    return list(GroupOut.model_validate(group) for group in groups)
