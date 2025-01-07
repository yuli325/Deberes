class Metodo80_20:
    def __init__(self):
        self.actividades = []  # Lista para almacenar todas las actividades
        self.calificaciones = []  # Lista para almacenar las calificaciones de cada actividad
        self.actividades_prioritarias = []  # Lista para las actividades del 20% más prioritarias

    # Método para ingresar actividades
    def ingresar_actividades(self):
        while True:
            actividad = input('Ingrese una actividad para el día (o "parar" para terminar): ')
            if actividad.lower() == 'parar':
                break
            self.actividades.append(actividad)

    # Método para calificar las actividades
    def calificar_actividades(self):
        for actividad in self.actividades:
            while True:
                try:
                    calificacion = int(input(f'Califique la actividad "{actividad}" del 1 al 10 (siendo 10 la más importante): '))
                    if 1 <= calificacion <= 10:
                        self.calificaciones.append(calificacion)
                        break
                    else:
                        print("Por favor, ingrese un número entre 1 y 10.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    # Método para organizar las actividades según la calificación
    def organizar_actividades(self):
        # Emparejar actividades con sus calificaciones
        actividades_calificadas = list(zip(self.actividades, self.calificaciones))
        # Ordenar actividades de mayor a menor según la calificación
        actividades_calificadas.sort(key=lambda x: x[1], reverse=True)
        
        # Calcular el 20% de las actividades
        total_actividades = len(actividades_calificadas)
        num_prioritarias = int(total_actividades * 0.2)
        
        # Tomar el 20% de las actividades más importantes
        self.actividades_prioritarias = [actividad for actividad, _ in actividades_calificadas[:num_prioritarias]]

    # Método para mostrar la lista completa de actividades
    def mostrar_lista_completa(self):
        print("\nLista completa de actividades para el día:")
        for actividad, calificacion in zip(self.actividades, self.calificaciones):
            if calificacion == 10:
                print(f"** {actividad} ** (Prioritaria - Calificada como 10)")
            elif actividad in self.actividades_prioritarias:
                print(f"** {actividad} ** (Prioritaria)")
            else:
                print(f"- {actividad}")

# Crear una instancia de la clase Metodo80_20
metodo = Metodo80_20()

# Ingresar actividades para el día
metodo.ingresar_actividades()

# Calificar las actividades según su importancia
metodo.calificar_actividades()

# Organizar las actividades y mostrar las prioridades
metodo.organizar_actividades()

# Mostrar la lista completa de actividades, destacando las prioritarias y calificadas con 10
metodo.mostrar_lista_completa()
