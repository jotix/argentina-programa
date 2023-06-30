# Ejercicio 7:
# Escriba un programa que permita que el usuario ingrese por
# teclado un string s. El programa deberá contar la cantidad de vocales
# y consonantes que tiene s.

lista_vocales = list("aeiou")
lista_consonantes = list("qwrtypsdfghjklñzxcvbnm")
string = input("Ingrese un string: ")
lista_string = list(string)

vocales = map(lambda c: c in lista_vocales, string)
for char in lista_string:
    if 
