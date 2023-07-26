from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

review_user =db.Table(
    'reviews_users',
    db.Column('review_id', db.Integer, db.ForeignKey('Reviews.id'),primary_key= True ),
    db.Column('user_id', db.Integer, db.ForeignKey('Users.id'),primary_key=True ),

)
review_product=db.Table(
    'review_products',
    db.Column('review_id', db.Integer, db.ForeignKey('Reviews.id'), primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey('Products.id'), primary_Key=True),
    db.Column('rating', db.Float),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now())
)

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

    id = db.Column(db.Integer, primary_key=True)
    productName =  db.Column(db.String)
    price = db.Column(db.Integer(18))
    description = db.Column(db.Text)
    imageURL = db.Column(db.String)
    categoryId = db.Column(db.ForeignKey('Categories.categoryId'),nullable=False,)
    quantityInStock = db.Column(db.INTEGER)
    createdAt = db.Column(db.TIMESTAMP,server_default=db.text("(CURRENT_TIMESTAMP)"),nullable=False)
    location=db.Column(db.String)
    rating = db.Column(db.Float)
    
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
