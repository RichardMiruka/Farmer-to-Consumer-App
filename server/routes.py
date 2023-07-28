from flask import Blueprint, request, jsonify, make_response, request
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
