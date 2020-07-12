#!/usr/bin/python3
# coding = UTF-8


lista = [
    [6, 5],
    [3, 7],
    [2, 8]
]
# key = lambda 元素：元素【字段索引】
lista.sort(key=lambda y: y[0])
print(lista)
lista.sort(key=lambda y: y[1])
print(lista)