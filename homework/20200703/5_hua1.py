#!/usr/bin/python3
# coding = UTF-8
# num = int(input('请您输入图形大小：'))
# for i in range(1, 2*num):
#     if i <= num:
#         print('*' * i)
#     else:
#         print('*' * (i - 2 * (i - num)))

num = int(input('请输入你要输入的图形的大小：'))
for i in range(1, 2*num):
    if i <= num:
        print(' ' * (num - i), '* ' * i)
    else:
        print(' ' * (i-num), '* ' * (i-2*(i-num)))
