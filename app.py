from dotenv import load_dotenv

load_dotenv()
import os
from flask_migrate import Migrate
from models.user import User
from services.account_service import AccountService
from commands import register_commands
import logging
import json
from flask_cors import CORS
from werkzeug.exceptions import Unauthorized
from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from configs import roboki_home_config

from extensions import (
    ext_database,
    ext_migrate,
    ext_login,
)
from extensions.ext_database import db
from extensions.ext_login import login_manager
from libs.passport import PassportService


logging.basicConfig(level=logging.DEBUG)


def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    ext_database.init_app(app)
    ext_migrate.init(app, db)
    ext_login.init_app(app)


# register blueprint routers
def register_blueprints(app):
    from controllers.console import bp as console_api_bp

    CORS(
        console_api_bp,
        resources={r"/*": {"origins": "*"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        expose_headers=["X-App"],
    )
    app.register_blueprint(console_api_bp, url_prefix="/api")


class RobokiHomeApp(Flask):
    pass


def create_flask_app_with_configs() -> Flask:
    """
    create a raw flask app
    with configs loaded from .env file
    """
    roboki_home_app = RobokiHomeApp(__name__)
    roboki_home_app.config.from_mapping(roboki_home_config.model_dump())

    # populate configs into system environment variables
    for key, value in roboki_home_app.config.items():
        if isinstance(value, str):
            os.environ[key] = value
        elif isinstance(value, int | float | bool):
            os.environ[key] = str(value)
        elif value is None:
            os.environ[key] = ""

    return roboki_home_app


def create_app() -> Flask:
    app = create_flask_app_with_configs()

    app.secret_key = app.config["SECRET_KEY"]

    register_blueprints(app)

    register_commands(app)
    initialize_extensions(app)

    return app


app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User}


@app.route("/health")
def health():
    return Response(
        json.dumps(
            {
                "pid": os.getpid(),
                "status": "ok",
                "version": app.config["CURRENT_VERSION"],
            }
        ),
        status=200,
        content_type="application/json",
    )


@login_manager.request_loader
def load_user_from_request(request_from_flask_login):
    """Load user based on the request header."""
    # if request.blueprint not in ["console"]:
    # return None
    print("request_from_flask_login", request_from_flask_login)
    auth_header = request.headers.get("Authorization", "")
    if not auth_header:
        auth_token = request.args.get("_token")
        if not auth_token:
            raise Unauthorized("Invalid Authorization token.")
    else:
        if " " not in auth_header:
            raise Unauthorized(
                "Invalid Authorization header format. Expected 'Bearer <api-key>' format."
            )
        auth_scheme, auth_token = auth_header.split(None, 1)
        auth_scheme = auth_scheme.lower()
        if auth_scheme != "bearer":
            raise Unauthorized(
                "Invalid Authorization header format. Expected 'Bearer <api-key>' format."
            )

    decoded = PassportService().verify(auth_token)
    user_id = decoded.get("user_id")

    user = AccountService.load_user_account(account_id=user_id)
    return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    """Handle unauthorized requests."""
    return Response(
        json.dumps({"status": "error", "message": "Unauthorized"}),
        status=401,
        content_type="application/json",
    )


@app.after_request
def after_request(response):
    """Add Version headers to the response."""
    response.set_cookie("remember_token", "", expires=0)
    response.headers.add("X-App", app.config["APPLICATION_NAME"])
    return response


if __name__ == "__main__":
    app.run()
