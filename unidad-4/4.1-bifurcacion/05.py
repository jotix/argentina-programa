# Ejercicio 5:
# Escriba un programa que permita que el usuario ingrese dos
# valores numéricos. Luego el programa le pregunta al usuario si quiere
# sumar, restar dividir o multiplicar y dependiendo de la opción elegida
# el programa realiza la operación correspondiente.

operaciones = { "+" : (lambda a,b: a+b), "-" : (lambda a,b:a-b), "*" : (lambda a,b: a*b), "/" : (lambda a,b: a/b) }

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

operacion = input("Operación a realizar (utilice + - * /): " )

print("Error" if operacion == 4 and b ==0 else f"Resultado {operaciones[operacion](a,b)}")

