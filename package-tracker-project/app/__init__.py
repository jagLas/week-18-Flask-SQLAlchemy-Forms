from flask import Flask, render_template
from app.config import Config
from app.shipping_form import ShippingForm
from flask_migrate import Migrate
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def root():
    return 'Package Tracker'


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        return 'Success'
    return render_template('shipping_request.html', form=form)