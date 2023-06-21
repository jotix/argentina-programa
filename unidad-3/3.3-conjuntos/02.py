# Ejercicio 2:
# Escriba un programa que:
# 1. Defina el conjunto universal U el cual está compuesto por los nú-
# meros del 1 al 20.
# 2. Pida al usuario dos conjuntos A y B.
# 3. Calcule la unión de A y B.
# 4. Calcule la intersección de A y B.
# 5. Calcule el complemento de las unión e intersección de A y B.
 
# punto 1
U = set(range(1,21))
print(U)
# punto 2
aux1 = input("Ingrese el conjunto A, separe los elementos con comas: ") 
aux2 = input("Ingrese el conjunto B, separe los elementos con comas: ") 
A = set(aux1.split(","))
B = set(aux2.split(","))
# punto 3
union = A | B
# punto 4
interseccion = A & B
# punto 5
comp_union_inter = union - interseccion
# imprimir resultados
print("Union A | B:", union)
print("Interseccion A & B:", interseccion)
print("Complemento de la union e interseccion:", comp_union_inter)
