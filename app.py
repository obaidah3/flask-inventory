from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from datetime import datetime
from bson import ObjectId
from flask_cors import CORS
import os
import json


# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure MongoDB URI from environment variable
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

# Initialize PyMongo
mongo = PyMongo(app)

# Root route to check connection
@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/sample_products', methods=['GET'])
def sample_products():
    with open('samples.json', encoding='utf-8') as f:
        samples = json.load(f)
    return jsonify({'samples': samples}), 200


# Add new product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    required_fields = ['name', 'quantity', 'price', 'category']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    product = {
        'name': data['name'],
        'quantity': int(data['quantity']),
        'price': float(data['price']),
        'category': data['category'],
        'created_at': datetime.utcnow()
    }
    mongo.db.products.insert_one(product)
    return jsonify({'message': 'Product added successfully'}), 201

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    products = list(mongo.db.products.find())
    for product in products:
        product['_id'] = str(product['_id'])
        product['created_at'] = product['created_at'].strftime('%Y-%m-%d %H:%M:%S')
    return jsonify(products), 200

# Delete a product
@app.route('/delete_product/<id>', methods=['DELETE'])
def delete_product(id):
    result = mongo.db.products.delete_one({'_id': ObjectId(id)})
    if result.deleted_count == 1:
        return jsonify({'message': 'Product deleted'}), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Update a product
@app.route('/update_product/<id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    update_data = {}
    for field in ['name', 'quantity', 'price', 'category']:
        if field in data:
            update_data[field] = data[field]

    result = mongo.db.products.update_one({'_id': ObjectId(id)}, {'$set': update_data})
    if result.modified_count == 1:
        return jsonify({'message': 'Product updated'}), 200
    else:
        return jsonify({'error': 'Product not found or no change'}), 404

# Apply bulk quantity reduction (used for checkout or sale)
@app.route('/apply_quantity_update', methods=['POST'])
def apply_quantity_update():
    data = request.get_json()
    if not isinstance(data, list):
        return jsonify({'error': 'Invalid data format'}), 400

    for item in data:
        if '_id' in item and 'quantity' in item:
            product_id = ObjectId(item['_id'])
            current = mongo.db.products.find_one({'_id': product_id})
            if current:
                new_quantity = max(0, current['quantity'] - int(item['quantity']))
                mongo.db.products.update_one({'_id': product_id}, {'$set': {'quantity': new_quantity}})

    return jsonify({'message': 'Quantities updated successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
