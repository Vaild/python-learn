#!/usr/bin/python3
# coding=utf-8

a, b = 3, 5
print(a, b)


def test_return():
    return 1, 3


c, d = test_return()
print(c, d)


def demo(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
    print(type(args))
    print(type(kwargs))


demo((1, 2), (3, {"name": 'laowang'}), 5, name="小明", age=18, gender=True)
