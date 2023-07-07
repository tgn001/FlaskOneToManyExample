from marshmallow import Schema, fields

class AddressSchema(Schema):
    id = fields.Str(dump_only=True)
    addr = fields.Str(required=True)
    type = fields.Str(required=True)
    emp_id = fields.Str(dump_only=True)


class AddressUpdateSchema(Schema):
    addr = fields.Str()
    type = fields.Str()


class EmployeeSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    addresses = AddressSchema

class EmployeeUpdateSchema(Schema):
    name = fields.Str()
    role = fields.Str()
