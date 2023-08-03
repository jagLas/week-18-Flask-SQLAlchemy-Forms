from dotenv import load_dotenv
load_dotenv()

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order, OrderDetail


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, type=sides, menu=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    # db.session.add(beverages)
    db.session.add_all([beverages, entrees, sides, dinner, fries, drp, jambalaya])
    db.session.commit()

    table1 = Table(number=13, capacity=4)
    table2 = Table(number=7, capacity=6)

    order = Order(employee=employee, table=table2, finished=False)
    detail1 = OrderDetail(order=order, item=fries)
    detail2 = OrderDetail(order=order, item=jambalaya)
    detail3 = OrderDetail(order=order, item=fries)

    order2 = Order(employee=employee, table=table1, finished=False)
    detail4 = OrderDetail(order=order2, item=drp)

    db.session.add_all([table1, table2, order, detail1, detail2, detail3, order2, detail4])
    db.session.commit()
