# This module is responsible for initializing the database schema.
from src.database.connection import Base, engine

def init_db():
    Base.metadata.create_all(engine)
