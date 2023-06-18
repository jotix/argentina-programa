"""
* Ejercicio 16:
Escriba un programa que permita que el usuario ingrese dos
tuplas t y r. El programa debe imprimir por pantalla la concatenación
de t y r.
"""

t_temp = input("Ingrese la tupla t, separe los elementos con comas: ")
r_temp = input("Ingrese la tupla r, separe los elementos con comas: ")
t = tuple(t_temp.split(","))
r = tuple(r_temp.split(","))
print("Tupla t:", t)
print("Tupla r:", r)
tupla_concatenada = t + r
print("Tuplas concatenadas:", tupla_concatenada)
