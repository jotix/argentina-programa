# Ejercicio 10:
# Escriba un programa que permite que el usuario ingrese dos
# valores en las variables a y b y luego determinaa si dichos valores se
# encuentran almacenados como valor en el diccionario d. El diccionario
# d es ingresado por el usuario.

# Paso 1: Permitir que el usuario ingrese un diccionario
d = {}
num_pares = int(input("Ingrese el número de pares clave-valor: "))

for i in range(num_pares):
    clave = input("Ingrese una clave: ")
    valor = input("Ingrese un valor: ")
    d[clave] = valor

# Paso 2: Permitir que el usuario ingrese los valores a y b
a = input("Ingrese el valor a: ")
b = input("Ingrese el valor b: ")

# Paso 3: Verificar si los valores a y b están en el diccionario

if a in d.values():
    print("El valor a se encuentra en el diccionario.")
else:
    print("El valor a no se encuentra en el diccionario.")

if b in d.values():
    print("El valor b se encuentra en el diccionario.")
else:
    print("El valor b no se encuentra en el diccionario.")

