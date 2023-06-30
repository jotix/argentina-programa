# Ejercicio 6:
# Escriba un programa que permita que el usuario ingrese 
# números por teclado hasta que ingrese un -1. Luego el programa debe
# informar la cantidad de números ingresados.

n = 0
contador = 0
while n != -1:
    n = int(input("ingrese un número (-1 para terminar): "))
    contador += 1

print(f"Usted ingreso {contador-1} números")
