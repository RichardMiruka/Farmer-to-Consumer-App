#!/usr/bin/env python3

from flask import Flask
from flask_cors import CORS
from server.models import db, migrate
from server.routes import product_routes
from server.config import Config
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt = JWTManager(app)

    app.register_blueprint(product_routes)

    return app
