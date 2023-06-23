lista = [100, 200, 300, 400, 500, 600, 700]
index = lista.index(500)
lista.insert(index + 1, "alpha")
lista.insert(index + 2, "qux")
lista.insert(index + 3, "thud")
print(lista)