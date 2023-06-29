# Ejercicio 7:
# Escriba un programa que pregunte al usuario su edad y muestre
# por pantalla si es mayor de edad o no. El programa también le debe
# solicitar al usuario la edad a partir de la cual se considera una persona
# mayor de edad.

mayoria = int(input("A partir de que edad (inclusive) se es mayor: "))
edad = int(input("Ingrese su edad: "))
print("Usted", "es" if edad >= mayoria else "no es", "mayor de edad.")
