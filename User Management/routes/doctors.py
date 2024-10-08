from flask import Blueprint, render_template, redirect, url_for, request
from forms.doctors_form import DoctorRegistrationForm

doctors_bp = Blueprint('doctors', __name__)


@doctors_bp.route('/register_doctor', methods=['GET', 'POST'])
def register_doctors():
    form = DoctorRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Form validated successfully!')
            return redirect(url_for('home.index'))
        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            return render_template('doctor_registration.html', form=form)

    return render_template('doctor_registration.html', form=form)
