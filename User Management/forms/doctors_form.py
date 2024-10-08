from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField, TextAreaField, FileField, DateField
from wtforms.validators import InputRequired, Email, Length, Optional


class DoctorRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(), Length(min=2, max=100)])
    last_name = StringField('Last Name', validators=[InputRequired(), Length(min=2, max=100)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[InputRequired()])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
                        validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email(), Length(max=100)])
    contact_number = StringField('Contact Number', validators=[InputRequired(), Length(min=10, max=15)])
    department = SelectField('Department',
                             choices=[('general', 'General'), ('cardiology', 'Cardiology'), ('neurology', 'Neurology'),
                                      ('pediatrics', 'Pediatrics')], validators=[InputRequired()])
    address = TextAreaField('Address', validators=[Optional(), Length(max=200)])
    profile_photo = FileField('Profile Photo', validators=[Optional()])