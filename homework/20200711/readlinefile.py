#!/usr/bin/python3
# coding = UTF-8
# code by va1id


file = open('readme', mode='r')
while True:
    x = file.readline()
    print(x,end='')
    # 如果中间有一个空行则也含有\n，也可以被读
    if len(x) == 0:
        break
# x = file.readline(8)
# print(x)
file.close()