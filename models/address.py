from db import db

class AddressModel(db.Model):
    __tablename__ = "address"

    id = db.Column(db.Integer, primary_key=True)
    addr = db.Column(db.String(80), unique=True, nullable=False)
    type = db.Column(db.String(80), unique=True, nullable=False)

    emp_id = db.Column(db.Integer, db.ForeignKey("employees.id"),  nullable=False)

