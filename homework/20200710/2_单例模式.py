#!/usr/bin/python3
# coding = UTF-8
# code by va1id


class Player:
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


p1 = Player()
print(id(p1))
p2 = Player()
print(id(p1))