"""
* Ejercicio 11:
Escriba un programa que permita que el usuario ingrese un
número a y una tupla t. Luego el programa debe imprimir por pantalla
la posición del número a en la tupla t. En caso de que el número a no
se encuentre en t el programa debe imprimir -1.
"""

a = int(input("Ingrese un número entero: "))
aux = input("Ingrese una lista de enteros separados por comas: ")
t = tuple(map(lambda elem: int(elem), aux.split(",")))
print("El indice del elemento es:", t.index(a) if a in t else -1 ,"(-1 indica que no existe en la tupla)")
