# Ejercicio 7:
# Escriba un programa que:
# 1. Permita que el usuario ingrese cuatro números, los almacene una
# lista l.
# 2. Genere una lista s la cual se obtiene sumando a cada elemento de
# l un valor ingresado por el usuario.
# 3. Genere una lista r la cual se obtiene restando a cada elemento de
# l un valor ingresado por el usuario.
# 4. Imprima: con leyendas adecuadas la tupla l, s y r.

lista = []
for x in range(4):
  n = int(input ("ingrese un numero para agregar a la lista: "))
  lista.append(n)
  
print(lista)


