from flask_wtf import FlaskForm
from wtforms import RadioField, SelectField, TextAreaField, DateField, TimeField
from wtforms.validators import InputRequired, DataRequired,Optional


class BookAppointmentForm(FlaskForm):
    patient_id = SelectField('Patient', choices=[], coerce=int, validators=[DataRequired()])
    doctor_id = SelectField('Doctor', choices=[], coerce=int, validators=[DataRequired()])
    has_medical_aid = RadioField('Does the Patient have Medical Aid ?', choices=[('yes', 'Yes'), ('no', 'No')],
                                 validators=[InputRequired()])
    medical_scheme_id = SelectField('Medical Scheme', choices=[], coerce=int, validators=[DataRequired()])
    appointment_date = DateField('Appointment Date', validators=[InputRequired()])
    appointment_time = TimeField('Appointment Time', validators=[InputRequired()])
    appointment_reason = TextAreaField('Appointment Reason', validators=[InputRequired()])
    appointment_status = SelectField('Appointment Status',choices=[('scheduled', 'Scheduled'), ('cancelled', 'Cancelled'),
                                                                   ('pending', 'Pending')])
    appointment_notes = TextAreaField('Appointment Notes', validators=[Optional()])