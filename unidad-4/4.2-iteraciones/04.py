# Ejercicio 4:
# Escriba un programa que permita que el usuario ingrese dos
# números n y m. El programa debe imprimir por pantalla los números
# entre 0 y m que son divisibles por n.

n = int(input("Ingrese un número entero n: "))
m = int(input("Ingrese un número entero m: "))
for i in range(1,m+1):
    if i % n == 0:
        print(i)

