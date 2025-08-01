from flask import Blueprint

bp = Blueprint("web_ui", __name__, url_prefix="/")

@bp.route("/")
def index_page():
    return "Hello, World!"

# Import other controllers
from .page import content