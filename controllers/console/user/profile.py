from flask_restful import Resource, fields, marshal_with, reqparse
from fields.profile_field import user_profile_fields
from flask_login import current_user
from controllers.console import api
from libs.login import login_required


class UserProfile(Resource):
    """Resource for user profile."""

    @login_required
    @marshal_with(user_profile_fields)
    def get(self):
        return current_user


api.add_resource(UserProfile, "/user/profile")
