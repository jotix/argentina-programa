# Ejercicio 12:
# Escriba un programa que permita que el usuario ingrese por
# teclado una lista de strings. El programa retorna como resultado la
# misma lista pero con los strings invertidos.

lista = []
ingreso_flag = True
while ingreso_flag:
    s = input("Ingrese un string (ingrese fin para terminar): ")
    if s == "fin":
        ingreso_flag = False
    else:
        lista.append(s)

lista_resultado = list(map(lambda string: string[::-1], lista))
print ("Lista resultado:", lista_resultado)

