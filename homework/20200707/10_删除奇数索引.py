#!/usr/bin/python3
# coding = UTF-8


lista = [0,1,2,3,4,5,6,7,8,9,10,11]
print(lista)
n = len(lista)
for i in range(1, n // 2 + 1):
    lista.pop(i)
print(lista)