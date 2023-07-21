from flask import Blueprint


bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/dashboard', methods=('GET', 'POST'))
def admin_dashboard():
    return '<h1>Admin Dashboard</h1>'