import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    DATABASE_HOST = os.getenv("DB_HOST", "localhost")
    DATABASE_USER = os.getenv("DB_USER", "root")
    DATABASE_PASSWORD = os.getenv("DB_PASSWORD", "S@03r0o/_k")
    DATABASE_NAME = os.getenv("DB_NAME", "rental")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
