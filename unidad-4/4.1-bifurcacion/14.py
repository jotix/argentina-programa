'''Ejercicio 14:
La pizzería Roma ofrece pizzas vegetarianas y no vegetarianas
a sus clientes. Los ingredientes para cada tipo de pizza aparecen a
continuación:
1. Ingredientes vegetarianos: Pimiento y tofu.
2. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escriba un programa que pregunte al usuario si quiere una pizza ve-
getariana o no, y en función de su respuesta le muestre un menú con
los ingredientes disponibles para que elija. Solo se puede elegir un
ingrediente además de la mozzarella y el tomate que están en todas las
pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.'''

import sys 

# cre un diccionario con tres listas para los ingredientes
menu = dict()
menu["base"]  = [ "Mozzarella", "Tomate" ]
menu["veg"]   = [ "Pimiento",   "Tofu" ]
menu["noveg"] = [ "Peperoni",   "Jamón", "Salmón" ]

eleccion = input("Quiere una pizza vegetariana? (s/n): ")
tipo = "veg" if eleccion == "s" else "noveg"

print( *[ f"{i+1} - {menu[tipo][i]}\n" for i in range(len(menu[tipo])) ] )

ingrediente = int(input("Elija ingrediente: ")) - 1

pizza = menu["base"]
pizza.append(menu[tipo][ingrediente])

print("Ingredientes:\n", *[f"- {i}\n" for i in pizza])
