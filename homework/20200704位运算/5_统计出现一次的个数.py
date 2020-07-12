#!/usr/bin/python3
# coding = UTF-8

# i = 3^5
# j = i^5
# print(j)

def Find_One(list):
    re = 0
    for i in list:
        re = re ^ i
    return re


list1 = [3, 4, 5, 7, 3, 4, 5,]
result = Find_One(list1)
print('唯一不重复的值是：', result)