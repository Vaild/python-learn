#!/usr/bin/python3
# coding = UTF-8

import unerline
a = 10
print(id(a))
a = 8
print(id(a))
print(id(a-1))
a1 = a - 1
print(id(a1))
a2 = a - 2
print(id(a2))  # 减一对应id减小16
unerline.dl()

for i in range(-10, 260):
    print(id(i))

unerline.dl()

b = True
print(id(b))
b = False
print(id(b))

unerline.dl()

c = 10.0
print(id(c))
print(id(c - 1.0))
c1 = c - 1
print(id(c1))

unerline.dl()

d = 'abc'
print(id(d))
d = 'ab'
print(id(d))

unerline.dl()

e = (1, 3, 4, 5)
print(e[0])
# e[0] = 2  错，不能修改
print(id(e))


unerline.dl()

list = [1, 2, 3, 4]
print(id(list))
for i in range(len(list)):
    print(id(list[i]))
list[0] = 5
print(id(list))
for i in range(len(list)):
    print(id(list[i]))

unerline.dl()


f = {"name": "wb", 'age': 18, 'sex': 'male'}
print(id(f))
f['name'] = 'yx'
print(id(f))