from database import Base, engine
import models

def init_db():
    Base.metadata.create_all(bind=engine)
