from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
print(sorted(list(app.config)))

@app.route('/')
def index():
    return '<h1>Sample App</h1>'