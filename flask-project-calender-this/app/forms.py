from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DateField, TimeField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, ValidationError
from datetime import datetime

class AppointmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_datetime_date = DateField('Start Date', validators=[DataRequired()])
    start_datetime_time = TimeField('Start Time', validators=[DataRequired()])
    end_datetime_date = DateField('End Date', validators=[DataRequired()])
    end_datetime_time = TimeField('End Time', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    private = BooleanField('Private?')
    submit = SubmitField('Create An Appointment')

    def validate_end_datetime_date(form, field):
        start_date = datetime.combine(form.start_datetime_date.data, form.start_datetime_time.data)
        end_date = datetime.combine(field.data, form.end_datetime_time.data)

        if start_date >= end_date:
            msg = 'End date/time must come after start date/time'
            raise ValidationError(msg)
        
        if field.data != form.start_datetime_date.data:
            msg = 'End Date must be the same day as start date'
            raise ValidationError(msg)