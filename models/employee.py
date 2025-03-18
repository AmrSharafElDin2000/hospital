import mysql.connector

class Employee:
    @staticmethod
    def connect():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="hospital_system"
        )

    @staticmethod
    def add_employee(name, email, salary):
        conn = Employee.connect()
        cursor = conn.cursor()
        query = "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, salary))
        conn.commit()
        conn.close()
        return "Employee added successfully."

    @staticmethod
    def get_employee(emp_id):
        """Retrieve an employee's details by employee_id."""
        conn = Employee.connect()
        cursor = conn.cursor(dictionary=True)  # Returns a dictionary instead of a tuple
        query = "SELECT * FROM employees WHERE employee_id = %s"
        
        try:
            cursor.execute(query, (emp_id,))
            employee = cursor.fetchone()
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            employee = None
        finally:
            conn.close()

        if employee:
            return employee
        else:
            print("Employee not found.")
            return None
