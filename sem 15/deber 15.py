import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

class AplicacionTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x500")

        # Inicializar la lista de tareas vacía
        self.tareas = []

        # Crear el marco principal de la interfaz
        self.frame_principal = ttk.Frame(self.root, padding="10")
        self.frame_principal.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear la entrada para agregar nuevas tareas
        self.entrada_tarea = ttk.Entry(self.frame_principal, width=40)
        self.entrada_tarea.grid(row=0, column=0, columnspan=2, pady=5)
        self.entrada_tarea.bind('<Return>', self.crear_tarea)

        # Botón para añadir una nueva tarea
        self.btn_crear_tarea = ttk.Button(self.frame_principal, text="Añadir Tarea", command=self.crear_tarea)
        self.btn_crear_tarea.grid(row=0, column=2, padx=5, pady=5)

        # Crear el componente de lista para mostrar tareas
        self.lista = tk.Listbox(self.frame_principal, width=50, height=20)
        self.lista.grid(row=1, column=0, columnspan=3, pady=10)

        # Botón para marcar una tarea como completada
        self.btn_completado = ttk.Button(self.frame_principal, text="Completar Tarea", command=self.marcar_realizada)
        self.btn_completado.grid(row=2, column=0, padx=5, pady=5)

        # Botón para eliminar la tarea seleccionada
        self.btn_eliminar = ttk.Button(self.frame_principal, text="Eliminar Tarea", command=self.borrar_tarea)
        self.btn_eliminar.grid(row=2, column=2, padx=5, pady=5)

    def crear_tarea(self, event=None):
        # Obtener el texto de la tarea desde la entrada
        tarea = self.entrada_tarea.get().strip()
        if tarea:
            # Añadir la tarea a la lista de tareas
            self.tareas.append({"texto": tarea, "Completada": False})
            # Insertar la tarea en la lista visual
            self.lista.insert(tk.END, tarea)
            # Limpiar el campo de entrada
            self.entrada_tarea.delete(0, tk.END)

    def marcar_realizada(self):
        # Verificar si hay una tarea seleccionada
        seleccion = self.lista.curselection()
        if seleccion:
            idx = seleccion[0]
            # Cambiar el estado de la tarea a realizada
            self.tareas[idx]["Completada"] = not self.tareas[idx]["Completada"]
            self.refrescar_lista()

    def refrescar_lista(self):
        # Limpiar la lista visual antes de actualizar
        self.lista.delete(0, tk.END)
        for tarea in self.tareas:
            texto = tarea["texto"]
            # Añadir un símbolo de verificación si está completada
            if tarea["Completada"]:
                texto = "✔ " + texto
            self.lista.insert(tk.END, texto)

    def borrar_tarea(self):
        # Verificar si hay una tarea seleccionada
        seleccion = self.lista.curselection()
        if seleccion:
            idx = seleccion[0]
            # Remover la tarea de la lista interna
            del self.tareas[idx]
            self.refrescar_lista()

# Inicializar la aplicación
root = tk.Tk()
app = AplicacionTareas(root)
root.mainloop()
