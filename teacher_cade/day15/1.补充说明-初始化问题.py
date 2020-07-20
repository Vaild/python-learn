#!/usr/bin/python3
# coding=utf-8
# l = [[0, 0], [0, 0], [0, 0]]
l = [[0, 0] for i in range(3)]
# for i in range(3):
#     l.append([0, 0])
print(l)
print(l[0])
print(l[0][1])
# [[0,1],[0,0],[0,0]]
l[0][1] = 1
print(l)
print('-' * 50)
l = [0] * 5
l[0] = 1
print(l)
