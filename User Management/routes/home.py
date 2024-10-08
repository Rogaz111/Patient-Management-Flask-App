from flask import Blueprint, render_template
from db_query_service import read_patients
from db_query_service import read_patients_today

home_bp = Blueprint('home', __name__)

@home_bp.route('/',methods=['GET'])
@home_bp.route('/home',methods=['GET'])
def index():
    all_patients = read_patients()

    total_patients = len(all_patients)

    patients_created_today = len(read_patients_today())


    print(f'Total Patients: {len(all_patients)}')
    return render_template('index.html',
                           total_patients=total_patients,patients_created_today=patients_created_today
                           )