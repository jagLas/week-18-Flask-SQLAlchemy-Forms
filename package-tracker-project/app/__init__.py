from flask import Flask, render_template, redirect
from app.config import Config
from app.shipping_form import ShippingForm
from flask_migrate import Migrate
from app.models import db, Package

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def root():
    packages = Package.query.all()
    return render_template('root.html', packages=packages)


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    form = ShippingForm()
    if form.validate_on_submit():
        Package.advance_all_locations()
        data = form.data.copy()
        data.pop('submit')
        data.pop('csrf_token')
        new_package = Package(location=data['origin'], **data)
        db.session.add(new_package)
        db.session.commit()
        return redirect('/')
    return render_template('shipping_request.html', form=form)