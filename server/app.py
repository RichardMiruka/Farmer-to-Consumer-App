#!/usr/bin/env python3

from flask import Flask
from server.models import db, migrate
from server.routes import product_routes
from flask_jwt_extended import JWTManager
from server.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'your_secret_key'

# Set up JWT
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Replace with a long random string
    jwt = JWTManager(app)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_routes)

    return app
