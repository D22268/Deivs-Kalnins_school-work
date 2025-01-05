import pymysql
import pytest
from app.database_setup import execute_sql_file
from app.config import Config

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
    execute_sql_file("schema.sql", connection)
    yield connection
    connection.close()

def test_add_renter(connection):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO Renter (Name, Surname, Personal_id_num, Phone_num) VALUES (%s, %s, %s, %s)", 
                       ("Test", "User", "ID456", 9876543210))
        cursor.execute("SELECT * FROM Renter WHERE Personal_id_num = %s", ("ID456",))
        renter = cursor.fetchone()
    assert renter["Name"] == "Test"
