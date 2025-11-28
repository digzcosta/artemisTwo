from dotenv import load_dotenv
import os

load_dotenv()

adzuna_app_id = os.getenv("ADZUNA_APP_ID")
adzuna_app_key = os.getenv("ADZUNA_APP_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
