import io
import requests
import pandas as pd
from flask import jsonify, abort
from flask_restful import Resource
 
class GoogleFinance(Resource):
    def get(self):
        response = requests.get("https://docs.google.com/spreadsheets/d/e/2PACX-1vS52nHfxMgWeORfDwt8Qx-27OZU4uwOXFmJx5Ua2BYKHbEPD0Oadygbs7VG3SvAyPZnNFhUb5uFQUFM/pub?gid=171518392&single=true&output=csv").content
        df=pd.read_csv(io.StringIO(response.decode('utf-8')),decimal=b",")
        #df["Date"] = pd.to_datetime(df.Date, infer_datetime_format=True, unit="ns" ) 
        df=df[260-30:260]
        #columns=["Date","Open","High","Low","Close","Volume"]
        return jsonify(df.to_dict(orient="list"))