# Ejercicio 3:
# Escriba un programa que muestre por pantalla la tabla de 
# multiplicar de un número n ingresado por el usuario.

n = int(input("Ingrese un número entero: "))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

