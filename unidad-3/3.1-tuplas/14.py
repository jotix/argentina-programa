"""
* Ejercicio 14:
Escriba un programa que permita que el usuario ingrese una
tupla t y un elemento e. El programa debe informar si e está en la tupla
t.
"""

aux = input("ingrese una tupla, separe los elementos con comas: ")
t = tuple(aux.split(","))
e = input("Ingrese un elemento a buscar: ")
print(f"El elemento {e} {'' if e in t else 'no '}esta en {t}")
