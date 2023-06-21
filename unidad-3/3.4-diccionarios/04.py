# Ejercicio 4:
# Escriba un programa que:
# 1. Permita que el usuario ingrese un diccionario d.
# 2. Permita que el usuario ingrese un elemento e.
# 3. Cuente cuántas veces aparece e en los valores de d.

d = {}
while True:
  clave = input("Ingrese una clave, ingrese 'fin' para terminar: ")
  if clave == "fin":
    break
  elemento = input("Ingrese un elemento: ")
  d.update({clave : elemento})

e = input("Ingrese un elemento para buscar: ")
print("El valor aparece en el diccionario:", e in d.values())
