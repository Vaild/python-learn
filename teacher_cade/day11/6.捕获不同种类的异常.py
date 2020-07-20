#!/usr/bin/python3
# coding=utf-8

try:
    num = int(input("请输入整数："))
    result = 8 / num
    print(result)
except ValueError:
    print("请输入正确的整数")
# except ZeroDivisionError:
#     print("除 0 错误")
except Exception as result:
    print("未知错误 %s" % result)
