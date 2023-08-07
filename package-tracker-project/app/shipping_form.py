from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

cities_list = tuple(map)

print(cities_list)

class ShippingForm(FlaskForm):
    sender = StringField('Sender Name', validators=[DataRequired()])
    recipient = StringField('Recipient Name', validators=[DataRequired()])
    origin = SelectField('Origin', choices=cities_list, validators=[DataRequired()])
    destination = SelectField('Destination', choices=cities_list, validators=[DataRequired()])
    express = BooleanField('Express Shipping',)
    submit = SubmitField('Submit')