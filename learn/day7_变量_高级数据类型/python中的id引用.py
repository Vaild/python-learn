#!/usr/bin/python3
# coding = UTF-8


num = 100
print(id(num))
num = 1
print(id(num))
print(id(num-1))
print(id(num-1))
n = num - 1
print(id(n))
m = n + 1
print(id(m))
print(id(num))
print(type(id(num)))
mn = num + 99
print(id(mn))
b = 100
print(id(b))



print('*' * 100)
int1 = 1
float1 = 12.0
str1 = 'str'
list1 = [1, 2, 3, 4, 'str']
tuple1 = (1, 2, 3, 4)
print(id(int1))
print(id(float1))
print(id(str1))
print(id(list1))
print(id(list1[0]))
print(id(list1[1]))
print(id(list1[2]))
print(id(tuple1))
print(id(tuple1[0]))
print(id(tuple1[1]))