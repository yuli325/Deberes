from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def mostrar_menu():
    print("\n----- Menú de la Biblioteca -----")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Dar de baja usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Ver libros prestados")
    print("9. Salir")

def main():
    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        try:
            if opcion == "1":
                titulo = input("Título del libro: ")
                autor = input("Autor del libro: ")
                categoria = input("Categoría del libro: ")
                isbn = input("ISBN del libro: ")
                libro = Libro(titulo, autor, categoria, isbn)
                biblioteca.añadir_libro(libro)

            elif opcion == "2":
                isbn = input("ISBN del libro a quitar: ")
                biblioteca.quitar_libro(isbn)

            elif opcion == "3":
                nombre = input("Nombre del usuario: ")
                id_usuario = input("ID de usuario: ")
                biblioteca.registrar_usuario(nombre, id_usuario)

            elif opcion == "4":
                id_usuario = input("ID del usuario a dar de baja: ")
                biblioteca.dar_baja_usuario(id_usuario)

            elif opcion == "5":
                isbn = input("ISBN del libro a prestar: ")
                id_usuario = input("ID del usuario: ")
                biblioteca.prestar_libro(isbn, id_usuario)

            elif opcion == "6":
                isbn = input("ISBN del libro a devolver: ")
                id_usuario = input("ID del usuario: ")
                biblioteca.devolver_libro(isbn, id_usuario)

            elif opcion == "7":
                criterio = input("Criterio de búsqueda (titulo, autor, categoria): ")
                valor = input(f"Valor para {criterio}: ")
                resultados = biblioteca.buscar_libro(criterio, valor)
                print("Libros encontrados:")
                for libro in resultados:
                    print(libro)

            elif opcion == "8":
                libros_prestados = biblioteca.listar_libros_prestados()
                print("Libros prestados actualmente:")
                for libro in libros_prestados:
                    print(libro)

            elif opcion == "9":
                print("Saliendo del sistema de biblioteca...")
                break

            else:
                print("Opción no válida, por favor intenta de nuevo.")
        
        except Exception as e:
            import traceback
            print("Se ha producido un error inesperado.")
            traceback.print_exc()

if __name__ == "__main__":
    main()
