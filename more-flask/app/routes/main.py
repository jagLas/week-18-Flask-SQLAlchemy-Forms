from flask import Blueprint, session
bp = Blueprint('main', __name__,)

@bp.route('/')
@bp.route('/home')
def index():
    return '<h1>Home</h1>'

@bp.route('/about')
def about():
    return '<h1>About</h1>'

@bp.route('/item/<int:id>')
def item(id):
    return f'<h1>Item {id}</h1>'

@bp.before_request
def before_request_function():
    print("before_request is running")

@bp.after_request
def after_request_function(response):
    print("after_request is running")
    return response

@bp.route('/visits-counter/')
def visits():
    if 'visits' in session:
        session['visits'] = session.get('visits') + 1
    else:
        session['visits'] = 1

    return 'Total Visits: {}'.format(session.get('visits'))

@bp.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)
    return 'Visits deleted'