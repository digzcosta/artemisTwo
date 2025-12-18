from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from src.config import DATABASE_PATH

DATABASE_URL = f"sqlite:///{DATABASE_PATH}"


engine = create_engine(DATABASE_URL, echo=False)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)