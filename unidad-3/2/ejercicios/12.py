a = int(input("Ingrese un número entero: "))
ingreso = input("Ingrese una lista de enteros separados por comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
print(lista.index(a) if a in lista else -1)
