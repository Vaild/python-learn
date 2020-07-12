#!/usr/bin/python3
# coding = UTF-8


list = ['15', '127', '65535']
n = max(len(list[0]), len(list[1]), len(list[2]))
for i in list:
    print(i.zfill(n))
