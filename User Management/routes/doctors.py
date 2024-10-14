from flask import Blueprint, render_template, redirect, url_for, request
from forms.doctors_form import DoctorRegistrationForm
from db_query_service import insert_doctor
from db_query_service import read_doctors, insert_error_log

doctors_bp = Blueprint('doctors', __name__)


@doctors_bp.route('/register_doctor', methods=['GET', 'POST'])
def register_doctors():
    form = DoctorRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Form validated successfully!')

            new_doctor = insert_doctor(
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                date_of_birth=form.date_of_birth.data,
                gender=form.gender.data,
                contact_number=form.contact_number.data,
                email=form.email.data,
                department=form.department.data,
                address=form.address.data,
                profile_photo=form.profile_photo.data if form.profile_photo.data else None
            )
            if new_doctor:
                print('Doctor added successfully!')
                return redirect(url_for('home.index'))
            else:
                print('Failed to add doctor.')
                insert_error_log('Failed to add doctor.', 'doctor', True)
                return render_template('doctor_registration.html', form=form)

        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            insert_error_log(form.errors, 'doctor', True)
            return render_template('doctor_registration.html', form=form)

    return render_template('doctor_registration.html', form=form)


@doctors_bp.route('/view_doctors', methods=['GET', 'POST'])
def doctors_view():
    try:
        all_doctors = read_doctors()
        return render_template('doctors_view.html', doctors=all_doctors)
    except Exception as e:
        insert_error_log(e, 'doctor', True)

