from flask import Blueprint, render_template, redirect, url_for, request
from forms.patient_form import MedicalPatientForm
from db_query_service import insert_patient
from db_query_service import read_patients

patients_bp = Blueprint('patients', __name__)


@patients_bp.route('/register', methods=['GET', 'POST'])
def register_patient():
    form = MedicalPatientForm()
    if request.method == 'POST':
        # Validate the form when the request is POST and form is submitted
        if form.validate_on_submit():
            print('Form validated successfully!')
            # You can process the form data here
            new_patient = insert_patient(
                name=form.name.data,
                date_of_birth=form.date_of_birth.data,
                gender=form.gender.data,
                contact_number=form.contact_number.data,
                email=form.email.data,
                address=form.address.data,
                medical_history=form.medical_history.data,
                emergency_contact_name=form.emergency_contact_name.data,
                emergency_contact_number=form.emergency_contact_number.data,
                blood_group=form.blood_group.data,
                photo=form.photo.data if form.photo.data else None
            )
            if new_patient:
                print('Patient added successfully!')
                # Redirect to another route after successful registration (e.g., home page)
                return redirect(url_for('home.index'))
            else:
                print('Failed to add patient.')
                return render_template('patient_registration.html', form=form)

        else:
            print('Form validation failed')
            print(f'Errors Occured:{form.errors}')
            return render_template('patient_registration.html', form=form)
    else:
        # If the request is GET or form validation failed, render the form template again
        return render_template('patient_registration.html', form=form)


@patients_bp.route('/view_patients', methods=['GET'])
def patient_view():
    all_patients = read_patients()
    return render_template('patient_view.html', patients=all_patients)
