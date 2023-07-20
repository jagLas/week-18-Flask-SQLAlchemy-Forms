from flask import (Flask, render_template, redirect)
from app.config import Config
from app.sample_form import SampleForm


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return '<h1>Simple App</h1><a href="/form">Form</a>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = SampleForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('form.html', form=form)