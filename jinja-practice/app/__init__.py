from flask import Flask, render_template
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)
# print(sorted(list(app.config)))

from app import routes # noqa