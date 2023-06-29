# Ejercicio 2:
# Escriba un programa que permita que el usuario ingrese un
# número n. El programa debe informar si el número es capicúa o no.

n = int(input("Ingrese un número entero: "))
print("El numero ingresado", "es" if str(n)[::-1] == str(n) else "no es", "capicúa.")
