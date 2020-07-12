#!/usr/bin/python3
# coding = UTF-8


lista = [True,1,0,'x',None,'x',False,2,True]
print(lista)
n = lista.count('x')
for i in range(n):
    lista.remove('x')

print(lista)