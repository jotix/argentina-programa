# Ejercicio 13:
# Escriba un programa que permita que el usuario ingrese una
# lista l de números. El programa debe informar si la lista l contiene más
# números positivos que negativos o más números negativos que positivos
# o contiene la misma cantidad de números positivos que negativos.

lista = []
ingreso_flag = True
while ingreso_flag:
    n = input("Ingrese un número (ingrese fin para terminar): ")
    if n == "fin":
        ingreso_flag = False
    else:
        lista.append(int(n))

negativos = len(list(filter(lambda n: n < 0, lista)))
positivos = len(list(filter(lambda n: n > 0, lista)))

if negativos == positivos:
    mensaje = "la misma cantidad de positivos y negativos"
elif negativos > positivos:
    mensaje = "mas negativos que positivos"
else:
    mensaje = "mas positivos que negativos"

print(f"La lista contiene {mensaje}")

