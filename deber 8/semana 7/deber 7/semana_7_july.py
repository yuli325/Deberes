class Product:
    def __init__(self, name, price):
        """Constructor para inicializar los datos del producto"""
        self.name = name
        self.price = price
        print(f"Producto '{self.name}' con precio {self.price} agregado al inventario.")

    def display_product(self):
        """Método para mostrar la información del producto"""
        print(f"Producto: {self.name}, Precio: {self.price}")

    def __del__(self):
        """Destructor para liberar recursos cuando el producto ya no se necesita"""
        print(f"Producto '{self.name}' eliminado del inventario y recursos liberados.")

# Solicitar datos al usuario
name = input("Ingrese el nombre del producto: ")
price = float(input("Ingrese el precio del producto: "))

# Crear objeto de la clase Product
product = Product(name, price)

# Mostrar los datos del producto
product.display_product()

# Destruir el objeto explícitamente
del product

# Intentar acceder a los atributos después de destruir el objeto
try:
    print(product.name)  # Esto genera un error si el objeto ha sido destruido
except NameError as e:
    print(f"Error: {e} - El objeto sin datos disponibles.")
