cantidad_a_invertir = float(input("Ingrese la cantidad a invertir:"))
interes_anual = float(input("Ingrese el interes anual:"))
cantidad_de_anios = int(input("Ingrese los años:"))
capital_obtenido = cantidad_a_invertir * \
    (1 + (interes_anual/100 * cantidad_de_anios)
print("Capital obtenido:",  capital_obtenido)
