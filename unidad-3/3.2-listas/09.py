# Ejercicio 9:
# Construya un programa que permita que el usuario ingrese una
# lista de dos elementos y luego desempaquete la lista en dos variables a
# y b. Luego el programa debe imprimir las variables a y b.

s = input("Ingrese una lista de dos elementos separados por comas (ej. 1,2):")
lista = s.split(",")
a = lista[0]
b = lista[1]
print("El elemento a es:", a)
print("El elemento b es:", b)


