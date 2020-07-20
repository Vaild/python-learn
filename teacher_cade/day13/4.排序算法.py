#!/usr/bin/python3
# coding=utf-8
# n = 10
# for i in range(n):
#     for j in range(n):
#         print(j, end=' ')
#
# for j in range(n):
#     print(j, end=' ')
import random
import time


class MySort:
    def __init__(self, count, val_range):
        self.arr = []
        self.count = count
        for i in range(count):
            self.arr.append(random.randint(0, val_range))

    def bubble(self):
        i = self.count - 1
        arr = self.arr
        while i > 0:
            j = 0
            flag = True
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = False
                j += 1
            if flag == True:
                break
            i -= 1

    def select(self):
        arr = self.arr
        i = 0
        j = 0
        while i < self.count - 1:
            min_pos = i
            j = i + 1
            while j < self.count:
                if arr[min_pos] > arr[j]:
                    min_pos = j
                j += 1
            # 交换
            arr[i], arr[min_pos] = arr[min_pos], arr[i]
            i += 1

    def insert(self):
        arr = self.arr
        for i in range(1, self.count):
            insert_val = arr[i]
            for j in range(i - 1, -1, -1):
                if insert_val < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
            if j == 0 and arr[j] > insert_val:
                j = -1
            arr[j + 1] = insert_val

    def insert_while(self):
        arr = self.arr
        i = 1
        while i < len(arr):
            j = i - 1
            insert_value = arr[i]
            while j >= 0:
                if insert_value < arr[j]:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = insert_value
            i += 1

    def partition(self, left, right):
        arr = self.arr
        i = k = left
        while i < right:
            if arr[i] < arr[right]:
                arr[i], arr[k] = arr[k], arr[i]
                i += 1
                k += 1
            else:
                i += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick_sort(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick_sort(left, pivot - 1)
            self.quick_sort(pivot + 1, right)


s = MySort(10000, 100000)
# print(s.arr)
start = time.time()
# s.bubble()
# s.select()
# s.insert()
s.insert_while()
# s.quick_sort(0, s.count - 1)
end = time.time()
print('use time %f' % (end - start))
# print(s.arr)
