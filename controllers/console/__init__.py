from flask import Blueprint

from libs.external_api import ExternalApi

bp = Blueprint("console_api", __name__, url_prefix="/api")
api = ExternalApi(bp)

# Import other controllers
from .auth import login
from .user import profile
