from models.product import Product
from flask import request, jsonify
from firebase import db


def get_products():
    if (request.method == "GET"):
        try:
            products_ref = db.collection("products").get()
            products = [Product(id=product.id, **product.to_dict())
                        for product in products_ref]
            return jsonify([product.to_dict() for product in products]), 200
        except Exception as e:
            return jsonify({"message": "error getting products", "error": str(e), "success": False}), 400


def get_by_id(product_id):
    if (request.method == "GET"):
        try:
            products_ref = db.collection("products").document(product_id).get()
            if (products_ref.exists):
                product = Product(id=products_ref.id, **products_ref.to_dict())
                return jsonify(product.to_dict()), 200
            else:
                return jsonify({"message": "product not found", "success": False}), 404
        except Exception as e:
            return jsonify({"message": "error getting product", "error": str(e), "success": False}), 400


def add_product():
    if (request.method == "POST"):
        try:
            data = request.json
            new_product = Product(**data)
            db.collection("products").add(new_product.to_dict())
            return jsonify({"message": "product added", "success": True}), 201
        except Exception as e:
            return jsonify({"message": "error adding product", "error": str(e), "success": False}), 400
