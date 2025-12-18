from sqlalchemy.exc import IntegrityError
from src.database.connection import SessionLocal
from src.models.job import Job

def save_job(cleaned_data: dict) -> bool:
    
    session = SessionLocal()
    try:
        job = Job(**cleaned_data)
        session.add(job)
        session.commit()
        return True
    except IntegrityError:
        session.rollback()
        return False
    finally:
        session.close()