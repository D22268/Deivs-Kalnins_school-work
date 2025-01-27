import pymysql
import pytest
from App.database_setup import get_db_connection

def test_update_multiple_tables():
    """
    Test case to update multiple tables in a single transaction.
    """
    connection = get_db_connection()  
    cursor = connection.cursor()

    try:
        # Start a transaction
        connection.begin()

        #  Update renter's phone number
        cursor.execute("""
            UPDATE Renter 
            SET Phone_num = %s 
            WHERE Renter_id = %s
        """, (266606449, 1))  # Replace with test values

        #  Update tool rental price
        cursor.execute("""
            UPDATE Rent 
            SET Rent_cost = %s 
            WHERE Rent_id = %s
        """, (20, 1))  # Fixed column name

        # Update tool storage amount
        cursor.execute("""
            UPDATE Tool_storage 
            SET Amount_stored = Amount_stored - 1 
            WHERE Tool_id = %s
        """, (1,))  # Replace with test values

        # Commit transaction if all queries succeed
        connection.commit()

    except Exception as e:
        # Rollback if any error occurs
        connection.rollback()
        pytest.fail(f"Transaction failed: {e}")

    finally:
        # Cleanup
        cursor.close()
        connection.close()
