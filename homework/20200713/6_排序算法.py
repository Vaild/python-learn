#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import time
import random
class OwnSort:
    def __init__(self, count, range_var):
        self.list = []
        self.count = count
        for i in range(count):
            self.list.append(random.randint(0, range_var))

    def bubble_sort(self):
        i = 0
        while i < self.count:
            j = 0
            flag = True
            while j < self.count - 1:
                if self.list[j] > self.list[j + 1]:
                    self.list[j], self.list[j+1] = self.list[j+1], self.list[j]
                    flag = False
                j += 1
            if flag:
                break
            i += 1

    def select_sort(self):
        i = 0
        while i < self.count-1:
            j = i + 1
            min_index = i
            while j < self.count:
                if self.list[min_index] > self.list[j]:
                    min_index = j
                j += 1
            self.list[min_index], self.list[i] = self.list[i], self.list[min_index]
            i += 1

    def insert_sort(self):
        i = 0
        while i < self.count-1:
            j = i
            insert_value = self.list[j+1]
            while j >= 0:
                if insert_value < self.list[j]:
                    self.list[j+1] = self.list[j]
                else:
                    break
                j -= 1
            self.list[j+1] = insert_value
            i += 1

    def partition_left(self, low, hight):
        pivot = self.list[low]
        while low < hight:
            while low < hight and pivot <= self.list[hight]:
                hight -= 1
            self.list[low] = self.list[hight]
            while low < hight and pivot >= self.list[low]:
                low += 1
            self.list[hight] = self.list[low]
        self.list[low] = pivot
        return low

    def partition_right(self, low, hight):
        i = k = low
        # pivot = self.list[hight]
        while i < self.count:
            if self.list[hight] > self.list[i]:
                self.list[i], self.list[k] = self.list[k], self.list[i]
                i += 1
                k += 1
            else:
                i += 1
        self.list[hight], self.list[k] = self.list[k], self.list[hight]
        return k

    def quick_sort(self, low, hight):
        if low < hight:
            pivot = self.partition_right(low, hight)
            self.quick_sort(low, pivot-1)
            self.quick_sort(pivot+1, hight)

if __name__ == '__main__':
    x = OwnSort(100000, 100000)
    # print(x.list)
    start = time.time()
    # x.bubble_sort()
    # x.select_sort()
    # x.insert_sort()
    x.quick_sort(0, x.count-1)
    end = time.time()
    print(end - start)
    # print(x.list)
