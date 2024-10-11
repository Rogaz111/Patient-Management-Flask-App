from flask import Blueprint, render_template, redirect, url_for, request
from forms.appointment_form import BookAppointmentForm
from models.appointment_model import Appointment
from db_query_service import read_doctors
from db_query_service import read_patients
from db_query_service import read_schemes
from db_query_service import insert_appointment


appointments_bp = Blueprint('appointments', __name__)


@appointments_bp.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    form = BookAppointmentForm()

    patients = read_patients()
    doctors = read_doctors()
    schemes = read_schemes()

    form.patient_id.choices = [(p.id, p.name) for p in patients]
    form.doctor_id.choices = [(d.id, d.first_name) for d in doctors]
    form.medical_scheme_id.choices = [(s.id, s.scheme_name) for s in schemes]

    if request.method == 'POST':
        if form.validate_on_submit():
            print('Form validated successfully!')
            new_appointment = insert_appointment(
                patient_id=form.patient_id.data,
                doctor_id=form.doctor_id.data,
                medical_scheme_id=form.medical_scheme_id.data,
                has_medical_aid=True if form.has_medical_aid.data == 'yes' else False,
                appointment_date=form.appointment_date.data,
                appointment_time=form.appointment_time.data,
                appointment_reason=form.appointment_reason.data,
                appointment_status=form.appointment_status.data,
                appointment_notes=form.appointment_notes.data
            )

            if new_appointment:
                print('New Appointment added successfully!')
                return redirect(url_for('home.index'))
            else:
                print('Failed to add appointment.')
                return render_template('book_appointment.html', form=form)
        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            return render_template('book_appointment.html', form=form)

    return render_template('book_appointment.html',form=form)