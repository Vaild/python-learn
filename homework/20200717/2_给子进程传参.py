#!/usr/bin/python3
# coding = UTF-8
# code by va1id


from multiprocessing import Process
import time
def son(list):
    for i in list:
        print('son process : ', i)
        time.sleep(1)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    p = Process(target=son, args=tuple(list1))
    p.start()
    for i in list1:
        print()
        print('dad process : ', i)
        time.sleep(1)