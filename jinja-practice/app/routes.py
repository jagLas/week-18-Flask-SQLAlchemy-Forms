from app import app
from flask import render_template
nav = [
  { 'href': 'https://appacademy.io', 'caption': 'App Academy' },
  { 'href': 'https://archive.or', 'caption': 'Internet Archive' },
]


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', sitename='My Sample', page='Home', logged_in=False, navigation = nav)

@app.route('/about')
def about():
    return render_template('index.html', sitename='My Sample', page='About')

@app.route('/item/<int:id>')
def item(id):
    return f'<h1>Item {id}</h1>'

@app.before_request
def before_request_function():
    print("before_request is running")

@app.after_request
def after_request_function(response):
    print("after_request is running")
    return response