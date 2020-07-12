#!/usr/bin/python3
# coding = UTF-8
list1 = []
for i in range(1, 1001):
    list1 += [i]
list1 = list1 + [100]
sum1 = sum(list1)
sum2 = sum(range(1, 1001))
num = sum1 - sum2
print('重复的数字是：', num)