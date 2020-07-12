#!/usr/bin/python3
# coding = UTF-8


lista = [3, 'a', 5.2, 4, {}, 9, []]
n = len(lista)
for i in range(n):
    if isinstance(lista[i], int) or isinstance(lista[i], float):
        if lista[i] > 3:
            lista[i] = 1
        else:
            lista[i] = 0
    else:
        lista[i] = 0
print(lista)