from flask import jsonify, request
from . import app, db
from .models import Customer, Employee, Product, Order

@app.route('/api/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return jsonify([customer.serialize() for customer in customers]), 200

@app.route('/api/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.serialize() for employee in employees]), 200

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.serialize() for product in products]), 200

@app.route('/api/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([order.serialize() for order in orders]), 200

@app.route('/api/orders/customer/<customer_id>', methods=['GET'])
def get_orders_by_customer(customer_id):
    orders = Order.query.filter_by(CustomerID=customer_id).all()
    return jsonify([order.serialize() for order in orders]), 200

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        CustomerID=data['CustomerID'],
        EmployeeID=data['EmployeeID'],
        OrderDate=data['OrderDate'],
        RequiredDate=data['RequiredDate'],
        ShippedDate=data.get('ShippedDate'),
        ShipVia=data['ShipVia'],
        Freight=data['Freight'],
        ShipName=data['ShipName'],
        ShipAddress=data['ShipAddress'],
        ShipCity=data['ShipCity'],
        ShipRegion=data.get('ShipRegion'),
        ShipPostalCode=data['ShipPostalCode'],
        ShipCountry=data['ShipCountry']
    )
    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order.serialize()), 201
