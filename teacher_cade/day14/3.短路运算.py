#!/usr/bin/python3
# coding=utf-8

import copy

# 短路运算
arr = [1, 2, 3, 4, 5, 6, 7]

print(0 and arr[4])

print(1 or arr[4])

# arr1 = copy.deepcopy(arr)
# print(arr is arr1)
# arr[0] = 10
# print(arr1[0])
arr1 = arr[0:7]
print(arr1)
arr1[0] = 100
print(arr)

for i in range(0):
    print('I am handsome')
