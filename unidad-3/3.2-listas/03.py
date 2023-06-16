"""
* Ejercicio 3:

Defina las listas l0 y l1 cada una con dos elementos numéricos
y luego construya la lista r cuyos elementos son la suma de los elemen-
tos de l0 y l1. Ejemplo: Si l0=[10,20] y l1=[8,20] la tupla r tiene que
contener r=[18,40].
"""

l0 = [10, 20]
l1 = [8, 20]
r = list(map(lambda n, m: n+m, l0, l1))
print(r)

