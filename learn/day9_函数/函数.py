#!/usr/bin/python3
# coding = UTF-8


a = 6
b = 7
a, b = b, a
print(a, b)

a ^= b
b ^= a
a ^= b
print(a, b)

