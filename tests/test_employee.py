import unittest
from models.employee import Employee
from database import Database

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Runs before each test: Deletes test data to prevent duplicates."""
        conn = Database.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM employees WHERE email = %s", ("john@example.com",))
        conn.commit()
        cursor.close()
        conn.close()

    def test_add_employee(self):
        """Test adding an employee."""
        result = Employee.add_employee("John Doe", "john@example.com", 5000)
        self.assertEqual(result, "Employee added successfully.")

if __name__ == "__main__":
    unittest.main()
