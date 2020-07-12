#!/usr/bin/python3
# coding = UTF-8


string = 'this is python'
j = 0
for i in range(string.count('is')):
    j = string.index('is',j)
    print(j)
    j = j + 1