"""
* Ejercicio 11:

Escriba un programa que permita que el usuario ingrese un
número a y una lista l. Luego el programa debe imprimir True si el
número a está en l y False en otro caso.
"""

a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una lista de enteros, separe elementos con comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
print("El elemento", a, "esta en la lista", lista, "? ", a in lista)

