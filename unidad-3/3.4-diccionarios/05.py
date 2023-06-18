"""
* Ejercicio 5:
Escriba un programa que:
1. Permita que el usuario ingrese un diccionario d.
2. Permita que el usuario ingrese una clave c.
3. Imprima por pantalla si la clave c está en el diccionario d.
"""

d = {}
while True:
  clave = input("Ingrese una clave, ingrese 'fin' para terminar: ")
  if clave == "fin":
    break
  elemento = input("Ingrese un elemento: ")
  d.update({clave : elemento})

c = input("Ingrese una clave para buscar: ")
print("La clave aparece en el diccionario:", c in d.keys())
