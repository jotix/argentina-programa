# Ejercicio 7:
# Escriba un programa que permita que el usuario ingrese por
# teclado un string s. El programa deberá contar la cantidad de vocales
# y consonantes que tiene s.

lista_vocales = list("aeiou")
lista_consonantes = list("qwrtypsdfghjklñzxcvbnm")

string = input("Ingrese un string: ")
lista_string = list(string)

vocales = list(filter(lambda char: char in lista_vocales, string))
consonantes = list(filter(lambda char: char in lista_consonantes, string))

print("Cantidad de vocales:", len(vocales))
print("Cantidad de consonantes:", len(consonantes))
