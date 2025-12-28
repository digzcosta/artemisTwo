# Definition of environment variables

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

adzuna_app_id = os.getenv("ADZUNA_APP_ID")
adzuna_app_key = os.getenv("ADZUNA_APP_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "data" / "artemis.db"