t = tuple(list([int(input("Ingrese elemento:")) for i in range(4)]))
elem_a_sumar = int(input("Ingrese elemento a sumar:"))
elem_a_restar =  int(input("Ingrese elemento a restar:"))
s = tuple(map(lambda elem: elem + elem_a_sumar, t))
r = tuple(map(lambda elem: elem - elem_a_restar, t))
print("original:", t)
print("elem a sumar:", elem_a_sumar)
print("elem a restar:", elem_a_restar)
print("tupla sumada:", s)
print("tupla restada:", r)
