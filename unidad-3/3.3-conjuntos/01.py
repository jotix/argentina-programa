# Ejercicio 1:
# Escriba un programa que:
# 1. Defina el conjunto universal el cual contiene las provincias de Ar-
# gentina.
# 2. Pida al usuario una provincia.
# 3. Calcule el complemento del conjunto single que contiene la pro-
# vincia ingresada por el usuario.

provincias = {"Buenos Aires", "CABA", "Catamarca", "Chaco", "Chubit", 
              "Cordoba", "Corrientes", "Entre Rios", "Formosa", "Jujuy",
              "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquen",
              "Rio Negro", "Salta", "San Juan", "San Luis", "Santa Cruz",
              "Santiago del Estero", "Tierra del Fuego", "Tucuman"}

prov = input("Ingrese una provincia: ")
complemento = provincias - {prov,}
print("Complemento:", complemento)