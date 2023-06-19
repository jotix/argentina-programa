"""
* Ejercicio 7:
Defina una tupla y muestre:
1. Cómo se accede a un elemento de la tupla?
2. Qué sucede si se intenta acceder a una posición inexistente de la
tupla?
3. Cómo se calcula la longitud de una tupla?
"""

tupla = (1, 1, 2, 3, 5, 8, 13)
print("La tupla es:", tupla)
print("El 5to elemento de la lista es:", tupla[5])
print("La longitud de la lista es:", len(tupla))
try:
  print(tupla[10])
except Exception as e:
  print("Intentar acceder a una posición inexistente de la tupla da el error:", e)
