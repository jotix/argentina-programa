# Ejercicio 6:
# Dado el siguiente programa:

def coordenadaZ (x, y) :
    x = x + 10
    y = y + 15
    return x + y

#programa principal
x = int (input("Coordenada eje x : "))
y = int (input("Coordenada eje y : "))
for i in range (3) :
    z = coordenadaZ(x, y)
    x = x + 1
    y = y + 1
    print (x, " . ", y, " . ", z )

# Se pide:
# 1. De un ejemplo de ejecución del programa.
# 2. Diga que hace el programa.
