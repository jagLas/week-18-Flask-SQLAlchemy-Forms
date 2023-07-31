from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TimeField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_datetime_date = DateField('Start Date', validators=[DataRequired()])
    start_datetime_time = TimeField('Start Time', validators=[DataRequired()])
    end_datetime_date = DateField('End Date', validators=[DataRequired()])
    end_datetime_time = TimeField('End Time', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    private = BooleanField('Private?')
    submit = SubmitField('Create An Appointment')