"""
* Ejercicio 3:
Escriba un programa que permita que el usuario ingrese una
lista de duplas ln. Cada dupla tiene como primer componente un nom-
bre y como segunda componente un número. Luego cree un diccionario
cuyas claves son los nombres en ln y cuyo valor sean enteros.
"""

lista=[]
for i in range(3):
    #lista.append([])
    n=str(input("Ingrese un nombre: "))
    v=int(input("Ingrese un numero: "))
    lista.append([n,v])
    #for j in range(1):
    #	n=str(input("Ingrese un nombre: "))
    #	v=int(input("Ingrese un numero: "))
    #	lista[i]+=n,v
print (lista)
d=dict(lista)
print(d)
