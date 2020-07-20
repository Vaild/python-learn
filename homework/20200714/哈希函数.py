#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import time
class Hash:
    def __init__(self, length):
        self.hashlength = length
        self.hashmap = [None] * length

    def myhash(self, string):
        h = 0
        for i in string:
            h = (h << 4) + ord(i)
            g = h & 0xf0000000
            if g:
                h ^= g >> 24
            h &= ~g
        return  h % self.hashlength
    # 冲突处理

    def solve_col(self, hash, string):
        self.hashmap[hash].append(string)

    def hash_save(self, string):
        hash = self.myhash(string)
        if self.hashmap[hash] is None:
            self.hashmap[hash] = [[string, 1]]
        else:
            for list_son in self.hashmap[hash]:
                if string in list_son:
                   list_son[1] += 1
                   break
            else:
                self.hashmap[hash].append([string, 1])


if __name__ == '__main__':
    s = time.time()
    hashlist = Hash(100000)
    file = open('The_Holy_Bible.txt', mode='r')
    for sentence in file:
        for word in sentence.split():
            hashlist.hash_save(word)
    file.close()
    # 开始统计
    # 将保存的数组转换为二维数组，再进行排序
    lists = []
    for two_dimension in hashlist.hashmap:
        if two_dimension is not None:
            for dimension in two_dimension:
                lists.append(dimension)
    print(lists)
    lists = sorted(lists, key=lambda di:di[1])
    for i in range(-1, -11, -1):
        print(lists[i])
    e = time.time()
    print(e -s)

