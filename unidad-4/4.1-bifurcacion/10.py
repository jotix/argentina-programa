'''
Ejercicio 10:
Los alumnos de un curso se han dividido en dos grupos A y
B de acuerdo al sexo y el nombre. El grupo A esta formado por las
mujeres con un nombre anterior a la M y los hombres con un nombre
posterior a la N y el grupo B por el resto. Escriba un programa que
pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde.'''

nombre = input("Ingrese el nombre: ")
sexo = input("Ingrese el sexo (m o f): ")
if (sexo == "f" and nombre < "m") or (sexo == "m" and nombre > "n"):
    grupo = "A"
else:
    grupo = "B"

print("Usted está en el grupo", grupo)
