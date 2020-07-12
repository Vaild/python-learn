#!/usr/bin/python3
# coding = UTF-8
# i = 1
# while i <= 13:
#     if i < 4:
#         print('{}')
num = int(input('请输入你要输入的图形的大小：'))
for i in range(2, num+1):
    if i < num:
        print(' ' * (num - i), '* ' * i, ' '*(2*(num-i-1)), '* '*i)
    else:
        print('', '* '*2*num)
i = 2*num-1
while i > 0:
    print(' ' * (2*num - i), '* ' * i)
    i -= 1