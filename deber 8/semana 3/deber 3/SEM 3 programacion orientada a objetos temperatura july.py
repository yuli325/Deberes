class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []
# Método para ingresar_temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            self.temperaturas.append(float(input(f'Ingrese la temperatura del día {i + 1}: ')))
# Método para calcular promedio
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Instanciar la clase y ejecutar el proceso
clima = ClimaSemanal()
clima.ingresar_temperaturas()
print(f'La temperatura semanal del Tena es: {clima.calcular_promedio():.2f}°C')
