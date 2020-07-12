#!/usr/bin/python3
# coding = UTF-8


# def return_ascii(alnum):
#     return ord(alnum)
#
#
# alnum = input('输入一个字符：')
# print(return_ascii(alnum))

def ascii_value(str):
    for i in str:
        print('字符是{}， ASCII码为{}'.format(i, ord(i)))


if __name__ == '__main__':
    string = input('输入要转换的字符：')
    ascii_value(string)