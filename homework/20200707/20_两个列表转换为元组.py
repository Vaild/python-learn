#!/usr/bin/python3
# coding = UTF-8

def list2tuple(list1, list2):
    list = [(list1[i], list2[i]) for i in range(len(list1))]
    return list
lista = ['x', 'y', 'z']
listb = [1, 2, 3]
# list = [(lista[i], listb[i]) for i in range(len(lista))]
list = list2tuple(lista, listb)
print(list)