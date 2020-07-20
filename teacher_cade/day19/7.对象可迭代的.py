#!/usr/bin/python3
# coding=utf-8
class MyList(object):

    def __init__(self):
        self.container = []

    def add(self, item):
        self.container.append(item)

    # 对象就是可迭代的
    def __iter__(self):
        return iter(self.container)


mylist = MyList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
for num in mylist:
    print(num)

from collections import Iterable

print(isinstance(mylist, Iterable))

from collections import Iterator

print(isinstance(mylist, Iterator))
print(isinstance([], Iterator))
