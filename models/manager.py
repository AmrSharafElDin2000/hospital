import mysql.connector
from models.employee import Employee

class Manager(Employee):
    def __init__(self, employee_id, name, email, salary, department):
        super().__init__(employee_id, name, email, salary)
        self.department = department

    @staticmethod
    def create_table():
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS managers (
                id INT PRIMARY KEY AUTO_INCREMENT,
                employee_id INT UNIQUE NOT NULL,
                department VARCHAR(255) NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE
            )
        """)
        connection.commit()
        connection.close()

    @staticmethod
    def add_manager(employee_id, department):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "INSERT INTO managers (employee_id, department) VALUES (%s, %s)"
        cursor.execute(query, (employee_id, department))
        connection.commit()
        connection.close()
        return "Manager added successfully."

    @staticmethod
    def get_manager(employee_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM managers WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        manager = cursor.fetchone()
        connection.close()
        return manager if manager else "Manager not found."

    @staticmethod
    def update_manager(employee_id, new_department):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "UPDATE managers SET department = %s WHERE employee_id = %s"
        cursor.execute(query, (new_department, employee_id))
        connection.commit()
        connection.close()
        return "Manager updated successfully."

    @staticmethod
    def delete_manager(employee_id):
        connection = mysql.connector.connect(host="localhost", user="root", password="1234", database="hospital_system")
        cursor = connection.cursor()
        query = "DELETE FROM managers WHERE employee_id = %s"
        cursor.execute(query, (employee_id,))
        connection.commit()
        connection.close()
        return "Manager deleted successfully."
