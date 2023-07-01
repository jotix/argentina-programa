# Ejercicio 14:
# Escriba un programa que permita que el usuario ingrese una
# lista de elementos. El programa debe informar la cantidad de números
# y strings que contiene la lista.

lista = []
ingreso_flag = True
while ingreso_flag:
    elem = input("Ingrese un número (ingrese fin para terminar): ")
    if elem == "fin":
        ingreso_flag = False
    else:
        lista.append(elem)

