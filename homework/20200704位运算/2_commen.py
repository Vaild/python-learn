#!/usr/bin/python3
# coding = UTF-8
# list1 = [1, 2, 3, 5, 7, 14, 16, 18, 19]
# list2 = [3, 4, 5, 7, 16, 19, 20, 23, 25, 30]
# if len(list1) <= len(list2):
#     short = list1
#     long = list2
# else:
#     short = list2
#     long = list1
# if short[len(short)-1] < long[0] or short[0] > long[len(long)-1]:
#     print('none')
# else:
#     for i in range(0,len(short)):

list1 = [1, 2, 3, 5, 7, 14, 16, 18, 19]
list2 = [3, 4, 5, 7, 16, 19, 20, 23, 25, 30]
list3 = []
for i in list1:
    if i in list2:
        list3 = list3 + [i]
print(list3)