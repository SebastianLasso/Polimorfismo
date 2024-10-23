class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other ):
       return Vector(self.x + other. x, self.y + other. y)
  

    def __repr__(self):
       return f"Vector({self.x}, {self.y})"
    

# Solicitar los datos  de los vectores
x1 = float(input("Introduce el valor de x para el primer vector: "))
y1 = float(input("Introduce el valor de y para el primer vector: "))

x2 = float(input("Introduce el valor de x para el segundo vector: "))
y2 = float(input("Introduce el valor de y para el segundo vector: "))

v1 = Vector(x1, y1)
v2 = Vector(x2, y2)

v3 = v1 + v2

print(f"La suma de los vectores es: {v3}")
