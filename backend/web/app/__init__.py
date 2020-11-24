from flask import Flask
from flask_restplus import Api
from flask_cors import CORS
from app.config import Config


server = Flask(__name__, static_folder='static')
server.config.from_object(Config())
cors = CORS(server, resources={r"/api/*": {"origins": "*"}})
api = Api(app=server)  # Api(app=server, doc=False) - отключить документацию

ns_api = api.namespace('api')
example = api.namespace('example')

import app.routes.test
