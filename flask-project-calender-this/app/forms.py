from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TimeField, TextAreaField, BooleanField

class AppointmentForm(FlaskForm):
    name = StringField('Name')
    start_datetime_date = DateField('Start Date')
    start_datetime_time = TimeField('Start Time')
    end_datetime_date = DateField('End Date')
    end_datetime_time = TimeField('End Time')
    description = TextAreaField('Description')
    private = BooleanField('Private?')
    submit = SubmitField('Create An Appointment')