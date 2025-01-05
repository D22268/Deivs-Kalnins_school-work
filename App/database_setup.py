import pymysql
from app.logger import logger
from app.config import Config

def execute_sql_file(sql_file, connection):
    """Executes the SQL file to set up the database schema."""
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    with connection.cursor() as cursor:
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
    connection.commit()

def initialize_database():
    """Connects to the database and initializes the schema."""
    connection = pymysql.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        logger.info("Executing schema.sql to set up the database...")
        execute_sql_file("schema.sql", connection)
        logger.info("Database setup complete.")
    finally:
        connection.close()
