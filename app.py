import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://erick_mwangi2:HEChbH3vMsoiYH2CuBXdUGRq02oXEY0g@dpg-cig2hftgkuvojjf3jg30-a.ohio-postgres.render.com/bird_app_lz1c'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.json.compact = False

migrate = Migrate(application, db)
db.init_app(application)

api = Api(application)

class Birds(Resource):
    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Birds, '/birds')
