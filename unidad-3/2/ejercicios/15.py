l = [34, 3.2, "Juan", "Pedro", -2]
print("La lista inicial es (se muesta todo en string):", l)
agregado = input("Ingrese un elemento para agregar a la lista: ")
l.append(agregado)
aux = input("Ingrese un elemento para contar las apariciones en la lista: ")
elem_a_contar = float(aux) if agregado.isnumeric() else aux
veces = l.count(elem_a_contar)
print(elem_a_contar, "aparece", veces, "vez" if veces == 1 else "veces", l)
s = input("Ingrese una lista para agregar a la anterior, separe los elementos con comas: ")
nuevalista = l + list(s.split(","))
nuevalista.reverse()
print("Nueva lista invertida:", nuevalista)
