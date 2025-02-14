class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, id, nombre, cantidad, precio):
        if any(p.get_id() == id for p in self.productos):
            print(f"Error: Ya existe un producto con el ID {id}. No se puede agregar.")
            return
        nuevo_producto = Producto(id, nombre, cantidad, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto {nombre} agregado al inventario.")

    def eliminar_producto(self, id):
        producto_a_eliminar = None
        for producto in self.productos:
            if producto.get_id() == id:
                producto_a_eliminar = producto
                break
        if producto_a_eliminar:
            self.productos.remove(producto_a_eliminar)
            print(f"Producto con ID {id} eliminado.")
        else:
            print(f"No se encontró un producto con ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.get_id() == id:
                if cantidad is not None:
                    producto.set_cantidad(cantidad)
                if precio is not None:
                    producto.set_precio(precio)
                print(f"Producto con ID {id} actualizado.")
                return
        print(f"No se encontró un producto con ID {id}.")

    def buscar_producto(self, nombre):
        productos_encontrados = [producto for producto in self.productos if nombre.lower() in producto.get_nombre().lower()]
        if productos_encontrados:
            print("Productos encontrados:")
            for producto in productos_encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if self.productos:
            print("\nInventario de productos:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")

def mostrar_menu():
    inventario = Inventario()
    while True:
        print("\n--- Menú de Gestión de Inventarios ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(id, nombre, cantidad, precio)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("¡Gracias por usar el sistema de inventario! Hasta luego.")
            break

        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    mostrar_menu()
