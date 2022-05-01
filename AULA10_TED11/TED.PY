import random

lista = []
for x in range(1, 11):
    lista_2 = []
    for y in range(1, 11):
        lista_2.append(random.randint(0, 100000))
        lista = lista_2
    print(lista)
