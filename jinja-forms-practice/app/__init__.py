from flask import Flask, render_template
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return '<h1>Simple App</h1><a href="/form">Form</a>'

@app.route('/form')
def form():
    return render_template('form.html')