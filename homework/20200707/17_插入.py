#!/usr/bin/python3
# coding = UTF-8


lista = [1,4,7,2,5,8]
listb = ['x', 'y', 'z']
n = 3
print(lista)
for i in range(len(listb)):
    lista.insert(n, listb[i])
    n += 1
print(lista)