#!/usr/bin/python3
# coding = UTF-8


def say_hello(num):
    '''
    打印 hello
    :param num: 打印次数
    :return:
    '''
    for i in range(num):
        print("hello!")

n = int(input('输入要打印的次数：'))
say_hello(n)