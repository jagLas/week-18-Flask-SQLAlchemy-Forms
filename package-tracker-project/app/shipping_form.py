from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField


class shipping_form(FlaskForm):
    sender_name = StringField('Sender Name')
    recipient_name = StringField('Recipient Name')
    origin = SelectField('Origin')
    destination = SelectField('Destination')
    express = BooleanField('Express Shipping')
    submit = SubmitField('Submit')