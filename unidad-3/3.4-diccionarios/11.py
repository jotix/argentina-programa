# Ejercicio 11:
# Escriba un programa que permita que el usuario ingrese un
# número a y una tupla t. Luego el programa debe insertar en el diccio-
# nario d el par a,t.

a = int(input("Ingrese un numero: "))
t_aux = input("Ingrese una tupla, separe los elementos con comas: ")
t = tuple(t_aux.split(","))
print(f"Insertando el par {a} : {t} en un diccionario")
dicc = {a : t}
print(f"Diccionario resultado: {dicc}")

