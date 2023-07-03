# Ejercicio 15:
# Escriba un programa que permita almacenar una lista de
# mercaderías. Los datos requeridos por cada mercadería son: nombre
# y precio. Dichos datos se almacenan en una tupla donde la primera
# componente es el nombre de la mercadería y la segunda componente
# es el precio. El programa debe permitir ingresar mercadería a la lista
# hasta que el usuario ingrese por teclado un *. Luego el programa debe
# imprimir por pantalla la lista de mercaderías ingresadas.

lista = []
ingreso_flag = True
while ingreso_flag:
    art = input("Ingrese el nombre del artículo: (ingrese * para terminar): ")
    if art == "*":
        ingreso_flag = False
    else:
        precio = float(input("Ingrese el precio: "))
        lista.append((art, precio))

linea = "+--------------------+------------+"
print(f"{linea}\n|     ARTÍCULO       |   PRECIO   |\n{linea}")
for merc in lista:
    print("| {:<18} | $ {:>8.2f} |".format(merc[0], merc[1]))

print(linea)
