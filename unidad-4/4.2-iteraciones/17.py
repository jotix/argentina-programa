# Ejercicio 17:
# Escriba un programa que defina un diccionario cuya clave es
# un número y cuyo valor es una lista de tuplas como la del ejercicio
# anterior. El programa debe crear un diccionario con tres pares clave:
# valor. El primero para el primer trimestre, el segundo para el segundo
# trimestre y el tercero para el tercer trimestre. Luego el programa debe
# informar el promedio general del alumno.

dicc = {}
tri = ["primer", "segundo", "tercer"]
for i in range(3):
    print(f"- Ingresando las notas para el {tri[i]} trimestre:")
    dicc[i+1] = []
    ingreso_flag = True
    while ingreso_flag:
        s = input("Ingrese la materia: (ingrese * para terminar): ")
        if s == "*":
            ingreso_flag = False
        else:
            n = float(input("Ingrese la nota: "))
            dicc[i+1].append((s, n))

suma = 0
contador = 0
for trimestre in dicc:
    for materia in dicc[trimestre]:
        suma += materia[1]
        contador += 1

promedio = suma / contador
print("El promedio del alumno es:", promedio)

