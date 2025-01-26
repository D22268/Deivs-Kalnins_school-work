import pytest
import pymysql
from App.config import Config
from App.database_setup import execute_sql_file

@pytest.fixture(scope="module")
def connection():
    connection = pymysql.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        db=Config.DATABASE_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    # Initialize the database schema before tests
    execute_sql_file("schema.sql", connection)
    yield connection  # This is returned to the test functions
    connection.close()  # Teardown after all tests in the module are complete
