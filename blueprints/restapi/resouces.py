from datetime import date
from flask import jsonify, abort
from flask_restful import Resource


class GetQuotes(Resource):
    def get(self):
        Price = {
            str(date.today()):{"o":"1,00","h":"2,50","l":"0,50","c":"150"},
            "2020-03-22":{"o":"1,10","h":"2,51","l":"0,51","c":"150"},
            "2020-03-23":{"o":"1,15","h":"2,52","l":"0,52","c":"145"}
        }
        return jsonify(Price)