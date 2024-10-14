from flask import Blueprint, render_template
from db_query_service import read_patients, read_patients_today, read_doctors, read_schemes, read_appointments, \
    insert_error_log

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
@home_bp.route('/home', methods=['GET'])
def index():
    try:

        #Query patients
        all_patients = read_patients()
        total_patients = len(all_patients)
        patients_created_today = len(read_patients_today())

        #Query Doctors
        all_doctors = read_doctors()
        total_doctors = len(all_doctors)

        #Query Medical Schemes
        all_schemes = read_schemes()
        total_medical_schemes = len(all_schemes)

        #Query Appointments
        all_appointments = read_appointments()
        total_appointments = len(all_appointments)

        print(f'Total Patients: {len(all_patients)}')
        print(f'Total Doctors: {len(all_doctors)}')
        print(f'Total Medical Schemes: {total_medical_schemes}')
        print(f'Total Appointments: {total_appointments}')

        return render_template('index.html',
                               total_patients=total_patients, patients_created_today=patients_created_today,
                               total_doctors=total_doctors, total_medical_schemes=total_medical_schemes,
                               total_appointments=total_appointments
                               )
    except Exception as e:
        insert_error_log(e, 'home', True)
