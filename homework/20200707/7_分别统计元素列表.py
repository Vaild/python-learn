#!/usr/bin/python3
# coding = UTF-8


lista = [True, False, 0, 1, 2]
print(len(lista))
for i in lista:
    print('{}在列表中有：{}个。'.format(i, lista.count(i)))