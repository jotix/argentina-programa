# Ejercicio 8:
# Construya un programa que permita que el usuario ingrese una
# dupla y luego desempaquete la tupla en dos variables a y b. Luego el
# programa debe imprimir las variables a y b.

aux = input("ingrese un dupla, separe los elementos con una coma: ")
tupla = tuple(aux.split(","))
a = tupla[0]
b = tupla[1]
print("el elemento a de la tupla es:", a)
print("el elemento b de la tupla es:", b)
