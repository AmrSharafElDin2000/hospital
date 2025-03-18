import mysql.connector
from database import Database

class Patient:
    @staticmethod
    def add_patient(name, age, phone_number, disease):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO patients (name, age, phone_number, disease) VALUES (%s, %s, %s, %s)", 
                           (name, age, phone_number, disease))
            conn.commit()
            return "Patient added successfully."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_patient(patient_id):
        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
            result = cursor.fetchone()
            if result:
                return result
            return "Patient not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_patient(patient_id, name=None, age=None, phone_number=None, disease=None):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            updates = []
            values = []

            if name:
                updates.append("name = %s")
                values.append(name)
            if age:
                updates.append("age = %s")
                values.append(age)
            if phone_number:
                updates.append("phone_number = %s")
                values.append(phone_number)
            if disease:
                updates.append("disease = %s")
                values.append(disease)

            if not updates:
                return "No updates provided."

            values.append(patient_id)
            query = f"UPDATE patients SET {', '.join(updates)} WHERE patient_id = %s"
            cursor.execute(query, values)
            conn.commit()

            if cursor.rowcount > 0:
                return "Patient updated successfully."
            return "Patient not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()
