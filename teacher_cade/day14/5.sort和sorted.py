#!/usr/bin/python3
# coding=utf-8

arr = [5, 2, 3, 1, 4]
# print(sorted(arr))
arr.sort()
print(arr)

print(sorted({1: 'D', 3: 'B', 2: 'B', 4: 'E', 5: 'A'}))

print(sorted("This is a test string from Andrew".split(), key=str.lower))

student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


def select(student):
    return student[2]


print(sorted(student_tuples, key=select))

print(sorted(student_tuples, key=lambda student: student[2]))
