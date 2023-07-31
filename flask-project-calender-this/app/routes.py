from flask import Blueprint, render_template
import psycopg2
import os

bp = Blueprint('main', __name__, '/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}

@bp.route('/')
def main():
    conn = psycopg2.connect(**CONNECTION_PARAMETERS)
    cursor = conn.cursor()
    print(cursor)
    cursor.execute('''SELECT id, name, start_datetime, end_datetime
                    FROM appointments
                    ORDER BY start_datetime''')
    records = cursor.fetchall()
    
    return render_template('main.html', rows=records)