#!/usr/bin/python3
# coding=utf-8

class HashStr:
    def __init__(self, hash_length):
        self.hash_length = hash_length
        self.hashmap = [None] * hash_length

    def elf_hash(self, str):
        h = g = 0
        for i in str:
            h = (h << 4) + ord(i)
            g = h & 0xf0000000
            if g:
                h ^= g >> 24
            h &= ~g

        return h % self.hash_length


if __name__ == '__main__':
    arr = ["hello", "world", 'mahuateng', 'henyouqian', 'xiongda']
    hash_execise = HashStr(100)
    for i in arr:
        hash_execise.hashmap[hash_execise.elf_hash(i)] = [[i, 0]]
    pass
