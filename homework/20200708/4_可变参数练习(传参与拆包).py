#!/usr/bin/python3
# coding = UTF-8
# code by va1id

def Unpackage(name=None, title = None):
    print(name, title)


def Unpack(*args, **kwargs):
    print(args)
    print(*args)
    print(kwargs)
    Unpackage(**kwargs)



Unpack(2,3,4,name='wangdao', title='tql')