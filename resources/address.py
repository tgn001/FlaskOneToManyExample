from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from db import db
from models import AddressModel
from schemas import AddressSchema, AddressUpdateSchema

empblueprint = Blueprint("Address", "address", description="TechGeekNext - Address CRUD operations")


@empblueprint.route("/employee/<string:emp_id>/address")
class EmployeeAdd(MethodView):

    @empblueprint.arguments(AddressSchema)
    @empblueprint.response(201, AddressSchema)
    def post(self, address_data, emp_id):
        addr = AddressModel(**address_data, emp_id=emp_id)
        try:
            db.session.add(addr)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while creating an address.")

        return


@empblueprint.route("/address/<string:add_id>")
class Address(MethodView):
    @empblueprint.response(200, AddressSchema)
    def get(self, add_id):
        return AddressModel.query.get_or_404(add_id)


    def delete(self, add_id):
        emp = AddressModel.query.get_or_404(add_id)
        db.session.delete(emp)
        db.session.commit()
        return {"message": "Address deleted."}

    @empblueprint.arguments(AddressUpdateSchema)
    @empblueprint.response(200, AddressSchema)
    def put(self, address_data, add_id):
        addr = AddressModel.query.get(add_id)

        if addr:
            addr.name = address_data["address"]
            addr.type = address_data["type"]
        else:
            addr = AddressModel(id=add_id, **address_data)

        db.session.add(addr)
        db.session.commit()

        return


@empblueprint.route("/address")
class GetAllAddress(MethodView):
    @empblueprint.response(200, AddressSchema(many=True))
    def get(self):
        return AddressModel.query.all()

