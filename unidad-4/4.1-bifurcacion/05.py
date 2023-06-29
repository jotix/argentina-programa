# Ejercicio 5:
# Escriba un programa que permita que el usuario ingrese dos
# valores numéricos. Luego el programa le pregunta al usuario si quiere
# sumar, restar dividir o multiplicar y dependiendo de la opción elegida
# el programa realiza la operación correspondiente.

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
operacion = input("Ingrese la operación a realizar, utilice los símbolos + - * / : " )

error = False

if operacion == "+":
    resultado = a + b
elif operacion == "-":
    resultado = a - b
elif operacion == "*":
    resultado = a * b
elif operacion == "/" and b != 0:
    resultado = a / b
else:
    error = True

print("Operación no válida." if error else f"El resultado es: {resultado}")
