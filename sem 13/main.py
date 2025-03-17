from tkinter import Tk
from gui_app import App

def main():
    # Crear una ventana principal
    root = Tk()
    root.title("Aplicación GUI Básica")

    # Crear la aplicación
    app = App(root)
    
    # Iniciar la aplicación
    root.mainloop()

if __name__ == "__main__":
    main()
