#!/usr/bin/python3
# coding = UTF-8


NUM = 100
def add_num():
    num = 10
    print('NUM = ', NUM)
    sum = NUM + num
    print(sum)

def Add_Num():
    global NUM
    NUM = 90
    num = 30
    sum = NUM + num
    print('NUM = ', NUM)
    print(sum)

print('NUM = ', NUM)
add_num()
Add_Num()
