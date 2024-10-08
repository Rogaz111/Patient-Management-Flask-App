from datetime import date
from database_service import session
from models.patient_model import Patient


# Insert a new patient into the database
def insert_patient(name, date_of_birth, gender, contact_number, email, address, medical_history,
                   emergency_contact_name, emergency_contact_number, blood_group, photo=None):
    try:
        new_patient = Patient(
            name=name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number,
            email=email,
            address=address,
            medical_history=medical_history,
            emergency_contact_name=emergency_contact_name,
            emergency_contact_number=emergency_contact_number,
            blood_group=blood_group,
            photo=photo
        )
        session.add(new_patient)  # Add to session
        session.commit()  # Commit the transaction
        print("Patient successfully added.")
        return True
    except Exception as e:
        session.rollback()  # Rollback the session if there’s an error
        print(f"Error inserting patient: {e}")
        return False


# Read all patients from the database
def read_patients():
    try:
        patients = session.query(Patient).all()  # Query all patients
        return patients
    except Exception as e:
        print(f"Error reading patients: {e}")
        return []


# Read all patients from the database created today
def read_patients_today():
    try:
        # Query for patients created today
        new_patients_today = session.query(Patient).filter(Patient.create_date == date.today()).all()
        return new_patients_today
    except Exception as e:
        print(f"Error reading patients: {e}")
        return []
