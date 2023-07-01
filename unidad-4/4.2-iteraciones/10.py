# Ejercicio 10
# Escriba un programa que permita que el usuario ingrese dos
# strings s0 y s1. El programa debe crear un nuevo string denominado
# merge el cual se forma a partir de s0 y s1 de la siguiente manera: primer
# carácter de s0, primer carácter de s1, segundo carácter de s0, segundo
# carácter de s1 y así siguiendo. Finalmente, el programa imprime s0, s1
# y r.

s0 = input("Ingrese un string: ")
s1 = input("Ingrese un string: ")
r = ""
for i in range(max([len(s0), len(s1)])):
    if i < len(s0):
        r += s0[i]
    if i < len(s1):
        r += s1[i]

print("String s0: ", s0)
print("String s1: ", s1)
print("String r:  ", r)
