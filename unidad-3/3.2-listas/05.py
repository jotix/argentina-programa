"""
* Ejercicio 5:

Escriba un programa que dada una lista t con 5 elementos y
un número n produzca como resultado una nueva lista con todos los
elementos de la lista t multiplicados por el número n.
"""

l = [ 1, 1, 2, 3, 5]
n = 3
nueval = []
nueval = list(map (lambda el:el*n, l))
print(nueval)

