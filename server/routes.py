from flask import Blueprint, request, jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from server.models import db, Product,Order, User, Reviews
import cloudinary
import cloudinary.uploader

product_routes = Blueprint('product_routes', __name__)

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
def view_all_products():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))

    # Query the products using pagination
    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    product_list = [
        {
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'image': product.image,
            'location': product.location,
            'quantity': product.quantity
        }
        for product in products.items
    ]

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

    response = make_response(jsonify(response_body), 200)
    response.headers['Content-Type'] = 'application/json'

    return response

@product_routes.route('/api/v1/products/<int:id>', methods=['GET'])
def view_product(id):
    product = Product.query.get(id)
    if not product:
        return jsonify({'message': 'Product not found'}), 404
    return jsonify(product.to_dict())


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
                'description': order.status,
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
                'description': user.status
            }
        user_list.append(user_data)

    return jsonify({
        'status': 'success',
        'data': user_list
    })


@product_routes.route('/api/v1/User/create', methods=['POST'])
def create_user():
    data = request.json

    user =User(
        username=data['username'],
        phone_number=data['phone_number'],
        password=data['password'],
        email=data['email'],                      
        user_type=data['user_type'],
        status=data['status']                      
          )
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@product_routes.route('/api/v1/Orders/create', methods=['POST'])
def create_order():
    data = request.json

    order =Order(
        product_id=data['product_id'],
        user_id=data['user_id'],
        status=data['status']                      
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
    

    
@product_routes.route('/api/v1/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user_id = get_jwt_identity()
    
    return jsonify({'message': 'You are accessing a protected route.', 'user_id': current_user_id}), 200  
    