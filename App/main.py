import pymysql
from App.logger import logger
from App.config import Config

def add_renter(connection, name, surname, personal_id_num, phone_num):
    """Adds a renter to the Renter table."""
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO Renter (Name, Surname, Personal_id_num, Phone_num)
                VALUES (%s, %s, %s, %s)
            """, (name, surname, personal_id_num, phone_num))
            connection.commit()
            logger.info(f"Renter {name} {surname} added successfully.")
        except pymysql.MySQLError as e:
            connection.rollback()
            logger.error(f"Error adding renter: {e}")
            raise

def add_category(connection, category):
    """Adds a category to the Categories table."""
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO Categories (Category)
                VALUES (%s)
            """, (category,))
            connection.commit()
            logger.info(f"Category {category} added successfully.")
        except pymysql.MySQLError as e:
            connection.rollback()
            logger.error(f"Error adding category: {e}")
            raise

def add_rent(connection, renter_id, rent_cost):
    """Adds a rent record to the Rent table."""
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO Rent (Renter_id, Rent_cost)
                VALUES (%s, %s)
            """, (renter_id, rent_cost))
            connection.commit()
            logger.info(f"Rent record for Renter ID {renter_id} added successfully.")
        except pymysql.MySQLError as e:
            connection.rollback()
            logger.error(f"Error adding rent record: {e}")
            raise

def add_tool_storage(connection, amount_stored):
    """Adds a tool storage record to the Tool_storage table."""
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO Tool_storage (Amount_stored)
                VALUES (%s)
            """, (amount_stored,))
            connection.commit()
            logger.info(f"Tool storage with {amount_stored} units added successfully.")
        except pymysql.MySQLError as e:
            connection.rollback()
            logger.error(f"Error adding tool storage: {e}")
            raise


def add_rented_tool(connection, tool_id, tool_name, rent_id, category_id, instrument_loss_cost):
    """Adds a rented tool record to the Rented_tool table."""
    with connection.cursor() as cursor:
        try:
            cursor.execute("""
                INSERT INTO Rented_tool (Tool_id, Tool_name, Rent_id, Category_id, Instrument_loss_cost)
                VALUES (%s, %s, %s, %s, %s)
            """, (tool_id, tool_name, rent_id, category_id, instrument_loss_cost))
            connection.commit()
            logger.info(f"Rented tool {tool_name} added successfully.")
        except pymysql.MySQLError as e:
            connection.rollback()
            logger.error(f"Error adding rented tool: {e}")
            raise

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
        # Insert data into the Categories table
        add_category(connection, 'Hand Held') 

        # Insert data into the Renter table
        add_renter(connection, 'John', 'Holland', '123456789', '555-1234')

        # Insert data into the Tool_storage table
        add_tool_storage(connection, 50)
        
        # Insert data into the Rent table
        add_rent(connection, 1, 100)  

        # Insert data into the Rented_tool table
        add_rented_tool(connection, 1, 'Hammer', 1, 1, 10)  

        logger.info("Data inserted into all tables successfully.")
    except Exception as e:
        logger.error(f"Error inserting data into all tables: {e}")
    finally:
        connection.close()
