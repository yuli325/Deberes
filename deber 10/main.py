from inventario import Inventario
import traceback

def mostrar_menu():
    try:
        inventario = Inventario()  # Cargar el inventario desde el archivo al inicio
        while True:
            print("\n--- Menú de Gestión de Inventarios ---")
            print("1. Añadir nuevo producto (asegurarse de que el ID sea único)")
            print("2. Eliminar producto por ID")
            print("3. Actualizar nombre de un producto por ID")
            print("4. Buscar producto(s) por nombre")
            print("5. Mostrar todos los productos en el inventario")
            print("6. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                inventario.agregar_producto(id, nombre)

            elif opcion == "2":
                id = input("Ingrese el ID del producto a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "3":
                id = input("Ingrese el ID del producto a actualizar: ")
                nombre = input("Ingrese el nuevo nombre del producto: ")
                inventario.actualizar_producto(id, nombre)

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
    except Exception as e:
        print(f"Error inesperado: {e}")
        traceback.print_exc()  # Imprimir la traza completa del error

if __name__ == "__main__":
    mostrar_menu()
