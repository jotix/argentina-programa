# Ejercicio 9:
# Escriba un programa que permita que el usuario ingrese n
# strings. El programa debe imprimir por pantalla el string de mayor
# longitud.

n = int(input("Cuantos strings va a ingresar? "))
lista = []
longitudes = []
for i in range(n):
    s = input("Ingrese un string: ")
    lista.append(s)
    longitudes.append(len(s))

print("EL string de mayor longitud es:", lista[longitudes.index(max(longitudes))])
