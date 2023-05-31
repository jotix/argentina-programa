peso_payaso = 112
peso_munieca = 75
cantidad_payasos = int(input("Ingrese la cantidad de payasos:"))
cantidad_muniecas = int(input("Ingrese la cantidad de muñecas:"))
peso_total_en_kg = \
    (cantidad_payasos * peso_payaso + cantidad_muniecas * peso_munieca) / 1000
print("Peso total del pedido:", peso_total_en_kg, "kg.")
