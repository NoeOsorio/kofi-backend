class Product():
    id: str
    name: str
    description: str
    price: float
    image_url: str
    category: str

    def __init__(self, name, description, price, image_url, category, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image_url = image_url
        self.category = category

    def __str__(self):
        return f'Product: {self.name.capitalize()}'

    def to_dict(self):
        product_dict = {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "category": self.category
        }
        if self.id is not None:
            product_dict["id"] = self.id
        return product_dict
