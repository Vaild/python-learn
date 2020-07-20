#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Search:
    def __init__(self):
        self.list = [2, 3, 5, 9, 13, 17, 20, 20, 22, 30, 33, 56, 78, 98, 99]

    def binary_search(self, value):
        low = 0
        high = len(self.list) - 1
        while low <= high:
            mid = (low + high) // 2
            if value == self.list[mid]:
                return mid
            elif value > self.list[mid]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            print('不存在')


if __name__ == '__main__':
    x = Search()
    print(x.binary_search(100))
