# Ejercicio 11:
# Escriba un programa que permita que el usuario ingrese por
# teclado una lista l. El programa debe crear dos listas la lista vocales y la
# lista consonante. En la lista vocales se encuentran todas la vocales que
# están en s y en la lista consonante todas las consonantes que están en
# s. Luego el programa debe imprimir por pantalla la cantidad de vocales
# y la cantidad de consonantes que tiene s.

todas_las_vocales = list("aeiou")
todas_las_consonantes = list("qwrtypsdfghjklñzxcvbnm")

vocales_ingresadas = []
consonantes_ingresadas = []

ingreso_flag = True
while ingreso_flag:
    s = input("Ingrese una letra (ingrese 0 para terminar): ")
    if s == "0":
        ingreso_flag = False    
    elif s in todas_las_consonantes:
        consonantes_ingresadas.append(s)
    elif s in todas_las_vocales:
        vocales_ingresadas.append(s)
    else:    
        print("Ese ingreso no cuenta, ingrese una LETRA!")

print(f"Vocales ingresadas: {vocales_ingresadas} / Total {len(vocales_ingresadas)}")
print(f"Consonantes ingresadas: {consonantes_ingresadas} / Total {len(consonantes_ingresadas)}")

