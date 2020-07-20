#!/usr/bin/python3
# coding=utf-8

# 求n的阶乘  f(n)=n*f(n-1)
# 要写结束条件
def f(n):
    if n == 1:
        return 1
    return n * f(n - 1)


print(f(5))

# n个台阶，1个台阶，2个台阶，请问上n台阶有多少种走法
# f(n)=f(n-1)+f(n-2)
