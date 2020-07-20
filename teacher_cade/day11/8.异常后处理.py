#!/usr/bin/python3
# coding=utf-8

flag = True
while flag:
    # try流程中某一句异常，不会再执行该语句后的代码，try代码块后代码可以得到执行
    try:
        num = int(input("请输入整数："))
        result = 8 / num
        print(result)
    except ValueError:
        print("请输入正确的整数")
    except ZeroDivisionError:
        print("除 0 错误")
    else:
        flag = False
