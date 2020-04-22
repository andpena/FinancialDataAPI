from flask import  Blueprint
from flask_restful import Api
from .resouces import GetQuotes
from ext.googledata import GoogleFinance

bp = Blueprint("restapi",__name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(GetQuotes,"/quotes/")
api.add_resource(GoogleFinance,"/google/")


def init_app(app):
    app.register_blueprint(bp)   