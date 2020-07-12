#!/usr/bin/python3
# coding = UTF-8
# code by va1id


# 不可变的数据类型的入参
def simple_practice(num1, num2):
    num1, num2 = num2, num1
    return num1, num2


if __name__ == '__main__':
    a = 2
    b = 3
    a, b = simple_practice(a, b)
    print(a, b)