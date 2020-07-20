#!/usr/bin/python3
# coding=utf-8

from collections.abc import Iterator


class MyIterator():
    """自定义的供上面可迭代对象使用的一个迭代器"""

    def __init__(self):
        self.mylist = []
        # current用来记录当前访问到的位置
        self.current = 0

    def add(self, val):
        self.mylist.append(val)

    # 调用next方法时，其实就是执行__next__
    def __next__(self):
        if self.current < len(self.mylist):
            item = self.mylist[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    myIterator = MyIterator()
    myIterator.add(1)
    myIterator.add(2)
    myIterator.add(3)
    myIterator.add(4)
    myIterator.add(5)
    print(isinstance(myIterator, Iterator))
    # print(next(myIterator))  # 打印结果是多少
    # for num in myIterator:
    #     print(num)
    next(myIterator)
