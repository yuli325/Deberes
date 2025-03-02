import traceback
import os
from producto import Producto

class Inventory:
    def __init__(self, filename="inventory"):
        # Inicializa el inventario, cargando productos desde un archivo si existe.
        self.filename = filename
        self.items = []  # Lista para almacenar los productos del inventario
        self.load_inventory()  # Carga el inventario desde el archivo

    def load_inventory(self):
        """Carga los productos desde el archivo si existe"""
        try:
            if os.path.isfile(self.filename + ".txt"):  # Verifica si el archivo existe
                with open(self.filename + ".txt", "r") as file:
                    for line in file:
                        # Divide la línea del archivo y crea un nuevo producto
                        product_id, name, stock, price = line.strip().split(",")
                        product = Producto(product_id, name, int(stock), float(price))
                        self.items.append(product)  # Agrega el producto a la lista
                print("Inventario cargado exitosamente.")
            else:
                print(f"Archivo {self.filename}.txt no encontrado, se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")
            traceback.print_exc()

    def save_inventory(self):
        """Guarda el inventario actual en un archivo de texto"""
        try:
            with open(self.filename + ".txt", "w") as file:
                for product in self.items:
                    # Guarda el ID, nombre, stock y precio de cada producto en el archivo
                    file.write(f"{product.get_id()},{product.get_name()},{product.get_stock()},{product.get_price()}\n")
            print("Inventario guardado exitosamente.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")
            traceback.print_exc()

    def add_product(self, product_id, name, stock, price):
        """Agrega un nuevo producto al inventario"""
        try:
            # Verifica si ya existe un producto con el mismo ID
            if any(item.get_id() == product_id for item in self.items):
                print(f"¡El producto con ID {product_id} ya existe!")
                return
            # Crea un nuevo producto y lo agrega al inventario
            new_product = Producto(product_id, name, stock, price)
            self.items.append(new_product)
            print(f"Producto {name} agregado al inventario.")
            self.save_inventory()  # Guarda el inventario actualizado en el archivo
        except Exception as e:
            print(f"Error al agregar el producto: {e}")
            traceback.print_exc()

    def remove_product(self, product_id):
        """Elimina un producto del inventario usando su ID"""
        try:
            # Busca el producto con el ID proporcionado
            product_to_remove = next((item for item in self.items if item.get_id() == product_id), None)
            if product_to_remove:
                self.items.remove(product_to_remove)  # Elimina el producto de la lista
                print(f"Producto con ID {product_id} eliminado del inventario.")
                self.save_inventory()  # Guarda el inventario actualizado
            else:
                print(f"No se encontró un producto con el ID {product_id}.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")
            traceback.print_exc()

    def search_product(self, name):
        """Busca productos por nombre, con coincidencias parciales"""
        try:
            # Filtra los productos que contienen el nombre dado
            results = [item for item in self.items if name.lower() in item.get_name().lower()]
            if results:
                print("Productos encontrados:")
                for product in results:
                    # Muestra los detalles de cada producto encontrado
                    print(f"ID: {product.get_id()}, Nombre: {product.get_name()}, Stock: {product.get_stock()}, Precio: {product.get_price()}")
            else:
                print("No se encontraron productos con ese nombre.")
        except Exception as e:
            print(f"Error al buscar productos: {e}")
            traceback.print_exc()

    def display_inventory(self):
        """Muestra todos los productos en el inventario"""
        try:
            if self.items:
                print("\nInventario actual:")
                for product in self.items:
                    # Muestra el ID, nombre, stock y precio de cada producto
                    print(f"ID: {product.get_id()}, Nombre: {product.get_name()}, Stock: {product.get_stock()}, Precio: {product.get_price()}")
            else:
                print("El inventario está vacío.")
        except Exception as e:
            print(f"Error al mostrar el inventario: {e}")
            traceback.print_exc()
