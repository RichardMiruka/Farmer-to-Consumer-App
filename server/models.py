from flask_sqlalchemy import SQLAlchemy
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
    status = db.Column(db.String())
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