#!/usr/bin/python3
# coding = UTF-8
# code by va1id


def practice(lista, dicta):
    lista.reverse()
    dicta['qq'] = 88888888

if __name__ == '__main__':
    list = [1, 2, 3, 4]
    dict = {"name":'bob', "phone":'12345678'}
    print(list, '\n', dict)
    practice(list, dict)
    print(list, '\n', dict)