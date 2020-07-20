#!/usr/bin/python3
# coding=utf-8
# 1. 打开 - 文件名需要注意大小写
file = open("README", encoding='utf-8')

# 2. 读取
text = file.read()
print(text)

# 3. 关闭
file.close()
