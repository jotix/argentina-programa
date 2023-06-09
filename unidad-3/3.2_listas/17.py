"""
Escriba un programa que:
1. Permita que el usuario ingrese una lista l.
2. Pida al usuario en elemento e.
3. Pida al usuario una posición p válida.
4. Inserte en la lista l el elemento e en la posición p.
"""

s = input("Ingrese una lista, separe los elementos con comas: ")
l = s.split(",")
e = input("ingrese un elemento:")
p = input("ingrese una posicion (la primera posicion es cero)")
nueva_l = l.insert(p, e)
print("La nueva lista es:", nueva_l)
