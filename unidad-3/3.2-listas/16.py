# Ejercicio 16:
# Construya un programa que:
# 1. Permita que el usuario ingrese una lista l de números enteros l.
# 2. Ordene la lista
# 3. Almacene en la variable mayor el mayor elemento de la lista
# 4. Almacene en la variable menor el menor elemento de la lista.
# 5. Imprima por pantalla la lista l y el elemento mayor y el elemento
# menor.

ingreso = input("Ingrese una lista, separe los elementos con comas: ")
lista = list(map(lambda elem: int(elem), ingreso.split(",")))
lista.sort()
menor = lista[0]
mayor = lista[len(lista)-1]
print("Lista ordenada:", lista)
print("Menor elemento:", menor)
print("Mayor elemento:", mayor)

