#!/usr/bin/python3
# coding = UTF-8


list2 = [[1], ['a', 'b'], [2.3, 4.5, 6.7]]
list1 = [x for i in list2 for x in i]
print(list1)