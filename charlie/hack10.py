#HACK-10 
#agregar después del item 500
#los alias qux y thud
#[100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]
lista = [100, 200, 300, 400, 500, 600, 700]
lista.insert(lista.index(500) + 1, "qux")
lista.insert(lista.index(500) + 2, "thud")
print(lista)