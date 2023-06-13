"""
* Ejercicio 6:

Escriba un programa que:
1. Permita que el usuario ingrese cuatro números, los almacene una
tupla t.
2. Genere una tupla s la cual se obtiene sumando a cada elemento
de t un valor ingresado por el usuario.
3. Genere una tupla r la cual se obtiene restando a cada elemento de
t un valor ingresado por el usuario.
4. Imprima: con leyendas adecuadas la tupla t, s y r.
"""

t = tuple(list([int(input("Ingrese elemento: ")) for i in range(4)]))
elem_a_sumar = int(input("Ingrese elemento a sumar: "))
elem_a_restar = int(input("Ingrese elemento a restar: "))
s = tuple(map(lambda elem: elem + elem_a_sumar, t))
r = tuple(map(lambda elem: elem - elem_a_restar, t))
print("original:", t)
print("elem a sumar:", elem_a_sumar)
print("elem a restar:", elem_a_restar)
print("tupla sumada:", s)
print("tupla restada:", r)
