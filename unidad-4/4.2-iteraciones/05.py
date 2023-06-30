# Ejercicio 5:
# Escriba un programa que permita que el usuario ingrese n 
# números por teclado. El programa debe imprimir el mayor y
# menor número ingresado.

n = int(input("Cuantos números va a ingresar? "))
lista = []
for i in range(n):
    lista.append(int(input(f"Ingrese un número:")))

print(f"El menor número ingresado es: {min(lista)}")
print(f"El mayor número ingresado es: {max(lista)}")

