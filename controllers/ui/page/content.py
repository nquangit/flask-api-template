from controllers.ui import bp

@bp.route("/content")
def content():
    return "Content Page"

