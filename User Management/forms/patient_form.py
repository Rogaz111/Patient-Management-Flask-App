from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DecimalField, RadioField, SelectField, TextAreaField, FileField, DateField, IntegerField
from wtforms.validators import InputRequired, Email, Length, NumberRange, Optional

class MedicalPatientForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    age = IntegerField('Age', render_kw={'readonly': True})
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[InputRequired()])
    contact_number = StringField('Contact Number', validators=[InputRequired(), Length(min=10, max=15)])
    email = StringField('Email', validators=[Optional(), Email()])
    address = TextAreaField('Address', validators=[InputRequired()])
    medical_history = TextAreaField('Medical History', validators=[Optional()])
    emergency_contact_name = StringField('Emergency Contact Name', validators=[InputRequired()])
    emergency_contact_number = StringField('Emergency Contact Number', validators=[InputRequired(), Length(min=10, max=15)])
    blood_group = SelectField('Blood Group', choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'),
                                                      ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'),
                                                      ('AB+', 'AB+'), ('AB-', 'AB-')], validators=[Optional()])
    photo = FileField('Photo', validators=[Optional()])
