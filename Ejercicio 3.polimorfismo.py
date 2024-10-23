class Punto3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        # Sobrecargar el operador de resta
        return Punto3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __repr__(self):
        # Representación legible del punto
        return f"Punto3D({self.x}, {self.y}, {self.z})"

# Pedir al usuario que ingrese los puntos para el primer punto 3D
x1 = float(input("Introduce el valor de x para el primer punto: "))
y1 = float(input("Introduce el valor de y para el primer punto: "))
z1 = float(input("Introduce el valor de z para el primer punto: "))

# Pedir al usuario que ingrese los puntos para el segundo punto 3D
x2 = float(input("Introduce el valor de x para el segundo punto: "))
y2 = float(input("Introduce el valor de y para el segundo punto: "))
z2 = float(input("Introduce el valor de z para el segundo punto: "))

# Crear los puntos 3D con los valores ingresados por el usuario
punto1 = Punto3D(x1, y1, z1)
punto2 = Punto3D(x2, y2, z2)

# Restar los dos puntos
resultado = punto1 - punto2

# Mostrar el resultado
print(f"La resta de los puntos es: {resultado}")
