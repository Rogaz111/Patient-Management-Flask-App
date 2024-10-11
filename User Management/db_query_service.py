from datetime import date
from database_service import session
from models.patient_model import Patient
from models.doctors_model import Doctor
from models.medical_scheme_model import MedicalScheme
from models.appointment_model import Appointment


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


def insert_doctor(first_name, last_name, date_of_birth, gender, email, contact_number, department, address,
                  profile_photo=None):
    try:
        new_doctor = Doctor(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            gender=gender,
            contact_number=contact_number,
            department=department,
            email=email,
            address=address,
            profile_photo=profile_photo
        )
        session.add(new_doctor)  # Add to session
        session.commit()  # Commit the transaction
        print("Doctor successfully added.")
        return True
    except Exception as e:
        session.rollback()  # Rollback the session if there’s an error
        print(f"Error inserting doctor: {e}")
        return False


# Read all doctors from the database
def read_doctors():
    try:
        doctors = session.query(Doctor).all()  # Query all patients
        return doctors
    except Exception as e:
        print(f"Error reading doctors: {e}")
        return []


# Insert new Medical Scheme
def insert_scheme(scheme_name, scheme_code, scheme_administrator, scheme_contact_number, scheme_email,
                  scheme_address, scheme_premium, scheme_status):
    try:
        new_scheme = MedicalScheme(
            scheme_name=scheme_name,
            scheme_code=scheme_code,
            scheme_administrator=scheme_administrator,
            scheme_contact_number=scheme_contact_number,
            scheme_email=scheme_email,
            scheme_address=scheme_address,
            scheme_premium=scheme_premium,
            scheme_status=scheme_status,
        )
        session.add(new_scheme)  # Add to session
        session.commit()  # Commit the transaction
        return True
    except Exception as e:
        print(f"Error inserting scheme: {e}")
        return False


# Read all Medical Schemes from the database
def read_schemes():
    try:
        schemes = session.query(MedicalScheme).all()  # Query all patients
        return schemes
    except Exception as e:
        print(f"Error reading schemes: {e}")
        return []


def insert_appointment(patient_id, doctor_id, has_medical_aid, medical_scheme_id, appointment_date, appointment_time,
                       appointment_reason,
                       appointment_status, appointment_notes):
    try:
        new_appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_id,
            medical_scheme_id=medical_scheme_id,
            has_medical_scheme=has_medical_aid,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            reason=appointment_reason,
            status=appointment_status,
            notes=appointment_notes
        )
        session.add(new_appointment)  # Add to session
        session.commit()  # Commit the transaction
        return True

    except Exception as e:
        print(f"Error inserting appointment: {e}")
        return False


def read_appointments():
    try:
        appointments = session.query(Appointment).all()  # Query all patients
        return appointments
    except Exception as e:
        print(f"Error reading schemes: {e}")
        return []
