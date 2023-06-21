# Ejercicio 9:
# Defina un diccionario y muestre:
# 1. Cómo se accede a un elemento de un diccionario
# 2. Qué sucede si se intenta acceder al diccionario con una clave in-
# existente.
# 3. ¿Cómo se calcula la longitud de un diccionario?

dicc = { 1 : "azul", 2 : "rojo", 3 : "naranja"}
print("Un elemento del diccionario:", dicc[2])
print("Longitud del diccionario:", len(dicc))
try:
    dicc[4]
except Exception as e:
    print("Acceder a un elemento inexistente de un diccionario da el siguiente error:")
    print(e)
