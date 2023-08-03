from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from ..models import db, Order, OrderDetail

bp = Blueprint('orders', __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)


@bp.route('/<int:id>/close', methods=['POST'])
@login_required
def close_table(id):
    order = db.get_or_404(Order, id)
    order.finished = True
    db.session.commit()

    return redirect(url_for('orders.index'))
