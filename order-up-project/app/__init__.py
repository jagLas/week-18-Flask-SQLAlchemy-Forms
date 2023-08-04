from flask import Flask
from .config import Configuration
from .routes import orders, session
from .models import db, Employee
from flask_login import LoginManager

app = Flask(__name__,
            static_url_path='',
            static_folder='static')
app.config.from_object(Configuration)
app.register_blueprint(orders.bp)
app.register_blueprint(session.bp)
db.init_app(app)

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))
