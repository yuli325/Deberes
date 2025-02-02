class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False
    
    def marcar_completada(self):
        self.completada = True
        print(f"Tarea '{self.descripcion}' marcada como completada.")
    
    def mostrar_tarea(self):
        estado = "Completada" if self.completada else "Pendiente"
        print(f"{self.descripcion} - Estado: {estado}")

class ListaDeTareas:
    def __init__(self):
        self.tareas = []
    
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.descripcion}' agregada a la lista.")
    
    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            print("Lista de Tareas:")
            for tarea in self.tareas:
                tarea.mostrar_tarea()
    
    def mostrar_tareas_pendientes(self):
        pendientes = [tarea for tarea in self.tareas if not tarea.completada]
        if not pendientes:
            print("No hay tareas pendientes.")
        else:
            print("Tareas Pendientes:")
            for tarea in pendientes:
                tarea.mostrar_tarea()

# Crear lista de tareas
mi_lista = ListaDeTareas()

# Crear tareas
tarea_1 = Tarea("Comprar alimentos")
tarea_2 = Tarea("Lavar la ropa")
tarea_3 = Tarea("Estudiar programación")

# Agregar tareas a la lista
mi_lista.agregar_tarea(tarea_1)
mi_lista.agregar_tarea(tarea_2)
mi_lista.agregar_tarea(tarea_3)

# Mostrar todas las tareas
mi_lista.mostrar_tareas()

# Marcar una tarea como completada
tarea_1.marcar_completada()

# Mostrar solo las tareas pendientes
mi_lista.mostrar_tareas_pendientes()

# Mostrar todas las tareas nuevamente
mi_lista.mostrar_tareas()
