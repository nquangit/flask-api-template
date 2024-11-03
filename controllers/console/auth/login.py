from services.account_service import AccountService
from flask_restful import Resource, reqparse
from controllers.console import api
from libs.helper import get_remote_ip
from flask import request


class LoginApi(Resource):
    """Resource for user login."""

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("token", type=str, required=True, location="json")
        args = parser.parse_args()

        if not args["token"]:
            return {"error": "Token is required"}

        access_token = AccountService.authenticate_with_google(
            args["token"], get_remote_ip(request)
        )
        if access_token:
            return {"status": "success", "data": access_token}, 200
        return {"status": "error", "message": "Invalid token"}


api.add_resource(LoginApi, "/login")
