"""
* Ejercicio 13:
Escriba un programa que permita que el usuario ingrese un
número a y una tupla t. Luego el programa debe mostrar por pantalla
la cantidad de veces que aparece el número a en la tupla t.
"""

a = int(input("Ingrese un numero entero: "))
aux = input("ingrese una tupla, separe los elementos con comas: ")
t = tuple(map(lambda elem: int(elem), aux.split(",")))
repeticiones = t.count(a)
glue = "no aparece" if repeticiones == 0 else ("aparece 1 vez" if repeticiones == 1 else "aparece "+str(repeticiones)+" veces")
print("El elemento", a, glue, "en", t)
