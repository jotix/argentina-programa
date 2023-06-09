"""
* Ejercicio 15:

Dada la lista l=[34, 3.2, Juan, Pedro,-2] se pide:
1. Agregue al final de l un string ingresado por el usuario.
2. Solicite al usuario un elemento y cuente la cantidad de veces que
aparece dicho elemento en l.
3. Pida al usuario una lista s e incorporela al final de l.
4. Invierta la lista l.
"""

l = [34, 3.2, "Juan", "Pedro", -2]
print("La lista inicial es (se muesta todo en string):", l)
agregado = input("Ingrese un elemento para agregar a la lista: ")
l.append(agregado)
elem_a_contar = input("Ingrese un elemento para contar las apariciones en la lista: ")
veces = l.count(eval(elem_a_contar))
print(elem_a_contar, "aparece", veces, "vez" if veces == 1 else "veces", l)
s = input("Ingrese una lista para agregar a la anterior, separe los elementos con comas: ")
nuevalista = l + list(s.split(","))
nuevalista.reverse()
print("Nueva lista invertida:", nuevalista)
