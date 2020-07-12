#!/usr/bin/python3
# coding = UTF-8


lista = [
    ['a', 1],
    ['b', 2]
]
tuplea = (
    ('x', 3),
    ('y', 4)
)
dicta = {}
dictb = {}
for i in lista:
    dicta[i[0]] = i[1]
print(dicta)

for i in tuplea:
    dictb[i[0]] = i[1]
print(dictb)