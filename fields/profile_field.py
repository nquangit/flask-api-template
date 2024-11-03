from flask_restful import fields
from libs.helper import TimestampField


user_profile_fields = {
    "id": fields.String,
    "email": fields.String,
    "name": fields.String,
    "picture": fields.String,
    "created_at": TimestampField(attribute="created_at"),
    "updated_at": TimestampField(attribute="updated_at"),
    "last_login_at": TimestampField(attribute="last_login_at"),
    "last_login_ip": fields.String(attribute="last_login_ip"),
}