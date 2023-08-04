from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectMultipleField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number',
                                  validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class MenuItemAssignmentForm(FlaskForm):
    menu_item_ids = SelectMultipleField("Menu items", coerce=int)
