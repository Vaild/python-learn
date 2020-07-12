#!/usr/bin/python3
# coding = UTF-8
num = int(input('请输入你要输入的图形的大小：'))
for i in range(1, 2*num):
    if i <= num:
        if i == 1:
            print(' '*(num - i), '*')
        else:
            print(' '*(num - i), '*{}*'.format(' '*(2*(i-1)-1)))
    else:
        if i < 2*num-1:
            print(' '*(i - num), '*{}*'.format(' '*(2*(2*num-i-1)-1)))
        else:
            print(' ' * (i - num), '*')
