import mysql.connector
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "1234"),
    "database": os.getenv("DB_NAME", "hospital_system"),
}

TABLES = {
    "employees": """
        CREATE TABLE IF NOT EXISTS employees (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            salary DECIMAL(10,2) NOT NULL
        );
    """,
    "patients": """
        CREATE TABLE IF NOT EXISTS patients (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            phone_number VARCHAR(20) NOT NULL,
            disease TEXT NOT NULL
        );
    """
}

def initialize_database():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Ensure the database exists
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_CONFIG['database']}")
    cursor.execute(f"USE {DB_CONFIG['database']}")

    # Create necessary tables
    for table, query in TABLES.items():
        print(f"Creating/updating table: {table}")
        cursor.execute(query)

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
