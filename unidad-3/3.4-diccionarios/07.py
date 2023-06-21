# Ejercicio 7:
# Escriba un programa que permita almacenar en un diccionario
# tres personas. Por cada persona se registra: el dni, nombre, domicilio y
# edad. Use como clave para el diccionario el dni.

d = {}

for i in range(3):
    dni = int(input("Ingrese su DNI: "))
    nombre = input("Ingrese su nombre: ")
    domicilio = input("Ingrese su domicilio: ")
    edad =  int(input("Ingrese su edad: "))
  
    d[dni] = [nombre, domicilio, edad]
  
print(d)
