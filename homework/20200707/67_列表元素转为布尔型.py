#!/usr/bin/python3
# coding = UTF-8


lista = [0, 1, 2, 3.14, 'x', None, '', list(), {5}]
n = len(lista)
for i in range(n):
    lista[i] = bool(lista[i])
print(lista)