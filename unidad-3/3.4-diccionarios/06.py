# Ejercicio 6:
# Escriba un programa que permita que el usuario ingrese un dic-
# cionario. El programa debe imprimir una lista de tuplas donde en cada
# tupla tiene como primer elemento la clave y como segundo elemento el
# valor asociado a la clave.
 
d = {}
while True:
  clave = input("Ingrese una clave, ingrese 'fin' para terminar: ")
  if clave == "fin":
    break
  elemento = input("Ingrese un valor: ")
  d.update({clave : elemento})

print("Diccionario:", d)
lista = []
for elem in d:
    lista.append((elem,d[elem]))

print("Diccionario convertido en uns lista de tuplas:", lista)
