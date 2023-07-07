from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80), unique=True, nullable=False)

    addresses = db.relationship("AddressModel", backref="employees")