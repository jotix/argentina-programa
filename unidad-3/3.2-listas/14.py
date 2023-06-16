"""
* Ejercicio 14:

Escriba un programa que permita que el usuario ingrese un
número a y una lista l. Luego el programa debe mostrar por pantalla
la cantidad de veces que aparece el número a en la lista l.
"""

a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una lista de enteros separados por comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
veces = lista.count(a)
print(a, "no aparece en" if veces == 0 else ("aparece", veces, "vez" if veces == 1 else "veces en"), lista)

