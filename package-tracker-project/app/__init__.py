from flask import Flask, render_template
from app.config import Config
from app.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def root():
    return 'Package Tracker'


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return 'Success'
    return render_template('shipping_request.html', form=form)