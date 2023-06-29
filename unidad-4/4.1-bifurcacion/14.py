# Ejercicio 14:
# La pizzería Roma ofrece pizzas vegetarianas y no vegetarianas
# a sus clientes. Los ingredientes para cada tipo de pizza aparecen a
# continuación:
# 1. Ingredientes vegetarianos: Pimiento y tofu.
# 2. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escriba un programa que pregunte al usuario si quiere una pizza ve-
# getariana o no, y en función de su respuesta le muestre un menú con
# los ingredientes disponibles para que elija. Solo se puede elegir un
# ingrediente además de la mozzarella y el tomate que están en todas las
# pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
# vegetariana o no y todos los ingredientes que lleva.

menu = dict()
menu["vegetariano"]    = [ "Pimiento",   "Tofu" ]
menu["no vegetariano"] = [ "Peperoni",   "Jamón", "Salmón" ]
ingredientes  = [ "Mozzarella", "Tomate" ]

tipos_de_menu = list(menu.keys())
print(*[f"\n{i+1} - {tipos_de_menu[i]}" for i in range(len(tipos_de_menu)) ])
indice_menu_elegido = int(input("Seleccione el tipo de menú: ")) - 1

menu_elegido = menu[tipos_de_menu[indice_menu_elegido]]

print( *[ f"\n{i+1} - {menu_elegido[i]}" for i in range(len(menu_elegido)) ] )
indice_ingrediente = int(input("Elija ingrediente: ")) - 1

ingredientes.append(menu_elegido[indice_ingrediente])

print("\nLista de ingredientes:\n", *[f"- {i}\n" for i in ingredientes])
