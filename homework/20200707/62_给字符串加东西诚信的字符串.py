#!/usr/bin/python3
# coding = UTF-8


string = 'abc'
n = len(string)
str = ''
for i in range(0,n-1):
    str = str + string[i] + ','
str = str + string[n-1]
print(str)