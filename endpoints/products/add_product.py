from flask import request, jsonify
from firebase import db
from models.product import Product

def add_product():
    if(request.method == "POST"):
        try:
            data = request.json
            new_product = Product(**data)
            db.collection("products").add(new_product.to_dict())
            return jsonify({"message": "product added", "success": True}),201
        except Exception as e:
            return jsonify({"message": "error adding product", "error": str(e), "success": False}),400