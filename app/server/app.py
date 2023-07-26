#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, Review, User, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Register models with SQLAlchemy
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'Page for Sharoun The Innovator'

if __name__ == '__main__':
    app.run(port=5555)
