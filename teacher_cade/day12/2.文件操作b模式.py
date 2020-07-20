#!/usr/bin/python3
# coding=utf-8

# 往文件中写入多少个字节
file = open('readme', 'rb+')
# file.write('我很牛'.encode('utf-8'))
text = file.read()
print(text.decode('utf-8'))
file.close()
