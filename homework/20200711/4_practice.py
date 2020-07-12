#!/usr/bin/python3
# coding = UTF-8
# code by va1id

# a+ 如果存在则将光标放到最后再写，如果不存在则创建新的再进行写入
# r+ 如果存在则进行覆盖，不写的话则不进行覆盖，如果不存在则报错
# w+ 如果存在则进行覆盖，即使不想其中写入任何的东西也会被空白文件覆盖，如果不存在则创建新的文件
file = open('readme',mode='a+')
file.write('\ntest')
x = file.read()
print(x)
file.close()

print('-'*100)

file = open('readme',mode='r+')
# file.write('\ntest')
x = file.read()
print(x)
file.close()

print('-'*100)

file = open('readme',mode='r+')
file.write('\ntest')
x = file.read()
print(x)
file.close()

print('-'*100)

file = open('readme',mode='w+')
x = file.read()
print(x)
file.close()

print('-'*100)

file = open('readme',mode='w+')
file.write('\ntest')
x = file.read()
print(x)
file.close()

# 在测试完之后，发现在w+和a+模式下并不能将其中的内容读取出来=====不知道是不是我的问题