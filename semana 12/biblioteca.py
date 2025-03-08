from libro import Libro
from usuario import Usuario
import traceback

class Biblioteca:
    def __init__(self):
        try:
            self.libros = {}  # Diccionario para almacenar libros con su ISBN como clave
            self.usuarios = set()  # Conjunto de usuarios registrados para garantizar unicidad
        except Exception as e:
            # Manejo de error en caso de falla al inicializar la biblioteca
            print(f"Error al inicializar la biblioteca: {e}")
            traceback.print_exc()

    def añadir_libro(self, libro):
        try:
            if libro.isbn not in self.libros:
                self.libros[libro.isbn] = libro
                print(f"Libro '{libro.titulo}' añadido correctamente.")
            else:
                print(f"El libro '{libro.titulo}' ya se encuentra en la biblioteca.")
        except Exception as e:
            # Si ocurre un error al añadir un libro, se muestra la traza
            print(f"Error al añadir el libro: {e}")
            traceback.print_exc()

    def quitar_libro(self, isbn):
        try:
            if isbn in self.libros:
                libro = self.libros.pop(isbn)
                print(f"Libro '{libro.titulo}' eliminado de la biblioteca.")
            else:
                print(f"No se encontró el libro con el ISBN {isbn}.")
        except Exception as e:
            # Si ocurre un error al eliminar un libro, se muestra la traza
            print(f"Error al eliminar el libro: {e}")
            traceback.print_exc()

    def registrar_usuario(self, nombre, id_usuario):
        try:
            # Verificar si el ID ya está registrado
            if id_usuario not in [usuario.id_usuario for usuario in self.usuarios]:
                nuevo_usuario = Usuario(nombre, id_usuario)
                self.usuarios.add(nuevo_usuario)
                print(f"Usuario {nombre} registrado correctamente con ID {id_usuario}.")
            else:
                print(f"El ID {id_usuario} ya está registrado.")
        except Exception as e:
            # Si ocurre un error al registrar el usuario, se maneja
            print(f"Error al registrar el usuario: {e}")
            traceback.print_exc()

    def dar_baja_usuario(self, id_usuario):
        try:
            usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
            if usuario:
                self.usuarios.remove(usuario)
                print(f"Usuario {usuario.nombre} dado de baja.")
            else:
                print(f"No se encontró el usuario con ID {id_usuario}.")
        except Exception as e:
            # Si ocurre un error al dar de baja un usuario, se maneja
            print(f"Error al dar de baja el usuario: {e}")
            traceback.print_exc()

    def prestar_libro(self, isbn, id_usuario):
        try:
            libro = self.libros.get(isbn)
            usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)

            if libro and usuario:
                usuario.agregar_libro(libro)
                print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
            elif not libro:
                print(f"Libro con ISBN {isbn} no encontrado.")
            elif not usuario:
                print(f"Usuario con ID {id_usuario} no encontrado.")
        except Exception as e:
            # Si ocurre un error al prestar el libro, se maneja
            print(f"Error al prestar el libro: {e}")
            traceback.print_exc()

    def devolver_libro(self, isbn, id_usuario):
        try:
            usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)

            if usuario:
                libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
                if libro:
                    usuario.devolver_libro(libro)
                    print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
                else:
                    print(f"El libro con ISBN {isbn} no está prestado a {usuario.nombre}.")
            else:
                print(f"Usuario con ID {id_usuario} no encontrado.")
        except Exception as e:
            # Si ocurre un error al devolver el libro, se maneja
            print(f"Error al devolver el libro: {e}")
            traceback.print_exc()

    def buscar_libro(self, criterio, valor):
        try:
            resultado = []
            for libro in self.libros.values():
                if getattr(libro, criterio, "").lower() == valor.lower():
                    resultado.append(libro)
            return resultado
        except Exception as e:
            # Si ocurre un error al realizar la búsqueda, se maneja
            print(f"Error al buscar el libro: {e}")
            traceback.print_exc()

    def listar_libros_prestados(self):
        try:
            libros_prestados = []
            for usuario in self.usuarios:
                libros_prestados.extend(usuario.listar_libros())
            return libros_prestados
        except Exception as e:
            # Si ocurre un error al listar los libros prestados, se maneja
            print(f"Error al listar los libros prestados: {e}")
            traceback.print_exc()

