#!/usr/bin/python3
# coding = UTF-8


tuple1 = (2,5,3,7)
print(tuple1)
tuple1 = list(tuple1)
tuple1.insert(2, 9)
tuple1 = tuple(tuple1)
print(tuple1)