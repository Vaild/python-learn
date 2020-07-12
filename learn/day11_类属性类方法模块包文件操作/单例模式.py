#!/usr/bin/python3
# coding = UTF-8
# code by va1id



class play:
    instance = None
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        print('正在分配空间')
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

p = play()
print(id(p))
p1 = play()
print(id(p1))