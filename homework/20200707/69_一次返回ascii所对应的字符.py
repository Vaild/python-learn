#!/usr/bin/python3
# coding = UTF-8


def ascii_char(num):
    return chr(num)


if __name__ == '__main__':
    num = int(input('输入ASCII码：'))
    print('ASCII码为%d所对应的字符是：' %num, ascii_char(num))