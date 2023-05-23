""""
EJERCICIO 15:

Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por pantalla el
capital obtenido en la inversión.
"""

cantidad_a_invertir = float(input("Ingrese la cantidad a invertir:"))
interes_anual = float(input("Ingrese el interes anual:"))
cantidad_de_anios = int(input("Ingrese los anios:"))

capital_obtenido = cantidad_a_invertir * ( (1 + (interes_anual/100)) ** cantidad_de_anios)

print("Capital obtenido:",  capital_obtenido)

