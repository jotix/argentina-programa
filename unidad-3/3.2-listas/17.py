# Ejercicio 17:
# Escriba un programa que:
# 1. Permita que el usuario ingrese una lista l.
# 2. Pida al usuario en elemento e.
# 3. Pida al usuario una posición p válida.
# 4. Inserte en la lista l el elemento e en la posición p.

s = input("Ingrese una lista, separe los elementos con comas: ")
l = list(s.split(","))
e = input("ingrese un elemento: ")
p = int(input("ingrese una posicion (la primara posicion es cero): "))
l.insert(p, e)
print("Resultado:", l)

