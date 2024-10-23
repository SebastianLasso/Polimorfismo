# Clase base
class Vehiculo:
    def moverse(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")
    
    def detenerse(self):
        raise NotImplementedError("Este método debe ser sobrescrito en las clases hijas")

# Clase hija: Auto
class Auto(Vehiculo):
    def moverse(self):
        return "El auto está conduciendo por la carretera."
    
    def detenerse(self):
        return "El auto se ha detenido en el semáforo."

# Clase hija: Bicicleta
class Bicicleta(Vehiculo):
    def moverse(self):
        return "La bicicleta está pedaleando por el carril bici."
    
    def detenerse(self):
        return "La bicicleta se ha detenido al lado de la acera."

# Clase hija: Barco
class Barco(Vehiculo):
    def moverse(self):
        return "El barco está navegando por el océano."
    
    def detenerse(self):
        return "El barco ha anclado en el puerto."

# Clase hija: Avión
class Avion(Vehiculo):
    def moverse(self):
        return "El avión está volando por el cielo."
    
    def detenerse(self):
        return "El avión ha aterrizado en la pista."

# Ejemplo de uso
vehiculos = [Auto(), Bicicleta(), Barco(), Avion()]

for vehiculo in vehiculos:
    print(vehiculo.moverse())
    print(vehiculo.detenerse())
    print()
