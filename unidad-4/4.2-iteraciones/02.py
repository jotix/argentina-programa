# Ejercicio 2:
# Escriba un programa que imprima por pantalla la suma de los
# n primeros números naturales.

n = int(input("Ingrese un número entero: "))
suma = 0
for i in range(1,n+1):
    suma += i

print(f"La suma de los primeros {n} números naturales es {suma}")

