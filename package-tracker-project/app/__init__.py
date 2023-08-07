from flask import Flask, render_template
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def root():
    return 'Package Tracker'