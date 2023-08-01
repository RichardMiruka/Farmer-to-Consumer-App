#!/usr/bin/env python3

from flask import Flask
from server.models import db, migrate
from flask_jwt_extended import JWTManager
from server.routes import product_routes
from server.config import Config
import secrets

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # we have to replace this with our actual secret key in production
    app.config['SECRET_KEY'] = 'your_flask_secret_key'

    # The we generate a random JWT secret key and set it in the app's configuration
    jwt_secret_key = secrets.token_hex(32)
    app.config['JWT_SECRET_KEY'] = jwt_secret_key

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(product_routes)

    return app
