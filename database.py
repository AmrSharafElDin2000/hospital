import mysql.connector

class Database:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital_system"
        )
