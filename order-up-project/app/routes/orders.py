from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.orm import joinedload
from flask_login import login_required
from ..models import db, Order, OrderDetail, Table, MenuItem, MenuItemType
from sqlalchemy.sql import functions as func
from ..forms import MenuItemAssignmentForm

bp = Blueprint('orders', __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    orders = db.session.query((OrderDetail.order_id),
                              Table.number,
                              Order.finished,
                              func.sum(MenuItem.price).label('total'))\
        .select_from(OrderDetail).join(Order).join(Table).join(MenuItem)\
        .group_by(OrderDetail.order_id, Table.number, Order.finished)\
        .order_by(Order.finished).order_by(Table.number).all()

    menu_items = MenuItem.query.join(MenuItemType)\
        .order_by(MenuItemType.name, MenuItem.name)\
        .all()

    form = MenuItemAssignmentForm()
    form.menu_item_ids.choices = [(item.id, item.name) for item in menu_items]

    return render_template('orders.html', orders=orders, form=form)


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


@bp.route('/orders/<int:id>/items', methods=['POST'])
@login_required
def add_items(id):
    menu_items = MenuItem.query.join(MenuItemType)\
        .order_by(MenuItemType.name, MenuItem.name)\
        .all()
    form = MenuItemAssignmentForm()
    form.menu_item_ids.choices = [(item.id, item.name) for item in menu_items]
    print(form.menu_item_ids.data)
    order = db.get_or_404(Order, id)
    if form.validate_on_submit():
        new_items = []
        for item in form.menu_item_ids.data:
            new_items.append(OrderDetail(order_id=id, menu_item_id=item))
        db.session.add_all(new_items)
        db.session.commit()
    return redirect(url_for('orders.index'))
