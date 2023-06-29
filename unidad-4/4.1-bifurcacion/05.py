# Ejercicio 5:
# Escriba un programa que permita que el usuario ingrese dos
# valores numéricos. Luego el programa le pregunta al usuario si quiere
# sumar, restar dividir o multiplicar y dependiendo de la opción elegida
# el programa realiza la operación correspondiente.

operaciones = { "+" : (lambda a,b: a+b), "-" : (lambda a,b:a-b), "*" : (lambda a,b: a*b), "/" : (lambda a,b: a/b) }

x = float(input("Ingrese el valor de a: "))
y = float(input("Ingrese el valor de b: "))

ingreso_flag = True
while ingreso_flag:
    operacion = input("Operación a realizar (utilice + - * /): " )
    if operacion in operaciones.keys():
        ingreso_flag = False

print("Error" if operacion == "/" and y == 0 else f"Resultado {operaciones[operacion](x,y)}")

