a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una lista de enteros, separe elementos con comas: ")
lista = map(lambda elem: int(elem), ingreso.split(","))
print(a in lista)
