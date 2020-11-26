from flask_restplus import Resource, abort
from app import ns_api


@ns_api.route('/git-webhook', methods=['POST'])
class GitWebhook(Resource):

    def post(self):
        print(ns_api.payload)
        return {'status': 'ok'}
  