from database.database import Base, engine
from models.db_models import user, group, subject, exam, task, result, group_subject, task

def init_db():
    print("Creating database...")
    Base.metadata.create_all(bind=engine)
    print("Done.")
