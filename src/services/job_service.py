# Functions for saving vacancies after cleaning and displaying saved vacancies in the database.
# Columns displayed will be limited due to the scope of the prototype.

from tabulate import tabulate
from sqlalchemy.exc import IntegrityError
from src.database.connection import SessionLocal
from src.models.job import Job

import pandas as pd
import os 
from datetime import datetime



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



def get_jobs_dataframe():
    session = SessionLocal()
    try:
        results = (
            session.query(
                Job.id,
                Job.external_id,
                Job.title,
                Job.company,
                Job.location,
                Job.salary,
                Job.created_at,
                Job.url
            )
            .all()
        ) 
        # Ajustar isso para retornar no CLI as mensagens
        if not results:
            return None

        df = pd.DataFrame(
            data=results,
            columns=[
                "id",
                "external_id",
                "title",
                "company",
                "location",
                "salary",
                "created_at",
                "url"
            ]
        )

        folder_path = os.path.join(os.getcwd(), 'exports/powerbi')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        
        date_suffix = datetime.now().strftime("_%d%m%Y_%H%M")
        original_filename = "jobs.csv"
        new_filename = original_filename.replace('.csv', f"{date_suffix}.csv")

        destination_path = os.path.join(folder_path, new_filename)
        df.to_csv(destination_path, index=False)

    finally:
        session.close()
        
    return destination_path