from flask import Flask, render_template
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def root():
    return 'Package Tracker'


@app.route('/new_package', methods=['POST', 'GET'])
def new_package():
    return render_template('shipping_request.html')