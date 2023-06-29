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

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

disc = b * b - 4 * a * c

if disc == 0:
    mensaje = "tiene una"
elif disc > 0:
    mensaje = "tiene dos"
else:
    mensaje = "no tiene"

print("La ecuación", mensaje, "solución/es real/es.")
