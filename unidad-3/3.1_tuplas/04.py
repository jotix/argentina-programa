Ejercicio 4:

Escriba un programa que dada una tupla t con 5 elementos y
un número n produzca como resultado una nueva tupla con todos los
elementos de la tupla t multiplicados por el número n.


  t = (1, 1, 2, 3, 5)
  n = int(input("Ingrese un numero para multiplicar la tupla: "))
  nueva_t = tuple((map(lambda elem: elem * n, t)))
  print("tupla original", t)
  print("multiplicada por:", n)
  print("nueva tupla:", nueva_t)
