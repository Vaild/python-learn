#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import random
class BitMap:
    def __init__(self, length, var_range):
        self.bit = 0
        self.length = length
        self.list = []
        self.var_range = var_range
        for i in range(self.length):
            self.list.append(random.randint(0, var_range))

    def bitmap(self, var):
        if self.bit & (1 << var) == 0:
            self.bit = self.bit | (1 << var)
        else:
            pass


if __name__ == '__main__':
    # 实现去重
    rem = BitMap(1000, 10000)
    print(rem.list)
    # 设置一个容器将去重结果取出
    listres = []
    for i in rem.list:
        rem.bitmap(i)
    for i in range(rem.var_range):
        if 1 & rem.bit != 0:
            listres.append(i)
        rem.bit = rem.bit >> 1
    print(listres)