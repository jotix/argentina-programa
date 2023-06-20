# Ejercicio 10
# Escriba un programa que permite que el usuario ingrese un
# número a y una tupla t. Luego el programa debe imprimir True si el
# número a está en t y False en otro caso.

a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una tupla de enteros, separe elementos con comas: ")
tupla = tuple(list(map(lambda elem: int(elem), ingreso.split(","))))
print(a in tupla)

