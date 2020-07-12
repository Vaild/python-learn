#!/usr/bin/python3
# coding = UTF-8


lista = [3,0,8,5,7]
n = len(lista)
print(lista)
for i in range(n):
    if lista[i] > 5:
        lista[i] = 1
    else:
        lista[i] = 0
print(lista)