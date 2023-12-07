from flask import Flask
from endpoints.products import get_products, add_product, get_by_id, update_product, delete_product

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# Products
app.add_url_rule("/products", "get_products", get_products, methods=["GET"])
app.add_url_rule("/products", "add_product", add_product, methods=["POST"])
app.add_url_rule("/products/<string:product_id>", "get_by_id", get_by_id, methods=["GET"])
app.add_url_rule("/products/<string:product_id>", "update_product", update_product, methods=["PUT", "PATCH"])
app.add_url_rule("/products/<string:product_id>", "delete_product", delete_product, methods=["DELETE"])

# TODO: Reservations
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

# TODO: Auth

@app.post("/auth/login")
def login():
    return "login"

@app.post("/auth/register")
def register():
    return "register"

@app.post("/auth/logout")
def logout():
    return "logout"
