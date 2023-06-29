# Ejercicio 6:
# Escriba un programa que permita que el usuario ingrese el
# nombre de dos equipos y la cantidad de goles que han hecho en un
# partido. Luego el programa imprime el nombre del equipo ganador y
# bien el nombre de los dos equipos en caso de empate.

equipo1 = input("Ingrese el primer equipo y separado con una coma los goles: ").split(",")
equipo2 = input("Ingrese el segundo equipo y separado con una coma los goles: ").split(",")

goles1 = int(equipo1[1])
goles2 = int(equipo2[1])

if goles1 == goles2:
    print(equipo1[0], equipo2[0])

elif goles1 > goles2:
    print(equipo1[0])

else:
    print(equipo2[0])
