# Ejercicio 1:
# Escriba un programa que permita que el usuario ingrese un
# número n. El programa debe imprimir los números pares comenzando
# desde 0 hasta n.

n = int(input("Ingrese un número entero: "))
for i in range(n):
    if not i & 1:
        print(i)

