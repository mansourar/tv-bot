from flask import request
from flask_restful import Resource

class Ping(Resource):

    def post(self):
        return {
            "Response": 200,
            "Message": "Server is up and ready"
        }
