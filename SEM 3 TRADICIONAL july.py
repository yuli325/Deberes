# Crear de las temperaturas
temperaturas = []

# Solicitar las temperaturas de los 7 días de la semana en Tena
for i in range(7):
    temp = float(input(f'Por favor, ingrese la temperatura del día {i + 1} en Tena (en grados Celsius): '))
    temperaturas.append(temp)

# Calcular el promedio de las temperaturas registradas
promedio = sum(temperaturas) / len(temperaturas)

# Imprimir el promedio de las temperaturas de la semana
print(f'El promedio de las temperaturas en Tena durante la semana es: {promedio:.2f}°C')
