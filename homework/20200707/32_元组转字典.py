#!/usr/bin/python3
# coding = UTF-8


tuple1 = (1, 2, 3)
tuple2 = ('x', 'y', 'z')
tuple3 = [(tuple2[i], tuple1[i]) for i in range(len(tuple1))]
print(tuple3)
tuple = tuple(tuple3)
print(tuple)