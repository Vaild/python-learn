#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import time
import random
class OwnSort:
    def __init__(self, length, var_range):
        self.length = length
        self.list = []
        self.var_range = var_range
        for i in range(length):
            self.list.append(random.randint(0, var_range))

    # 快速排序
    def partition(self, low, high):
        i = k = low
        while i < high:
            if self.list[i] < self.list[high]:
                self.list[i], self.list[k] = self.list[k], self.list[i]
                i += 1
                k += 1
            else:
                i += 1
        self.list[k], self.list[high] = self.list[high], self.list[k]
        return k


    def quick_sort(self, low, high):
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot-1)
            self.quick_sort(pivot+1, high)

    # 归并排序
    def merge(self, low, mid, high):
        listp = self.list.copy()
        i = k = low
        j = mid + 1
        while i <= mid and j <= high:
            if listp[i] <= listp[j]:
                self.list[k] = listp[i]
                i += 1
            else:
                self.list[k] = listp[j]
                j += 1
            k += 1
        while i <= mid:
            self.list[k] = listp[i]
            k += 1
            i += 1
        while j <= high:
            self.list[k] = listp[j]
            k += 1
            j += 1

    def mergesort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.mergesort(low, mid-1)
            self.mergesort(mid+1, high)
            self.merge(low, mid, high)


    # 堆排序
    def  adjust_max_heap(self, adjust_pos, length):
        dad = adjust_pos
        son = 2 * dad + 1
        while son < length:
            if son + 1 < length and self.list[son] < self.list[son+1]:
                son = son + 1
            if self.list[dad] < self.list[son]:
                self.list[dad], self.list[son] = self.list[son], self.list[dad]
                dad = son
                son = 2 * dad + 1
            else:
                break


    def heapsort(self):
        # 建堆
        for i in range(self.length // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.length)
        # 对大根堆进行排序
        self.list[0], self.list[self.length-1] = self.list[self.length-1], self.list[0]
        for i in range(self.length - 1, 1, -1):
            self.adjust_max_heap(0, i)
            self.list[0], self.list[i - 1] = self.list[i - 1], self.list[0]
    # 计数排序
    def countsort(self):
        listp = [0] * (self.var_range+1)
        k = 0
        for num in self.list:
            listp[num] += 1  # 每次统计这个位置的数则加1
        # 对于整个辅助列表进行遍历
        for i in range(self.var_range+1):
            for j in range(listp[i]):
                self.list[k] = i
                k += 1




if __name__ == '__main__':
    x = OwnSort(10, 100)
    print(x.list)
    # start = time.time()
    # x.quick_sort(0, x.length-1)
    # x.heapsort()
    x.countsort()
    # x.mergesort(0, x.length-1)
    # end = time.time()
    # print(end - start)
    print(x.list)
