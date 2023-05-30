# (IMC = peso (kg)/ [estatura (m)]2
peso = float(input("Ingrese el peso:"))
estatura = float(input("Ingrese la estatura (en metros):"))
imc = peso / (estatura ** 2)
print("el IMC de la persona es:", imc)
