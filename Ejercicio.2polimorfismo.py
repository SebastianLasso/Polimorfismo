class Animal:
 def sonido(self):
  return "El animal hace un momento"
 
class Loro(Animal):
 def sonido(self):
  return "El loro, habla"

class Leon(Animal):
    def sonido(self):
      return "El leon, ruge"
    
animales = [Loro(),Leon()]
for animal in animales:
  print(animal.sonido())

a = Leon()
print(a.sonido())

b = Loro()
print(b.sonido())

