from flask import Flask
from flask_restplus import Api
from flask_cors import CORS


flask = Flask(__name__, static_folder='static')
flask.config["JSON_AS_ASCII"] = False
cors = CORS(flask, resources={r"/api/*": {"origins": "*"}})
api = Api(app=flask)

ns_api = api.namespace('api')

import app.routes.test
