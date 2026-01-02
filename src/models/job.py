# Creation of the table model to store in the database, based on the API's receiving parameters.

from src.database.connection import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class Job(Base):
    __tablename__ = "adzuna_jobs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    external_id = Column(String, nullable=False, unique=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    salary = Column(Float)
    created_at = Column(DateTime)
    url = Column(String, unique=True, nullable=False)


