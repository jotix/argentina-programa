# Ejercicio 11:
# Los tramos impositivos para la declaración de la renta en un
# determinado país son mostrados en la tabla 1.
# 
# +-----------------------+-----------------+
# | Renta                 | Tipo Impositivo |
# |-----------------------+-----------------|
# | Menos de $10000       | 5 %             |
# | Entre $10000 y $20000 | 15 %            |
# | Entre $20000 y $35000 | 20 %            |
# | Entre $35000 y $60000 | 30 %            |
# | Más de $60000         | 45 %            |
# +-----------------------+-----------------+
# Cuadro 1: Tramos Impositivos
# 
# Escriba un programa que pregunte al usuario su renta anual y muestre
# por pantalla el tipo impositivo que le corresponde.

renta = float(input("ingrese su renta anual: "))

if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

print("El tipo impositivo que le corresponde es:", tipo, "%")
