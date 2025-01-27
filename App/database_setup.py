import pymysql
from App.logger import logger
from App.config import Config

def execute_sql_file(sql_file, connection):
    """Executes the SQL file to set up the database schema."""
    with open(sql_file, 'r') as file:
        sql_script = file.read()
    
    with connection.cursor() as cursor:
        for statement in sql_script.split(';'):
            if statement.strip():
                try:
                    cursor.execute(statement)
                except pymysql.MySQLError as e:
                    logger.error(f"SQL Execution Error: {e}")
                    raise  # Stop execution if an error occurs
    connection.commit()

def initialize_database():
    """Connects to MySQL, creates the database if it doesn't exist, and initializes the schema."""
    connection = pymysql.connect(
    host=Config.DATABASE_HOST,
    user=Config.DATABASE_USER,
    password=Config.DATABASE_PASSWORD,
    db='rental',  # Ensure you're connecting to the 'Rental' database
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with connection.cursor() as cursor:
            # Ensure the database exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS rental;")
            cursor.execute("USE rental;")  # Explicitly select the database

        logger.info("Executing schema.sql to set up the database...")
        execute_sql_file("schema.sql", connection)
        logger.info("Database setup complete.")

    except pymysql.MySQLError as e:
        logger.error(f"Database initialization failed: {e}")
    
    finally:
        connection.close()
        
    def get_db_connection():
        """Establishes and returns a connection to the MySQL database."""
    connection = pymysql.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        db=Config.DATABASE_NAME,  # Replace with the actual database name if needed
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
        
    if __name__ == "__main__":
        initialize_database()