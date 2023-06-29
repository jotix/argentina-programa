# Ejercicio 1:
# Escriba un programa que permita que el usuario ingrese un
# número el programa debe informar si el número ingresado es par o
# impar.

n = int(input("Ingrese un número entero: "))
print("El número ingresado es", "impar." if n & 1 else "par.")
