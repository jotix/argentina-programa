# Ejercicio 16:
# Escriba un programa que permita registrar en una lista de tuplas
# las materias y las notas que un alumno obtuvo durante un trimestre.
# Luego el programa debe calcular el promedio general del trimestre
# ingresado.


lista = []
ingreso_flag = True
while ingreso_flag:
    materia = input("Ingrese la materia: (ingrese * para terminar): ")
    if materia == "*":
        ingreso_flag = False
    else:
        nota = float(input("Ingrese la nota: "))
        lista.append((materia, nota))

suma = 0
for elem in lista:
    suma += elem[1]

promedio = suma / len(lista)
print("El promedio del alumno es:", promedio)
