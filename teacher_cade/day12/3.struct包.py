#!/usr/bin/python3
# coding=utf-8

import struct

a = 20
b = 400
# 转换后的str虽然是字符串类型，但相当于其他语言中的字节流（字节数组），
# 可以在网络上传输
str = struct.pack("ii", a, b)
print('length:', len(str))
print(str)
