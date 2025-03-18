import mysql.connector
from database import Database

class Prescription:
    @staticmethod
    def create_prescription(patient_id, doctor_id, medicine, dosage):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO prescriptions (patient_id, doctor_id, medicine, dosage) VALUES (%s, %s, %s, %s)", 
                           (patient_id, doctor_id, medicine, dosage))
            conn.commit()
            return "Prescription added successfully."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_prescription(patient_id):
        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM prescriptions WHERE patient_id = %s", (patient_id,))
            result = cursor.fetchall()
            if result:
                return result
            return "No prescriptions found for this patient."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_prescription(prescription_id, medicine=None, dosage=None):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            updates = []
            values = []

            if medicine:
                updates.append("medicine = %s")
                values.append(medicine)
            if dosage:
                updates.append("dosage = %s")
                values.append(dosage)

            if not updates:
                return "No updates provided."

            values.append(prescription_id)
            query = f"UPDATE prescriptions SET {', '.join(updates)} WHERE id = %s"
            cursor.execute(query, values)
            conn.commit()

            if cursor.rowcount > 0:
                return "Prescription updated successfully."
            return "Prescription not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_prescription(prescription_id):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM prescriptions WHERE id = %s", (prescription_id,))
            conn.commit()
            if cursor.rowcount > 0:
                return "Prescription deleted successfully."
            return "Prescription not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()
