""" 
id: Identificador único del producto (por ejemplo, un número o UUID).
nombre: Nombre del producto.
descripcion: Descripción detallada del producto.
precio: Precio del producto.
imagenUrl: URL de la imagen del producto.
categoria: Categoría a la que pertenece el producto (por ejemplo, bebidas, postres).
"""

class Product():
    id: int
    nombre: str
    descripcion: str
    precio: float
    imagenUrl: str
    categoria: str

    def __init__(self, id, nombre, descripcion, precio, imagenUrl, categoria):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagenUrl = imagenUrl
        self.categoria = categoria

    def __str__(self):
        return f'Product: {self.nombre}'
    
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "imagenUrl": self.imagenUrl,
            "categoria": self.categoria
        }