# Función para convertir kilómetros a millas
def convertir_km_a_millas(kilometros):
    millas = kilometros * 0.621371  # 1 km = 0.621371 millas
    return millas

# Solicitar al usuario la distancia en kilómetros
km_input = input("Introduce la distancia en kilómetros: ")
kilometros = float(km_input)  # Convertir la entrada a float

# Convertir a millas
millas_convertidas = convertir_km_a_millas(kilometros)

# Mostrar el resultado
print(f"{kilometros} kilómetros son {millas_convertidas:.2f} millas.")
