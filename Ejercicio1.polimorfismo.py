a=int(input("Ingrese el primer numero entero: "))
b=int(input("Ingrese el segundo numero entero: "))

def multiplicar(a,b):
 return a * b

print(multiplicar("hola",1))
print(multiplicar("El resultado es:",1))
print(multiplicar(a,b))
print(multiplicar("Adios, fue un placer haverte ayudado",1))
print(multiplicar("Bye,  ",5))

#Utilice dos funciones la de multiplicar y la de sumar 

def sumar(num1, num2):
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        # Sumar números
        return num1 + num2
    elif isinstance(num1, list) and isinstance(num2, list):
        # Concatenar listas
        return num1 + num2
    elif isinstance(num1, str) and isinstance(num2, str):
        # Concatenar cadenas de texto
        return num1 + num2
    else:
        raise TypeError("Los tipos de objetos no son compatibles para la suma")

print(sumar(3, 5)) 
print(sumar([1, 2], [3, 4])) 
print(sumar("Hola ")) 
