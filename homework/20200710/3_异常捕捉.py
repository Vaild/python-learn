#!/usr/bin/python3
# coding = UTF-8
# code by va1id


flag = True
while flag:
    try:
        num = int(input('请输入一个整型数：'))
        num = str(num)
        n = len(num)
        for i in range(n // 2):
            if num[i] == num[-1-i]:
                pass
            else:
                print('不是对称数。')
                flag = False
                break
        else:
            print('这是一个对称数。')
            flag = False
    except:
        print('输入的不是整型数，请重新输入。')