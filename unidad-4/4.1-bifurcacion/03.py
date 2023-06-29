# Ejercicio 3:
# Escriba un programa que muestre las siguientes opciones:
# 1. Calcular el perímetro de un triángulo.
# 2. Calcular el área de un triángulo.
# Luego dependiendo de la opción elegida por el usuario calcule el área
# o perímetro de un triángulo cuyos datos son también ingresados por el
# usuario.

opcion = int(input("Ingrese 1 para calcular el perímetro, ingrese 2 para calcular el área: "))

if opcion == 1:
    perimetro = sum([int(input("Ingrese lado: ")) for i in range (3)])
    print("El perímetro es:", perimetro)
else:
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura / 2
    print("El área del triángulo es:", area)
