from flask import Flask
from flask_restplus import Api
from flask_cors import CORS

server = Flask(__name__, static_folder='static')
server.config["JSON_AS_ASCII"] = False
cors = CORS(server, resources={r"/api/*": {"origins": "*"}})
api = Api(app=server)

ns_api = api.namespace('api')

import app.routes.test
