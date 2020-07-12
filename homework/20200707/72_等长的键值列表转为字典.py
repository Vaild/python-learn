#!/usr/bin/python3
# coding = UTF-8


def list_dict(list_key, list_value):
    n = len(list_key)
    dicta = {}
    for i in range(n):
        dicta[list_key[i]] = list_value[i]
    return dicta


if __name__ == '__main__':
    lista = ['a', 'b', 'c', 'd']
    listb = [1, 2, 3, 4]
    dictb = list_dict(lista, listb)
    print(dictb)