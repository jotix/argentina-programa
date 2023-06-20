# Ejercicio 12:
# Escriba un programa que permita que el usuario ingrese un
# número a y una lista l. Luego el programa debe imprimir por pantalla
# la posición del número a en la lista l. En caso de que el número a no se
# encuentre en l el programa debe imprimir -1.

a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una lista de enteros separados por comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
print(lista.index(a) if a in lista else -1)


