from flask import Blueprint, render_template, redirect, url_for, request
from forms.medical_scheme_form import MedicalSchemeForm
from db_query_service import insert_scheme
from db_query_service import read_schemes

medical_scheme_bp = Blueprint('medical_schemes', __name__)


@medical_scheme_bp.route('/load_scheme', methods=['GET', 'POST'])
def load_scheme():
    form = MedicalSchemeForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print('Form validated successfully!')
            try:
                new_scheme = insert_scheme(
                    scheme_name=form.scheme_name.data,
                    scheme_code=form.scheme_code.data,
                    scheme_administrator=form.scheme_administrator.data,
                    scheme_contact_number=form.scheme_contact_number.data,
                    scheme_email=form.scheme_email.data,
                    scheme_address=form.scheme_address.data,
                    scheme_premium=form.scheme_premium.data,
                    scheme_status=form.scheme_status.data,
                )
                print(f"Selected Scheme Status: {form.scheme_status.data}")
                if new_scheme:
                    print('Medical Scheme added successfully!')
                    return redirect(url_for('home.index'))
                else:
                    print('Failed to add Scheme.')
                    return render_template('medical_scheme_reg.html', form=form)
            except Exception as e:
                print(f'Failed to add Scheme: {e}')
        else:
            print('Form validation failed')
            print(f'Errors Occurred:{form.errors}')
            return render_template('medical_scheme_reg.html', form=form)

    return render_template('medical_scheme_reg.html', form=form)

