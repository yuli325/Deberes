from producto import Producto
from inventario import Inventory
import traceback

def show_menu():
    """Muestra el menú de opciones y maneja la entrada del usuario"""
    try:
        inventory = Inventory()  # Inicializa el objeto de inventario y carga los datos desde el archivo
        while True:
            print("\n--- Sistema de Gestión de Inventarios ---")
            print("1. Agregar un nuevo producto (ID debe ser único)")
            print("2. Eliminar producto por ID")
            print("3. Actualizar stock o precio de un producto")
            print("4. Buscar productos por nombre")
            print("5. Ver todos los productos en el inventario")
            print("6. Salir")

            user_choice = input("Elige una opción: ")

            if user_choice == "1":
                # Solicita al usuario los detalles del producto a agregar
                product_id = input("Ingresa el ID del producto: ")
                name = input("Ingresa el nombre del producto: ")
                stock = int(input("Ingresa la cantidad de stock: "))
                price = float(input("Ingresa el precio del producto: "))
                inventory.add_product(product_id, name, stock, price)

            elif user_choice == "2":
                # Solicita al usuario el ID del producto a eliminar
                product_id = input("Ingresa el ID del producto a eliminar: ")
                inventory.remove_product(product_id)

            elif user_choice == "3":
                # Solicita al usuario el ID del producto a actualizar
                product_id = input("Ingresa el ID del producto a actualizar: ")
                new_stock = int(input("Ingresa la nueva cantidad de stock: "))
                new_price = float(input("Ingresa el nuevo precio: "))
                for product in inventory.items:
                    if product.get_id() == product_id:
                        # Actualiza el stock y precio del producto
                        product.set_stock(new_stock)
                        product.set_price(new_price)
                        inventory.save_inventory()  # Guarda el inventario actualizado
                        print(f"Producto con ID {product_id} actualizado.")
                        break

            elif user_choice == "4":
                # Solicita al usuario el nombre del producto a buscar
                name = input("Ingresa el nombre del producto a buscar: ")
                inventory.search_product(name)

            elif user_choice == "5":
                # Muestra todos los productos en el inventario
                inventory.display_inventory()

            elif user_choice == "6":
                print("¡Gracias por usar el sistema de inventario! Hasta luego.")
                break

            else:
                print("Opción no válida. Por favor, intenta de nuevo.")
    except Exception as e:
        print(f"Error inesperado: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    show_menu()
