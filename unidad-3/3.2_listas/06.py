"""
* Ejercicio 6:

Escriba un programa que almacene el valor de tres variables
ingresadas por el usuario en una lista.
"""

lista = []
for x in range(3):
  n = input ("ingrese un elemento para agregar a la lista: ")
  lista.append(n)

print(lista)
