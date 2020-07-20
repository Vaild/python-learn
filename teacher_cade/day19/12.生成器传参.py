#!/usr/bin/python3
# coding=utf-8
def gen():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1


F = gen()
print(next(F))
F.send('hello')
