"""
Ejercicio 3:

Escriba un ejemplo que muestre que las tuplas son inmutables.
"""

lista = [1, 2]
print(id(lista))
lista.append(2)
print(id(lista))
tupla = (1, 2)
print(id(tupla))
tupla = (2, 4)
print(id(tupla))
