import pymysql
from App.logger import logger
from App.config import Config

def add_renter(connection, name, surname, personal_id, phone):
    with connection.cursor() as cursor:
        sql = "INSERT INTO Renter (Name, Surname, Personal_id_num, Phone_num) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, surname, personal_id, phone))
    connection.commit()
    logger.info(f"Added renter: {name} {surname}")

if __name__ == "__main__":
    connection = pymysql.connect(
        host=Config.DATABASE_HOST,
        user=Config.DATABASE_USER,
        password=Config.DATABASE_PASSWORD,
        db=Config.DATABASE_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        logger.info("Adding sample data...")
        add_renter(connection, "David", "Johnson", "ID123", 1234567890)
    finally:
        connection.close()
