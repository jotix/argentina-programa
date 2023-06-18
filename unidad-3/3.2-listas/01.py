"""
* Ejercicio 1:
Dada la siguiente lista l=[10,"hola",2.5,20,"que",3.5,30,"tal",4.5]
se pide recuperar:
1. el 30
2. "hola"
3. 10,"hola",2.5
4. Los strings
5. Los flotantes
6. Los enteros
"""

l = [10,"hola",2.5,20,"que",3.5,30,"tal",4.5]
print (l[6])
print (l[2])
print (l[:3])
strings = list(filter(lambda elemento: isinstance(elemento, str), l))
flotantes = list(filter(lambda elemento: isinstance(elemento, float), l))
enteros = list(filter(lambda elemento: isinstance(elemento, int), l))
print ("Los strings son:", strings)
print ("los flotantes son:", flotantes)
print ("los enteros son:", enteros)
