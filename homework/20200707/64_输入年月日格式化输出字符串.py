#!/usr/bin/python3
# coding = UTF-8


# 分割成列表之后再转换为元组进行格式化输出
string = input('输入现在的时间:')
lista = string.split()
print(lista)
lista = tuple(lista)
print('%s-%s-%s %s:%s:%s' % lista)