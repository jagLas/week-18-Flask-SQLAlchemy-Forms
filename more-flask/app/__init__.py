from flask import Flask
from app.config import Config
from app.routes import admin


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(admin.bp)


from app import routes_base # noqa