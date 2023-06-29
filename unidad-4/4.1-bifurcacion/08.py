# Ejercicio 8:
# Escriba un programa que:
# 1. Almacene una contraseña en una variable.
# 2. Pregunte al usuario por la contraseña.
# 3. Imprima por pantalla si la contraseña introducida por el usuario
#    coincide con la guardada en la variable sin tener en cuenta
#    mayúsculas y minúsculas.

password = "1234"
ing_pass = input("Ingrese su contraseña: ")
print("Las contraseñas", "\b" if password == ing_pass else "NO", "coinciden.")
#+end_src
