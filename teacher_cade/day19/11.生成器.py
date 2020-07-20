#!/usr/bin/python3
# coding=utf-8


# G = (x for x in range(5))
# print(G)
#
# print(next(G))
# print(next(G))
# print(next(G))
def fib(n):
    current = 0
    num1, num2 = 0, 1
    while current < n:
        num = num1
        num1, num2 = num2, num1 + num2
        current += 1
        yield num
    return 'done'


F = fib(5)
print(F)
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
print(next(F))
