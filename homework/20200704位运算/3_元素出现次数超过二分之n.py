#!/usr/bin/python3
# coding = UTF-8
list2 = [3, 16, 16, 4, 16, 5, 16, 7,  16, 16, 19, 16, 20, 16, 23, 16, 25, 16, 30]
list1 = set(list2)
for i in list1:
    if list2.count(i) > len(list2) /2:
        print('个数大于本列表个数{}的1/2的是：{}'.format(len(list2), i))
        break
