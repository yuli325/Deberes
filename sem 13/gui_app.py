from tkinter import Frame, Label, Button, Entry, Listbox, Scrollbar

class App:
    def __init__(self, master):
        self.master = master
        
        # Crear el marco de la aplicación
        self.frame = Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Crear el título de la aplicación
        self.title_label = Label(self.frame, text="Información de Mercado", font=("Arial", 14))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campo de texto para ingresar datos
        self.entry_label = Label(self.frame, text="Ingresar Información de compras del día:")
        self.entry_label.grid(row=1, column=0, padx=10, pady=5)

        self.entry = Entry(self.frame)
        self.entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón para agregar información
        self.add_button = Button(self.frame, text="Agregar", command=self.agregar_info)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Lista para mostrar la información
        self.listbox = Listbox(self.frame, height=10, width=40, selectmode="single")
        self.listbox.grid(row=3, column=0, columnspan=2, pady=5)

        # Agregar barra de desplazamiento a la lista
        self.scrollbar = Scrollbar(self.frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.grid(row=3, column=2, sticky="ns")
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Botón para limpiar la entrada de texto
        self.clear_button = Button(self.frame, text="Limpiar", command=self.limpiar_entrada)
        self.clear_button.grid(row=4, column=0, columnspan=2, pady=10)

    def agregar_info(self):
        """Agregar la información ingresada en la lista"""
        info = self.entry.get()
        if info != "":
            self.listbox.insert("end", info)
            self.entry.delete(0, "end")  # Limpiar el campo de texto

    def limpiar_entrada(self):
        """Limpiar el campo de texto y la lista"""
        self.entry.delete(0, "end")
        self.listbox.delete(0, "end")
