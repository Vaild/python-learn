#!/usr/bin/python3
# coding=utf-8
from collections.abc import Iterator


class MyList():
    """自定义的一个可迭代对象"""

    def __init__(self):
        self.items = []

    def add(self, val):
        self.items.append(val)

    def __iter__(self):
        myiterator = MyIterator(self)
        return myiterator


# 迭代器
class MyIterator():
    """自定义的供上面可迭代对象使用的一个迭代器"""

    def __init__(self, mylist):
        self.mylist = mylist
        # current用来记录当前访问到的位置
        self.current = 0

    # 调用next方法时，其实就是执行__next__
    def __next__(self):
        if self.current < len(self.mylist.items):
            item = self.mylist.items[self.current]
            self.current += 2
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    mylist = MyList()
    # 不是迭代器
    print(isinstance(mylist, Iterator))
    mylist.add(1)
    mylist.add(2)
    mylist.add(3)
    mylist.add(4)
    mylist.add(5)
    # print(next(mylist)) #为啥不行
    for num in mylist:
        print(num)
    myIterator = MyIterator(mylist)
    print(isinstance(myIterator, Iterator))
    # print(next(myIterator))  # 打印结果是多少
    # for num in myIterator:
    #     print(num)
