#!/usr/bin/python3
# coding = UTF-8

def list_tuple(list1, list2):
    list = [(list1[i], list2[i]) for i in range(len(list1))]
    return list
dicta = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
dicta_keys = list(dicta.keys())
dicta_value = list(dicta.values())

list = list_tuple(dicta_keys, dicta_value)
print(list)
