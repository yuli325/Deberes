
class Usuario:
    def __init__(self, nombre, id_usuario):
        try:
            self.nombre = nombre
            self.id_usuario = id_usuario
            self.libros_prestados = []  # Lista para almacenar los libros que tiene prestados
        except Exception as e:
            # Si hay un error al crear el usuario, se maneja y se imprime el error
            import traceback
            print(f"Error al crear el usuario: {e}")
            traceback.print_exc()

    def agregar_libro(self, libro):
        try:
            self.libros_prestados.append(libro)
        except Exception as e:
            # Si ocurre un error al agregar un libro, se captura y muestra
            import traceback
            print(f"Error al agregar el libro: {e}")
            traceback.print_exc()

    def devolver_libro(self, libro):
        try:
            if libro in self.libros_prestados:
                self.libros_prestados.remove(libro)
            else:
                print(f"El libro '{libro.titulo}' no está en los libros prestados.")
        except Exception as e:
            # Si ocurre un error al devolver un libro, se maneja
            import traceback
            print(f"Error al devolver el libro: {e}")
            traceback.print_exc()

    def listar_libros(self):
        return self.libros_prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    def __repr__(self):
        return self.__str__()