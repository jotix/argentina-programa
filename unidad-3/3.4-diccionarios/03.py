# Ejercicio 3:
# Escriba un programa que permita que el usuario ingrese una
# lista de duplas ln. Cada dupla tiene como primer componente un nom-
# bre y como segunda componente un número. Luego cree un diccionario
# cuyas claves son los nombres en ln y cuyo valor sean enteros.

lista=[]
while True:
    nombre = input("Ingrese un nombre, ingrese fin para terminar: ")
    if nombre == "fin":
        break
    num = int(input("Ingrese un numero: "))
    lista.append([nombre, num])

print ("Lista ingresada", lista)
d = dict(lista)
print("Diccionario resultado:", d)

