import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Relentlesspursuit'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database without SELECT or SHOW
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")

    finally:
        # Close cursor and connection safely
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
