from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required
from ..models import db, Order, OrderDetail, Table, MenuItem, MenuItemType, \
    Employee
from sqlalchemy.sql import functions as func
from ..forms import MenuItemAssignmentForm, TableAssignmentForm

bp = Blueprint('orders', __name__, url_prefix='')


@bp.route('/')
@login_required
def index():
    # need to fix query so that orders show up when there are no details
    orders = db.session.query((Order.id),
                              Table.number,
                              Order.finished,
                              func.coalesce(func.sum(MenuItem.price),
                                            0).label('total'))\
        .select_from(Order).join(OrderDetail, full=True)\
        .join(Table, full=True).join(MenuItem, full=True)\
        .group_by(Order.id, Table.number, Order.finished)\
        .order_by(Order.finished).order_by(Table.number)

    print(orders)
    orders = orders.all()

    menu_items = MenuItem.query.join(MenuItemType)\
        .order_by(MenuItemType.name, MenuItem.name)\
        .all()

    menu_form = MenuItemAssignmentForm()
    menu_form.menu_item_ids.choices = [(item.id, item.name)
                                       for item in menu_items]

    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished == False)
    busy_table_ids = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_table_ids]
    servers = Employee.query.all()

    table_assign_form = TableAssignmentForm()
    table_assign_form.servers.choices = [(s.id, s.name) for s in servers]
    table_assign_form.tables.choices = [(t.id, f'Table {t.number}')
                                        for t in open_tables]

    return render_template('orders.html', orders=orders, menu_form=menu_form,
                           table_assign_form=table_assign_form)


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


@bp.route('/new_order', methods=['POST'])
@login_required
def new_order():
    tables = Table.query.order_by(Table.number).all()
    open_orders = Order.query.filter(Order.finished == False)
    busy_table_ids = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_table_ids]
    servers = Employee.query.all()

    table_assign_form = TableAssignmentForm()
    table_assign_form.servers.choices = [(s.id, s.name) for s in servers]
    table_assign_form.tables.choices = [(t.id, f'Table {t.number}')
                                        for t in open_tables]

    if table_assign_form.validate_on_submit():
        new_order = Order(employee_id=table_assign_form.servers.data,
                          table_id=table_assign_form.tables.data,
                          finished=False)
        db.session.add(new_order)
        db.session.commit()
        print(table_assign_form.servers.data)
        print(table_assign_form.tables.data)
    return redirect(url_for('orders.index'))
