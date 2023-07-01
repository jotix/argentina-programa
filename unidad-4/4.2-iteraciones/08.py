# Ejercicio 8:
# Escriba un programa que permita comprobar si un string es un
# palíndromo. Para resolver este ejercicio no realice conversiones.

string = input("Ingrese un string: ")
print("La string ingresada", "es" if string == string[::-1] else "no es", "un palíndromo")
