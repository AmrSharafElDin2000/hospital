import mysql.connector
from models.employee import Employee
from models.doctor import Doctor
from models.manager import Manager
from models.patient import Patient
from models.data_entry import DataEntry
from models.prescription import Prescription

def main():
    while True:
        print("\nHospital System Menu:")
        print("1. Add Employee")
        print("2. Get Employee Details")
        print("3. Add Doctor")
        print("4. Get Doctor Details")
        print("5. Update Doctor")
        print("6. Delete Doctor")
        print("7. Add Manager")
        print("8. Get Manager Details")
        print("9. Add Patient")
        print("10. Get Patient Details")
        print("11. Add Data Entry")
        print("12. Get Data Entry Details")
        print("13. Create Prescription")
        print("14. Get Prescription Details")
        print("15. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            salary = input("Enter Salary: ")
            print(Employee.add_employee(name, email, salary))

        elif choice == "2":
            employee_id = input("Enter Employee ID: ")
            print(Employee.get_employee(employee_id))

        elif choice == "3":
            employee_id = input("Enter Doctor Employee ID: ")
            name = input("Enter Name: ")
            specialization = input("Enter Specialization: ")
            print(Doctor.add_doctor(employee_id, name, specialization))

        elif choice == "4":
            employee_id = input("Enter Doctor Employee ID: ")
            print(Doctor.get_doctor(employee_id))

        elif choice == "5":
            employee_id = input("Enter Doctor Employee ID: ")
            new_specialization = input("Enter New Specialization: ")
            print(Doctor.update_doctor(employee_id, new_specialization))

        elif choice == "6":
            employee_id = input("Enter Doctor Employee ID: ")
            print(Doctor.delete_doctor(employee_id))

        elif choice == "7":
            employee_id = input("Enter Manager Employee ID: ")
            department = input("Enter Department: ")
            print(Manager.add_manager(employee_id, department))

        elif choice == "8":
            employee_id = input("Enter Manager Employee ID: ")
            print(Manager.get_manager(employee_id))

        elif choice == "9":
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            phone_number = input("Enter Patient Phone: ")
            disease = input("Enter Disease: ")
            print(Patient.add_patient(name, age, phone_number, disease))

        elif choice == "10":
            patient_id = input("Enter Patient ID: ")
            print(Patient.get_patient(patient_id))

        elif choice == "11":
            employee_id = input("Enter Data Entry Employee ID: ")
            shift = input("Enter Shift: ")
            print(DataEntry.add_data_entry(employee_id, shift))

        elif choice == "12":
            employee_id = input("Enter Data Entry Employee ID: ")
            print(DataEntry.get_data_entry(employee_id))

        elif choice == "13":
            patient_id = input("Enter Patient ID: ")
            doctor_id = input("Enter Doctor ID: ")
            medicine = input("Enter Medication: ")
            dosage = input("Enter Dosage: ")
            print(Prescription.create_prescription(patient_id, doctor_id, medicine, dosage))

        elif choice == "14":
            patient_id = input("Enter Patient ID: ")
            print(Prescription.get_prescription(patient_id))

        elif choice == "15":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
