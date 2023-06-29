# Ejercicio 4:
# Escriba un programa que permita determinar si una ecuación
# de segundo grado tiene:
# 1. Dos soluciones reales distintas. Una ecuación de segundo grado
#    tiene dos soluciones si el discriminante b2−4ac es mayor que cero.
# 2. Una única solución real. Una ecuación de segundo grado tiene dos
#    soluciones si el discriminante b2−4ac es igual que cero.
# 3. No tiene solución real. Una ecuación de segundo grado tiene dos
#    soluciones si el discriminante b2−4ac es menor que cero.
# Nota: Todos los valores requeridos por la ecuación son ingresados por
# el usuario.

a = float(input("Ingrese el coeficiente a de la ecuación: "))
b = float(input("Ingrese el coeficiente b de la ecuación: "))
c = float(input("Ingrese el coeficiente c de la ecuación: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
    print("La ecuación tiene dos soluciones reales distintas.")
elif discriminante == 0:
    print("La ecuación tiene una única solución real.")
else:
    print("La ecuación no tiene solución real.")
