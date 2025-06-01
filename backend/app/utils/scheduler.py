from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.db_models.exam import Exam
from database.database import SessionLocal

def update_exam_statuses():
    db: Session = SessionLocal()
    now = datetime.utcnow() + timedelta(hours=3)

    # Обновляем экзамены, которые должны начаться
    db.query(Exam).filter(
        Exam.status == "not_started",
        Exam.start_time <= now,
        Exam.end_time > now
    ).update({Exam.status: "in_progress"}, synchronize_session=False)

    # Обновляем экзамены, которые должны завершиться
    db.query(Exam).filter(
        Exam.status.in_(["not_started", "in_progress"]),
        Exam.end_time <= now
    ).update({Exam.status: "finished"}, synchronize_session=False)

    db.commit()
    db.close()
