#!/usr/bin/python3
# coding = UTF-8


def MinDist(list):
    if len(list) < 2:
        return None
    list1 = sorted(list)
    n = len(list1)
    mindist = abs(list1[n-1]-list1[0])
    for i in range(0, n-1):
        abs_now = abs(list1[i] - list1[i + 1])
        if abs_now < mindist:
            mindist = abs_now
        else:
            pass
    print('最小距离为：', mindist)

list2 = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
MinDist(list2)
