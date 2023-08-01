#!/usr/bin/env python3

from flask import Flask
from server.models import db, migrate
from server.routes import product_routes
from flask_jwt_extended import JWTManager
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_routes)

    return app
