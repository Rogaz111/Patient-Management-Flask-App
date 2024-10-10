from flask import Blueprint, render_template
from db_query_service import read_patients
from db_query_service import read_patients_today
from db_query_service import read_doctors
from db_query_service import read_schemes

home_bp = Blueprint('home', __name__)


@home_bp.route('/', methods=['GET'])
@home_bp.route('/home', methods=['GET'])
def index():
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

    print(f'Total Patients: {len(all_patients)}')
    print(f'Total Doctors: {len(all_doctors)}')
    print(f'Total Medical Schemes: {total_medical_schemes}')
    return render_template('index.html',
                           total_patients=total_patients, patients_created_today=patients_created_today,
                           total_doctors=total_doctors, total_medical_schemes=total_medical_schemes
                           )
