# Ejercicio 14:
# Escriba un programa que permita que el usuario ingrese dos
# diccionarios a y b y a partir de ellos cree las siguientes vistas:
# 1. u el cual contiene la unión de la vista de claves de a con la vista
# de claves de b.
# 2. i el cual contiene la intersección de la vista de claves de a con la
# vista de claves de b.
# 3. d la cual contiene la diferencia entre la vista de claves de a con la
# vista de claves de b.
# 4. ds la cual contiene la diferencia simétrica de la visa de claves de a
# con la vista de claves de b.

lista = []
for i in range (2):
    print(f"Ingrese diccionario:")
    lista.append({})
    while True:
        clave = input("Ingrese clave, fin para terminar: ")
        if clave == "fin":
            break
        valor = input("Ingrese un valor: ")
        lista[i].update({ clave : valor })

dicc1 = lista[0]
dicc2 = lista[1]

u = dicc1.keys() | dicc2.keys()
i = dicc1.keys() & dicc2.keys()
d = dicc1.keys() - dicc2.keys()
ds = dicc1.keys() ^ dicc2.keys()
print("Union de las claves: ", u)
print("Interseccion de las claves:", i)
print("Diferencia de las claves:", d)
print("Diferencia simetrica de las claves:", ds)
