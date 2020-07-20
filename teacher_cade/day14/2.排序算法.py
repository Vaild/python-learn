#!/usr/bin/python3
# coding=utf-8

import random
import time
import copy


class MySort:
    def __init__(self, count, val_range):
        self.arr = []
        self.count = count
        self.val_range = val_range
        for i in range(count):
            self.arr.append(random.randint(0, val_range))
        self.arr1 = [0] * count

    # 只把某个子树调整为大根堆
    def adjust_max_heap(self, adjust_pos, length):
        arr = self.arr
        dad = adjust_pos
        son = 2 * dad + 1
        while son < length:
            # 左孩子和右孩子谁大拿谁和父亲比较
            if son + 1 < length and arr[son] < arr[son + 1]:
                son = son + 1
            if arr[dad] < arr[son]:
                arr[dad], arr[son] = arr[son], arr[dad]
                dad = son
                son = son * 2 + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr
        # 把堆调整为大根堆
        for i in range(self.count // 2 - 1, -1, -1):
            self.adjust_max_heap(i, self.count)
        # 交换顶部元素和尾部元素
        arr[0], arr[self.count - 1] = arr[self.count - 1], arr[0]

        for len in range(self.count - 1, 1, -1):
            self.adjust_max_heap(0, len)
            arr[0], arr[len - 1] = arr[len - 1], arr[0]

    def merge(self, low, mid, high):
        arr = self.arr
        arr_t = self.arr1
        for i in range(low, high + 1):
            arr_t[i] = arr[i]
        i = low
        j = mid + 1
        k = low
        # 合并两个有序数组
        while i <= mid and j <= high:
            if arr_t[i] < arr_t[j]:
                arr[k] = arr_t[i]
                i += 1
            else:
                arr[k] = arr_t[j]
                j += 1
            k += 1

        while j <= high:
            arr[k] = arr_t[j]
            k += 1
            j += 1
        while i <= mid:
            arr[k] = arr_t[i]
            k += 1
            i += 1

    # 归并排序不限制是二路归并（也可以叫两两归并），
    # 还是多个归并，因为两两归并编写简单，同时面试官
    # 也不会要求编写其他数目的归并，所以大家掌握两两归并即可
    def merge_sort(self, low, high):
        # 递归分割
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)

    def count_sort(self):
        count_value_list = [0] * (self.val_range + 1)
        arr = self.arr
        # 统计每个值出现的次数
        for i in arr:
            count_value_list[i] += 1
        k = 0
        for i in range(self.val_range + 1):
            for j in range(count_value_list[i]):
                arr[k] = i
                k += 1


if __name__ == '__main__':
    s = MySort(10, 100)
    print(s.arr)
    start = time.time()
    # s.heap_sort()
    # s.merge_sort(0, 1000000 - 1)
    s.count_sort()
    end = time.time()
    print('use time %f' % (end - start))
    print(s.arr)
