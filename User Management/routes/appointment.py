from flask import Blueprint, render_template, redirect, url_for, request, jsonify
from db_query_service import (read_doctors, read_patients, read_schemes, insert_appointment, read_appointments,
                              update_appointment_query, insert_error_log)
from forms.appointment_form import BookAppointmentForm

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
                insert_error_log('Failed to add appointment.', 'appointment', True)
                return render_template('book_appointment.html', form=form)
        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            insert_error_log(form.errors, 'appointment', True)

            return render_template('book_appointment.html', form=form)

    return render_template('book_appointment.html', form=form)


@appointments_bp.route('/view_schedule', methods=['GET'])
def view_schedule():
    try:

        all_appointments = read_appointments()
        return render_template('view_appointments.html', all_appointments=all_appointments)

    except Exception as e:
        insert_error_log(e, 'appointment', True)


@appointments_bp.route('/update_appointments', methods=['POST'])
def update_appointment():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        appointment_id = data.get('appointment_id')
        field = data.get('field')
        new_value = data.get('new_value')
        print(f'field: {field} new_value: {new_value}')

        try:
            update_appointment_query(appointment_id, field, new_value)

            return jsonify({'status': 'success'})
        except Exception as e:
            insert_error_log(e, 'appointment', True)
            return jsonify({'status': 'error', 'message': str(e)})
