from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.fields.numeric import FloatField
from wtforms.validators import InputRequired, Email, Length


class MedicalSchemeForm(FlaskForm):
    scheme_name = StringField('Scheme Name', validators=[InputRequired(), Length(min=2, max=100)])
    scheme_code = StringField('Scheme Code', validators=[InputRequired(), Length(min=2, max=100)])
    scheme_administrator = StringField('Administrator', validators=[InputRequired(), Length(min=2, max=100)])
    scheme_contact_number = StringField('Contact Number', validators=[InputRequired(), Length(min=2, max=15)])
    scheme_email = StringField('Scheme Email', validators=[InputRequired(), Email(), Length(min=2, max=100)])
    scheme_address = TextAreaField('Scheme Address', validators=[InputRequired()])
    scheme_premium = FloatField('Scheme Premium', validators=[InputRequired()])
    scheme_status = SelectField('Scheme Status',
                                choices=[('active', 'Active'), ('inactive', 'Inactive'), ('cancelled', 'Cancelled')],
                                validators=[InputRequired()])