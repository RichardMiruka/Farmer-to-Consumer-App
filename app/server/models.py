from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__='Users'
    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, index=True,nullable
                      = False)
    userType=db.Column(db.String)
    status= db.Column(db.String)
    phoneNumber= db.Column(db.Integer)
    createdOn = db.Column(db.DateTime, default=datetime.utcnow)

class Product(db.Model):
    __tablename__ ='Products'
    productName =  db.Column('productname', db.VARCHAR(250),
                             primary_key= True )
    price = db.Column(db.DECIMAL(18))
    description = db.Column(db.Text)
    imageURL = db.Column(db.String)
    categoryId = db.Column("categoryid",
                           db.ForeignKey('Categories.categoryId'),
                           nullable=False,)
    quantityInStock = db.Column(db.INTEGER)
    createdAt = db.Column(db.TIMESTAMP,
                          server_default=db.text("(CURRENT_TIMESTAMP)"),
                          nullable=False)
    location=db.Column(db.String)
    
class Review(db.Model):
    __tablename__ = 'Reviews'

    id = db.Column(db.Integer, primary_key=True)
    productId = db.Column(db.String)
    rating = db.Column(db.Float)
    comment = db.Column(db.String)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Reviews {self.title}, published at {self.published_at}.>'
