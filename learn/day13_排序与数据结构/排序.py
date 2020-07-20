#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import random
import time
class MySort:
    def __init__(self, count, range_num):
        self.count = count
        self.list = []
        for i in range(self.count):
            self.list.append(random.randint(0, range_num))

    def bublle(self):
        i = 0
        while i < self.count:
            j = 0
            flag = True
            while j < self.count-1:
                if self.list[j] > self.list[j+1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
                    flag = False
                j += 1
            if flag:
                break
            i += 1


    def select(self):
        i = 0
        while i < self.count-1:
            j = i+ 1
            min_index = i
            while j < self.count:
                if self.list[min_index] > self.list[j]:
                    min_index = j
                j += 1
            # 选到最小的之后进行交换
            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
            i += 1


    # def insert(self):



    def partition_left(self, left, right):
        list = self.list
        pivot = list[left]
        while left < right:
            while left < right and list[right] > pivot:
                right -= 1
            if left < right:
                list[left] = list[right]
            while left < right and list[left] < pivot:
                left += 1
            if left < right:
                list[right] = list[left]
        list[left] = pivot
        return left


    def partition_right(self, left, right):
        i = k = left
        while i < right:
            if self.list[i] < self.list[right]:
                self.list[i], self.list[k] = self.list[k], self.list[i]
                i += 1
                k += 1
            else:
                i += 1
        self.list[k], self.list[right] = self.list[right], self.list[k]
        return k


    def quicksort(self, left, right):
        if left < right:
            pivot = self.partition_right(left, right)
            self.quicksort(left, pivot-1)
            self.quicksort(pivot+1, right)


if __name__ == '__main__':
    x = MySort(100000, 100000)
    # print(x.list)
    start = time.time()
    # print(x.list)
    # x.select()
    x.quicksort(0, x.count-1)
    end = time.time()
    # print(x.list)
    print(end-start)
    # print(x.list)