# Clase base (Padre)
class Padre:
    def __init__(self, dinero):
        self.__dinero = dinero  # Ahorros

    # (Encapsulación)
    def get_dinero(self):
        return self.__dinero

# Clase derivada (Hijo) que hereda de Padre
class Hijo(Padre):
    def __init__(self, dinero, extra):
        super().__init__(dinero)  # Llamada al constructor de la clase base
        self.extra = extra  # Atributo adicional del hijo

    # Sobrescritura del método: el hijo agrega su dinero extra
    def get_dinero(self):
        return super().get_dinero() + self.extra  # Polimorfismo: agrega extra

# Dar datos a padre e hijo
dinero_padre = float(input("Ingresa el dinero del padre: "))
dinero_extra_hijo = float(input("Ingresa el dinero extra del hijo: "))
padre = Padre(dinero_padre)
hijo = Hijo(dinero_padre, dinero_extra_hijo)

# Mostrar dinero del padre y del hijo
print("Dinero del padre:", padre.get_dinero())  # 1000
print("Dinero del hijo:", hijo.get_dinero())  # 1500
