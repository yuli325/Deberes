class Producto:
    def __init__(self, product_id, product_name, stock, price):
        # Inicializa un producto con su ID, nombre, cantidad (stock) y precio.
        self.product_id = product_id
        self.product_name = product_name
        self.stock = stock
        self.price = price

    def get_id(self):
        # Devuelve el ID del producto
        return self.product_id

    def set_id(self, new_id):
        # Establece un nuevo ID para el producto
        self.product_id = new_id

    def get_name(self):
        # Devuelve el nombre del producto
        return self.product_name

    def set_name(self, new_name):
        # Establece un nuevo nombre para el producto
        self.product_name = new_name

    def get_stock(self):
        # Devuelve la cantidad de stock disponible del producto
        return self.stock

    def set_stock(self, new_stock):
        # Establece una nueva cantidad de stock para el producto
        self.stock = new_stock

    def get_price(self):
        # Devuelve el precio del producto
        return self.price

    def set_price(self, new_price):
        # Establece un nuevo precio para el producto
        self.price = new_price
