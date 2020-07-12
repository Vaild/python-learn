#!/usr/bin/python3
# coding = UTF-8


str1 = 'Hello, 我是David'
str2 = 'OK, 好'
str3 = '很高兴认识你'
n = max(len(str1), len(str2),len(str3))

print(str1.ljust(n))
print(str2.ljust(n))
print(str3.ljust(n))
print('*'*50)
print(str1.rjust(n))
print(str2.rjust(n))
print(str3.rjust(n))
print('*'*50)
print(str1.center(n))
print(str2.center(n))
print(str3.center(n))