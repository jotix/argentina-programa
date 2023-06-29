# Ejercicio 9:
# Para tributar un determinado impuesto se debe ser mayor de
# 16 años y tener unos ingresos iguales o superiores a $1000 mensuales.
# Escriba un programa que pregunte al usuario su edad y sus ingresos
# mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Cuanto son sus ingresos: "))
print("Usted", "\b" if edad > 16 and ingresos > 1000 else "no", "tiene que tributar")
