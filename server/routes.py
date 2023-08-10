from flask import Blueprint, request, jsonify, make_response, request, current_app
from server.models import db, Product,Order, User, Reviews
import cloudinary
import cloudinary.uploader
import jwt
from sqlalchemy import func
from datetime import datetime, timedelta
from flask_jwt_extended import jwt_required, get_jwt_identity, JWTManager
from werkzeug.security import generate_password_hash,check_password_hash
import requests
import base64
from requests.auth import HTTPBasicAuth

product_routes = Blueprint('product_routes', __name__)
consumer_key='0gc0uEwGcFcoxtHXIySEPF5ek4k8uvhf'
consumer_secret='6UvaqPmZWjdDlbGj'
my_endpoint = 'https://c001-41-80-116-223.ngrok-free.app' #callback url
@product_routes.route('/access_token')
def token():
    data = access_token()
    return data

def access_token():
    mpesa_auth_url='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    data = (requests.get(mpesa_auth_url, auth=HTTPBasicAuth(consumer_key,consumer_secret))).json()
    return data['access_token'] 

@product_routes.route('/pay',methods=['POST']) 
def MpesaExpress():
    data = request.json
    amount = data['amount']
    phone = data['phone']
    endpoint = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    access_token_value = access_token()
    print(access_token_value)
    headers = { "Authorization": "Bearer %s" %access_token_value}
    TimeStamp = datetime.now()
    times = TimeStamp.strftime("%Y%m%d%H%M%S")
    password = "174379" + "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919" + times
    datapass = base64.b64encode(password.encode('utf-8')).decode('utf-8') 
    data = {
        "BusinessShortCode": "174379",
        "Password": datapass,
        "Timestamp": times,
        "TransactionType": "CustomerPayBillOnline",
        "PartyA": phone, # fill with your phone number
        "PartyB": "174379",
        "PhoneNumber": phone, # fill with your phone number
        "CallBackURL": my_endpoint+ "/lmno-callback",
        "AccountReference": "ECO-GREEN FARMERS",
        "TransactionDesc": "HelloTest",
        "Amount": amount
    }
    res = requests.post(endpoint,json=data, headers = headers)
    print(res)
    return res.json()
@product_routes.route('/lmno-callback', methods=['POST'])
def incoming():
    data = request.get_json()
    print("Incoming Callback Request:")
    print(request.data.decode('utf-8'))
    callback_data = data.get('Body', {}).get('stkCallback', {})
    print(callback_data)
    return "ok"
    # Extract relevant information from the callback data
    # merchant_request_id = callback_data.get('MerchantRequestID')
    # checkout_request_id = callback_data.get('CheckoutRequestID')
    # result_code = callback_data.get('ResultCode')
    # result_desc = callback_data.get('ResultDesc')
    # mpesa_receipt_number = callback_data.get('CallbackMetadata', {}).get('Item', [])[1].get('Value')
    # transaction_date_str = datetime.now()
    # phone_number = callback_data.get('CallbackMetadata', {}).get('Item', [])[4].get('Value')
    # print(merchant_request_id)
    # try:
    #     # Find the user_id based on phone_number
    #     user = User.query.filter_by(phone_number=phone_number).first()

    #     if user:
    #         # Create an Order and save it to the database
            
    #         order = Order(
    #             user_id=user.id,
    #             mpesa_receipt_number=mpesa_receipt_number,
    #             merchant_request_id=merchant_request_id,
    #             checkout_request_id=checkout_request_id,
    #             result_code=result_code,
    #             result_desc=result_desc,
    #             order_status='Pending',  # You can set the initial status here
    #             phone_number=phone_number,
    #             amount=1.0,  # Adjust this according to your data
    #             transaction_date=transaction_date_str
    #         )
    #         db.session.add(order)
    #         db.session.commit()

    #         return jsonify({'message': 'Order created successfully'})
    #     else:
    #         return jsonify({'error': 'User not found'}), 404

    # except Exception as e:
    #     print(str(e))
    #     return jsonify({'error': str(e)}), 500
@product_routes.route('/register_urls')

@product_routes.route('/api/v1/products/create', methods=['POST'])
def create_product():
    data = request.form

    image = request.files.get('image')
    if image:
        result = cloudinary.uploader.upload(image)
        image_url = result['secure_url']
    else:
        image_url = None

    product = Product(
        name=data['name'],
        price=data['price'],
        description=data['description'],
        image=image_url,
        location=data['location'],                      
        quantity=data['quantity']
          )
    db.session.add(product)
    db.session.commit()
    return jsonify({'message': 'Product created successfully'}), 201
@product_routes.route('/api/v1/products', methods=['GET'])
@jwt_required()
def view_all_products():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 20))

    # Query the products using pagination
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    
    product_list = []

    for product in products.items:
        # Calculate average rating for the product
        avg_rating = db.session.query(func.avg(Reviews.rating)).filter_by(product_id=product.id).scalar()
        
        # Fetch comments for the product
        comments = Reviews.query.filter_by(product_id=product.id).all()
        comment_list = []

        for comment in comments:
            user = User.query.get(comment.user_id)
            if user:
                comment_data = {
                    'comment': comment.comment,
                    'user_username': user.username  # Fetch username from user
                }
                comment_list.append(comment_data)
        
        product_data = {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'image': product.image,
            'location': product.location,
            'quantity': product.quantity,
            'avg_rating': round(avg_rating, 1) if avg_rating else None,  # Rounded avg_rating
            'comments': comment_list  # Comments list
        }
        
        product_list.append(product_data)

        response_body = {
        'status': 'success',
        'data': product_list,
        'pagination': {
            'total': products.total,
            'pages': products.pages,
            'current_page': products.page,
            'next_page': products.next_num,
            'prev_page': products.prev_num,
            'per_page': products.per_page
        }
    }

    return jsonify(response_body), 200


@product_routes.route('/api/v1/products/<int:id>', methods=['GET'])
def view_product(id):
    product = Product.query.get(id)
    
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    
    # Calculate average rating for the product
    avg_rating = db.session.query(func.avg(Reviews.rating)).filter_by(product_id=id).scalar()
    
    # Fetch comments for the product
    comments = Reviews.query.filter_by(product_id=id).all()
    comment_list = []

    for comment in comments:
        user = User.query.get(comment.user_id)
        if user:
            comment_data = {
                'comment': comment.comment,
                'user_username': user.username  # Fetch username from user
            }
            comment_list.append(comment_data)
    
    product_data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'image': product.image,
        'location': product.location,
        'quantity': product.quantity,
        'avg_rating': round(avg_rating, 1) if avg_rating else None,  # Rounded avg_rating
        'comments': comment_list  # Comments list
    }

    return jsonify(product_data), 200

@product_routes.route('/api/v1/Orders', methods=['GET'])
def view_all_orders():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Query the products using pagination
    orders = Order.query.paginate(page=page, per_page=per_page, error_out=False)
    order_list= []
    for order in orders.items:

        order_data= {
                'id': order.id,
                'product_id': order.product_id,
                'user_id': order.user_id,
                'status': order.status,
                'orderDate':order.order_date
            }
        order_list.append(order_data)

    return jsonify({
        'status': 'success',
        'data': order_list
    })


@product_routes.route('/api/v1/Orders/<int:user_id>', methods=['GET'])
def view_my_orders(user_id):
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Query the products using pagination
    orders = Order.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page, error_out=False)
    order_list= []
    for order in orders.items:

        order_data= {
                'id': order.id,
                'product_id': order.product_id,
                'user_id': order.user_id,
                'status': order.status,
                'orderDate':order.order_date
            }
        order_list.append(order_data)

    return jsonify({
        'status': 'success',
        'data': order_list
    })


@product_routes.route('/api/v1/Reviews', methods=['GET'])
def view_all_reviews():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Query the products using pagination
    reviews = Reviews.query.paginate(page=page, per_page=per_page, error_out=False)
    review_list= []
    for review in reviews.items:
        review_data= {
                'id': review.id,
                'product_id': review.product_id,
                'user_id': review.user_id,
                'comment': review.comment,
                'rating' : review.rating
            }
        review_list.append(review_data)

    return jsonify({
        'status': 'success',
        'data': review_list,
        'pages': reviews.pages
    })
@product_routes.route('/api/v1/User', methods=['GET'])
def view_all_user():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Query the products using pagination
    user = User.query.paginate(page=page, per_page=per_page, error_out=False)
    user_list= []
    for user in user.items:
        user_data= {
                'id': user.id,
                'username': user.username,
                'phone number': user.phone_number,
                'email': user.email,
                'user_type' : user.user_type,
                'status': user.status,
                'password': user.password
            }
        user_list.append(user_data)

    return jsonify({
        'status': 'success',
        'data': user_list
    })


@product_routes.route('/api/v1/User/create', methods=['POST'])
def create_user():
    data = request.json

    username=data['username']
    phone_number=data['phone_number']
    password=data['password']
    email=data['email']                    
    user_type=data['user_type']
    status='Active'
    password_harsh= generate_password_hash(password)
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exist'}), 409
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email already exist'}), 409
    user= User(username=username, email=email, password=password_harsh, 
               user_type=user_type,status=status,phone_number=phone_number)

    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@product_routes.route('/api/v1/Orders/create', methods=['POST'])
@jwt_required()
def create_order():
    data = request.json

    order =Order(
        product_id=data['product_id'],
        user_id=data['user_id'],
        status=data['status'],
        order_date=datetime.utcnow()
          )
    db.session.add(order)
    db.session.commit()
    return jsonify({'message': 'Order has been taken into consideration'}), 201

@product_routes.route('/api/v1/Reviews/create', methods=['POST'])
def create_review():
    data = request.json

    review =Reviews(
        product_id=data['product_id'],
        user_id=data['user_id'],
        comment=data['comment'],                      
        rating=data['rating']                     
          )
    db.session.add(review)
    db.session.commit()
    return jsonify({'message': 'Reviews have been greatly appreciated'}), 201



@product_routes.route('/api/v1/Search', methods=['POST'])
def search():
    data = request.json
    user_id = data.get('user_id')
    keyword = data.get('keyword')
    
    if not user_id or not keyword:
        return jsonify({'error': 'Invalid request data'}), 400

    try:
        # Create a new Search record in the database
        search = Search(user_id=user_id, keyword=keyword)
        db.session.add(search)
        db.session.commit()
        
        products = Product.query.filter(Product.name.ilike(f'%{keyword}%')).all()
        product_list = []
        for product in products:
            product_data = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'description': product.description,
                'image': product.image,
                'location': product.location,
                'quantity': product.quantity
            }
            product_list.append(product_data)

        return jsonify({
            'status': 'success',
            'data': product_list
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500


@product_routes.route('/api/v1/Login', methods=['POST'])
def login():
    username =request.json["username"]
    password =request.json["password"]
    user=User.query.filter_by(username=username).first()
    if  user and check_password_hash(user.password, password):
        access_token=generate_token(user)
        return jsonify({
            "access-token" : access_token
        }), 200
    else:
        return jsonify({
            'error' :"Invalid credentials",
        }),401



def generate_token(user):
    secret_key=current_app.config['JWT_SECRET_KEY']
    expiration= datetime.utcnow()+timedelta(days=1)
    payload={
        "sub":user.id,
        "user_id":user.id,
        "exp":expiration,
        "username":user.username,
        "email":user.email,
        "usertype":user.user_type
    }
    token=jwt.encode(payload, secret_key, algorithm= 'HS256')
    return token