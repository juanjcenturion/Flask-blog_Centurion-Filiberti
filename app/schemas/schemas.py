from app import ma
from marshmallow import fields


class UserSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String()
    password = fields.String()
