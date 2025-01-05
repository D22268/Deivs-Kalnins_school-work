import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    DATABASE_HOST = os.getenv("DB_HOST", "localhost")
    DATABASE_USER = os.getenv("DB_USER", "DeivsK")
    DATABASE_PASSWORD = os.getenv("DB_PASSWORD", "password")
    DATABASE_NAME = os.getenv("DB_NAME", "Rental")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
