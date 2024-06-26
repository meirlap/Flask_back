from . import db

class Customer(db.Model):
    __tablename__ = 'Customers'
    CustomerID = db.Column(db.String, primary_key=True)
    CompanyName = db.Column(db.String)
    ContactName = db.Column(db.String)
    ContactTitle = db.Column(db.String)

    def serialize(self):
        return {
            'CustomerID': self.CustomerID,
            'CompanyName': self.CompanyName,
            'ContactName': self.ContactName,
            'ContactTitle': self.ContactTitle
        }

class Employee(db.Model):
    __tablename__ = 'Employees'
    EmployeeID = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String)
    FirstName = db.Column(db.String)
    Title = db.Column(db.String)

    def serialize(self):
        return {
            'EmployeeID': self.EmployeeID,
            'LastName': self.LastName,
            'FirstName': self.FirstName,
            'Title': self.Title
        }

class Product(db.Model):
    __tablename__ = 'Products'
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String)
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String)
    UnitPrice = db.Column(db.Float)

    def serialize(self):
        return {
            'ProductID': self.ProductID,
            'ProductName': self.ProductName,
            'SupplierID': self.SupplierID,
            'CategoryID': self.CategoryID,
            'QuantityPerUnit': self.QuantityPerUnit,
            'UnitPrice': self.UnitPrice
        }

class Order(db.Model):
    __tablename__ = 'Orders'
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.String)
    EmployeeID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)

    def serialize(self):
        return {
            'OrderID': self.OrderID,
            'CustomerID': self.CustomerID,
            'EmployeeID': self.EmployeeID,
            'OrderDate': self.OrderDate
        }
