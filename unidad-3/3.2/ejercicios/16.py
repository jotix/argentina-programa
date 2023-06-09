ingreso = input("Ingrese una lista, separe los elementos con comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
lista.sort()
menor = lista[0]
mayor = lista[len(lista)-1]
print("Lista ordenada:", lista)
print("Menor elemento:", menor)
print("Mayor elemento:", mayor)
