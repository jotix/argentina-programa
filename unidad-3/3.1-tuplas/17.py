# Ejercicio 17:
# Escriba un programa que:
# 1. Permita que el usuario ingrese una tupla t de cinco números.
# 2. Sume los números pares.
# 3. Sume los números impares.

tupla = tuple(list([int(input("Ingrese elemento: ")) for i in range(5)]))
impares = list(filter(lambda el: el & 1, tupla))
pares = list(filter(lambda el: not el & 1, tupla))
print("Impares:", impares, "suma", sum(impares))
print("pares:", pares, "suma", sum(pares))
