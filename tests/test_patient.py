import unittest
from models.patient import Patient
from database import Database

class TestPatient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.conn = Database.get_connection()
        cls.cursor = cls.conn.cursor()

    def test_add_patient(self):
        result = Patient.add_patient("Alice", 30, "1234567890", "Flu")
        self.assertEqual(result, "Patient added successfully.")

    def test_get_patient(self):
        patient_id = 1
        patient = Patient.get_patient(patient_id)
        self.assertIsNotNone(patient)

    @classmethod
    def tearDownClass(cls):
        cls.cursor.close()
        cls.conn.close()

if __name__ == '__main__':
    unittest.main()
