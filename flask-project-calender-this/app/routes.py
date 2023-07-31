from flask import Blueprint, render_template, redirect, url_for
import psycopg2
import os
from app import forms
from datetime import datetime

bp = Blueprint('main', __name__, '/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route('/', methods = ['POST', 'GET'])
def main():
    curr_date = datetime.now()
    print(curr_date.strftime('%m'))
    url = url_for('.daily', year=curr_date.strftime('%Y'), month=curr_date.strftime('%m'), day=curr_date.strftime('%d'))
    return redirect(url)
    print(url)
    form = forms.AppointmentForm()
    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_datetime_date.data, form.start_datetime_time.data),
            'end_datetime': datetime.combine(form.end_datetime_date.data, form.end_datetime_time.data),
            'description': form.description.data,
            'private': form.private.data
        }
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                '''
                    INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
                    VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s);
                ''', 
                params)
                return redirect('/')
    else:
        conn = psycopg2.connect(**CONNECTION_PARAMETERS)
        cursor = conn.cursor()
        cursor.execute('''SELECT id, name, start_datetime, end_datetime
                        FROM appointments
                        ORDER BY start_datetime''')
        records = cursor.fetchall()
        
        return render_template('main.html', rows=records, form=form)


@bp.route('/<int:year>/<int:month>/<int:day>')
def daily(year, month, day):
    form = forms.AppointmentForm()
    if form.validate_on_submit():
        params = {
            'name': form.name.data,
            'start_datetime': datetime.combine(form.start_datetime_date.data, form.start_datetime_time.data),
            'end_datetime': datetime.combine(form.end_datetime_date.data, form.end_datetime_time.data),
            'description': form.description.data,
            'private': form.private.data
        }
        with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
            with conn.cursor() as curs:
                curs.execute(
                '''
                    INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
                    VALUES (%(name)s, %(start_datetime)s, %(end_datetime)s, %(description)s, %(private)s);
                ''', 
                params)
                return redirect('/')
    else:
        conn = psycopg2.connect(**CONNECTION_PARAMETERS)
        cursor = conn.cursor()
        cursor.execute('''SELECT id, name, start_datetime, end_datetime
                        FROM appointments
                        ORDER BY start_datetime''')
        records = cursor.fetchall()
        
        return render_template('main.html', rows=records, form=form)
    return f'{year}/{month}/{day}'