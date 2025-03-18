import mysql.connector
from models.employee import Employee

class Doctor(Employee):
    def __init__(self, employee_id, name, email, salary, specialization):
        super().__init__(employee_id, name, email, salary)
        self.specialization = specialization

    @staticmethod
    def create_table():
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                id INT PRIMARY KEY AUTO_INCREMENT,
                employee_id INT UNIQUE NOT NULL,
                name VARCHAR(255) NOT NULL,
                specialization VARCHAR(255) NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
            )
        """)
        connection.commit()
        connection.close()

    @staticmethod
    def add_doctor(employee_id, name, specialization):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "INSERT INTO doctors (employee_id, name, specialization) VALUES (%s, %s, %s)"
        cursor.execute(query, (employee_id, name, specialization))
        connection.commit()
        connection.close()
        return "Doctor added successfully."

    @staticmethod
    def get_doctor(employee_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM doctors WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        doctor = cursor.fetchone()
        connection.close()
        return doctor if doctor else "Doctor not found."

    @staticmethod
    def update_doctor(employee_id, new_specialization):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "UPDATE doctors SET specialization = %s WHERE employee_id = %s"
        cursor.execute(query, (new_specialization, employee_id))
        connection.commit()
        connection.close()
        return "Doctor updated successfully."

    @staticmethod
    def delete_doctor(employee_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "DELETE FROM doctors WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        connection.commit()
        connection.close()
        return "Doctor deleted successfully."
