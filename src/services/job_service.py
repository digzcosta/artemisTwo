# Functions for saving vacancies after cleaning and displaying saved vacancies in the database.
# Columns displayed will be limited due to the scope of the prototype.

from tabulate import tabulate
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


def show_jobs():
    session = SessionLocal()
    try:
        results = (
            session.query(
                Job.title,
                Job.company,
                Job.location
            )
            .all()
        )

        if not results:
            print("Nenhum job encontrado.")
            return

        headers = ["Title", "Company", "Location"]

        print(tabulate(results, headers=headers, tablefmt="grid"))

    finally:
        session.close()