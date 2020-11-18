from flask_restplus import Resource, reqparse, fields
from app.routes.test.provider import Provider
from app import ns_api


@ns_api.route('/test/<data>')
class Test(Resource):
    def get(self):
        return Provider.get_text()

    def post(self, ):
        return Provider.get_text()