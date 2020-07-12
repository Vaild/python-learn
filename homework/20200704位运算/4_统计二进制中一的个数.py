#!/usr/bin/python3
# coding = UTF-8
def Num_One(n):
    if n >= 0:
        return bin(n).count('1')
    else:
        return bin(n & 0xffffffffffffffff).count('1')


n = int(input('输入数字：'))
m = Num_One(n)
print(m)
