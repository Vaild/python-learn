#!/usr/bin/python3
# coding=utf-8

# 1. 打开
file = open("README", "w+")
print(type(file))
# 2. 写入文件
file.write("123 hello")
file.seek(0, 0)
# python只能偏移到末尾
file.seek(0, 1)
text = file.read()
print(text)
# 3. 关闭
file.close()
