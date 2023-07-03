# Ejercicio 14:
# Escriba un programa que permita que el usuario ingrese una
# lista de elementos. El programa debe informar la cantidad de números
# y strings que contiene la lista.

lista = []
ingreso_flag = True
while ingreso_flag:
    elem = input("Ingrese un número o una string (ingrese * para terminar): ")
    if elem == "*":
        ingreso_flag = False
    else:
        lista.append(elem)

numeros = []
strings = []
for i in range(len(lista)):
    if lista[i].replace('.','',1).replace('-','',1).isdigit():
        numeros.append(lista[i])
    else:
        strings.append(lista[i])

print(f"Números ingresados:\n{numeros} / TOTAL: {len(numeros)}")
print(f"Strings ingresadas:\n{strings} / TOTAL: {len(strings)}")
