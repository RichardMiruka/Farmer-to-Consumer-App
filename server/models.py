from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float,ForeignKey
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(200))  # Cloudinary public_id for the image
    location = db.Column(db.String(100))
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'image': self.image,
            'location': self.location,
            'quantity': self.quantity
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    phone_number = db.Column(db.Float, nullable=False)
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)  # Cloudinary public_id for the image
    user_type = db.Column(db.String())
    status = db.Column(db.String())
    def repr(self):
        return f'<User {self.id}>'
    


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    amount = db.Column(db.Float, nullable=False)
    mpesa_receipt_number = db.Column(db.String(255), nullable=False)
    merchant_request_id = db.Column(db.String(255), nullable=False)
    checkout_request_id = db.Column(db.String(255), nullable=False)
    result_code = db.Column(db.Integer, nullable=False)
    result_desc = db.Column(db.String(255), nullable=False)
    order_status = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    transaction_date=db.Column(db.DateTime)

    product=db.relationship('Product', backref= db.backref('orders', lazy=True))
    user=db.relationship('User', backref= db.backref('orders', lazy=True))
    
    def repr(self):
        return f'<Order {self.id}>'

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable= False)
    comment= db.Column(db.String())
    rating = db.Column(db.Integer())
    product=db.relationship('Product', backref= db.backref('reviews', lazy=True))
    user=db.relationship('User', backref= db.backref('reviews', lazy=True))


    def repr(self):
        return f'<Review {self.id}>'


class Search(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    keyword = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('searches', lazy=True))

    def repr(self):
        return f'<Search {self.id}>'