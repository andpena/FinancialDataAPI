from flask import Blueprint
from .dashboard_view import index

bp = Blueprint("webui", __name__,template_folder="templates/")
bp.add_url_rule("/dashboard", view_func=index)

def init_app(app):
    app.register_blueprint(bp)