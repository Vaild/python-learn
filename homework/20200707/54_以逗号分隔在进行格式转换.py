#!/usr/bin/python3
# coding = UTF-8


string = '2.72, 5, 7, 3.14'
list1 = string.split(sep=', ')
print(list1)
for i in range(len(list1)):
    if list1[i].isnumeric():
        list1[i] = int(list1[i])
    else:
        list1[i] = float(list1[i])
print(list1)
