#!/usr/bin/python3
# coding = UTF-8
# code by va1id


file = open('readme', mode='r')
# 从开头开始偏移
file.seek(5, 0)
x = file.read()
print(x)
file.close()