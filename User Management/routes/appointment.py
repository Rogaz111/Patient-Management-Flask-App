from flask import Blueprint, render_template, redirect, url_for, request
from forms.appointment_form import BookAppointmentForm

appointments_bp = Blueprint('appointments', __name__)


@appointments_bp.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    form = BookAppointmentForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Form validated successfully!')

            return redirect(url_for('home.index'))
        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            return render_template('book_appointment.html', form=form)

    return render_template('book_appointment.html',form=form)