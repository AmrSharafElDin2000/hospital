import mysql.connector
from database import Database

class DataEntry:
    @staticmethod
    def add_data_entry(employee_id, shift):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO data_entries (employee_id, shift) VALUES (%s, %s)", (employee_id, shift))
            conn.commit()
            return "Data entry added successfully."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_data_entry(employee_id):
        conn = Database.get_connection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM data_entries WHERE employee_id = %s", (employee_id,))
            result = cursor.fetchone()
            if result:
                return result
            return "Data entry not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def update_data_entry(employee_id, new_shift):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("UPDATE data_entries SET shift = %s WHERE employee_id = %s", (new_shift, employee_id))
            conn.commit()
            if cursor.rowcount > 0:
                return "Data entry updated successfully."
            return "Data entry not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def delete_data_entry(employee_id):
        conn = Database.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM data_entries WHERE employee_id = %s", (employee_id,))
            conn.commit()
            if cursor.rowcount > 0:
                return "Data entry deleted successfully."
            return "Data entry not found."
        except mysql.connector.Error as err:
            return f"Error: {err}"
        finally:
            cursor.close()
            conn.close()
