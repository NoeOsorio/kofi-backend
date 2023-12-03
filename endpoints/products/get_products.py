from models.product import Product
from flask import request, jsonify

products = [Product(1, "Coca Cola", "Refresco de cola", 15.0, "https://www.coca-cola.com.mx/content/dam/journey/mx/es/private/historias/2018/07/la-historia-de-la-coca-cola-light/coca-cola-light-1982.jpg", "bebidas"), Product(2, "Pepsi", "Refresco de cola", 15.0, "https://www.coca-cola.com.mx/content/dam/journey/mx/es/private/historias/2018/07/la-historia-de-la-coca-cola-light/coca-cola-light-1982.jpg", "bebidas"), Product(3, "Fanta", "Refresco de naranja", 15.0, "https://www.coca-cola.com.mx/content/dam/journey/mx/es/private/historias/2018/07/la-historia-de-la-coca-cola-light/coca-cola-light-1982.jpg", "bebidas")]

def get_products():
    if(request.method == "GET"):
        return jsonify([product.to_dict() for product in products])
    