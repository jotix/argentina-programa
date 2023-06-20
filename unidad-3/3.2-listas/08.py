# Ejercicio 8:
# Cree una lista y muestre:
# 1. El acceso a un elemento de la lista.
# 2. Qué sucede si se intenta acceder a una posición inexistente de la
# lista.
# 3. Cómo se calcula la longitud de una lista.

lista = [1, 1, 2, 3, 5, 8, 13]
print("La lista es:", lista)
print("El 5to elemento de la lista es:", lista[5])
print("La longitud de la lista es:", len(lista))
try:
  print(lista[10])
except Exception as e:
  print("Intentar acceder a una posición inexistente de la lista da el error:", e)


