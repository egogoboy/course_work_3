from sqlalchemy.orm import Session

from models.schemas.subject import SubjectCreate, SubjectOut
from utils.exceptions.subject import SubjectAlreadyExistsException, SubjectNotFoundException
from models.db_models.subject import Subject


class crudSubject:
    @staticmethod
    async def create_subject(subject_data: SubjectCreate,
                    db: Session):
        existing_subject = db.query(Subject).filter(Subject.name == subject_data.name).first()

        if existing_subject is not None:
            raise SubjectAlreadyExistsException

        new_subject = Subject(
            name=subject_data.name
        )

        db.add(new_subject)
        db.commit()
        db.refresh(new_subject)

        return SubjectOut.model_validate(new_subject)


    @staticmethod
    async def get_all_subjects(db: Session):
        subjects = db.query(Subject).all()

        return list(SubjectOut.model_validate(subject) for subject in subjects)


    @staticmethod
    async def get_current_subject(id: int,
                                 db: Session):
        subject = db.query(Subject).filter(Subject.id == id).first()

        if subject is None:
            raise SubjectNotFoundException

        return subject


    @staticmethod
    async def update_subject(id: int,
                   new_subject_data: SubjectCreate,
                   db: Session):
        current_subject = db.query(Subject).filter(Subject.id == id).first()

        if not current_subject:
            raise SubjectNotFoundException

        for field, value in new_subject_data.model_dump(exclude_unset=True).items():
            setattr(current_subject, field, value)

        db.commit()
        db.refresh(current_subject)

        return SubjectOut.model_validate(current_subject)


    @staticmethod
    async def delete_subject(subject_id: int,
                          db: Session):
        subject = db.query(Subject).filter(Subject.id == subject_id).first()
        if not subject:
            raise SubjectNotFoundException 
        db.delete(subject)
        db.commit()
        return SubjectOut.model_validate(subject)
