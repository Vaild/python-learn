#!/usr/bin/python3
# coding = UTF-8
# code by va1id



from collections.abc import Iterator, Iterable
import time
class Iterate():
    def __init__(self):
        self.list = []
        self.index = 0

    def add(self, var):
        self.list.append(var)

    def __next__(self):
        if self.index < len(self.list):
            res = self.list[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration


    def __iter__(self):
        return self


if __name__ == '__main__':
    a = Iterate()
    a.add(1)
    a.add(2)
    a.add(2)
    a.add(2)
    a.add(2)
    a.add(2)
    print(isinstance(a, Iterable))
    print(isinstance(a, Iterator))
    try:
        for i in a:
            print(i)
    except StopIteration:
        pass
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))
    # print(next(a))


