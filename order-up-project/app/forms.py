from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, \
    SelectMultipleField, SelectField, widgets
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    employee_number = StringField('Employee Number',
                                  validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class MenuItemAssignmentForm(FlaskForm):
    menu_item_ids = MultiCheckboxField("Menu items", coerce=int)


class TableAssignmentForm(FlaskForm):
    tables = SelectField('Tables', coerce=int)
    servers = SelectField('Servers', coerce=int)
    assign = SubmitField('Assign')
