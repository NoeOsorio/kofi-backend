from flask import Flask
from endpoints.products.get_products import get_products

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/orders")
def get_orders():
    return ["order1", "order2", "order3"]

# @app.get("/products")
# def get_products_endpoint():
#     return get_products()

app.add_url_rule("/products", "get_products", get_products, methods=["GET"])

@app.post("/products")
def add_product():
    return "product added"

@app.get("/products/<int:id>")
def get_product(id):
    return "product " + str(id)

@app.put("/products/<int:id>")
def update_product(id):
    return "product " + str(id) + " updated"

@app.delete("/products/<int:id>")
def delete_product(id):
    return "product " + str(id) + " deleted"

@app.post("/reservations")
def add_reservation():
    return "reservation added"

@app.get("/reservations/<int:id>")
def get_reservation(id):
    return "reservation " + str(id)

@app.put("/reservations/<int:id>") 
def update_reservation(id):
    return "reservation " + str(id) + " updated"

@app.delete("/reservations/<int:id>")
def delete_reservation(id):
    return "reservation " + str(id) + " deleted"

@app.post("/auth/login")
def login():
    return "login"

@app.post("/auth/register")
def register():
    return "register"

@app.post("/auth/logout")
def logout():
    return "logout"
