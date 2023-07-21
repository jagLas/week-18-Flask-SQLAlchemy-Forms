from flask import Flask
from app.config import Config
from app import routes


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(routes.admin.bp)
app.register_blueprint(routes.main.bp)


# from app.routes import routes_base # noqa