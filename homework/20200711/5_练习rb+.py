#!/usr/bin/python3
# coding = UTF-8
# code by va1id

# 创建文件
# file = open('rb', mode='a')
# for i in range(10):
#     file.write('test{}\n'.format(i))
# file.close()

file = open('rb', mode='r+')
x = file.read()
print(x)
file.close()

file = open('rb', mode='a+')
file.write('\n人生苦短')
file.close()

file = open('rb', mode='rb+')
x = file.read()
print(x)
file.close()