dinero = float(input("Ingrese la cantidad de dinero:"))
porcentaje = float(input("Ingrese el porcentaje:"))
resultado = dinero * porcentaje / 100
print("El", porcentaje, "%", "de", dinero, "es:", round(resultado, 2))
