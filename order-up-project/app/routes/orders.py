from flask import Blueprint, render_template, redirect, url_for
from sqlalchemy.orm import joinedload
from flask_login import login_required
from ..models import db, Order, OrderDetail, Table

bp = Blueprint('orders', __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    orders = Order.query.options(joinedload(Order.table)).all()
    return render_template('orders.html', orders=orders)


@bp.route('/<int:id>/close', methods=['POST'])
@login_required
def close_table(id):
    order = db.get_or_404(Order, id)
    order.finished = True
    db.session.commit()

    return redirect(url_for('orders.index'))


@bp.route('/<int:id>/open', methods=['POST'])
@login_required
def open_table(id):
    order = db.get_or_404(Order, id)
    order.finished = False
    db.session.commit()

    return redirect(url_for('orders.index'))
