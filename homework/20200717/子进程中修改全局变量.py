#!/usr/bin/python3
# coding = UTF-8
# code by va1id


# 定义全局变量
import os
import time
from multiprocessing import Process
N= [1, 2]
def change_process():
    print('未修改之前的列表:', N)
    print('列表此时的ID是:', os.getpid())
    for i in range(10):
        N.append(i)
        print('修改之后的列表:', N)
        print('修改之后的ID:', os.getpid())
        time.sleep(1)

def watch_list():
    print('列表是:', N)
    time.sleep(1)


if __name__ == '__main__':
    x = Process(target=change_process)
    y = Process(target=watch_list)

    x.start()
    y.start()

    x.join()
    y.join()

    print('最终的列表是:', N)
    print('最终的ID是:', os.getpid())

# 对于整型数的尝试,发现整型数最后的时候打印出来的ID时发生了变化
N = 1
def change_process():
    global N
    print('未修改之前的列表:', N)
    print('列表此时的ID是:', os.getpid())
    for i in range(10):
        N = i
        print('修改之后的列表:', N)
        print('修改之后的ID:', os.getpid())
        time.sleep(1)

def watch_list():
    print('列表是:', N)
    time.sleep(1)


if __name__ == '__main__':
    x = Process(target=change_process)
    y = Process(target=watch_list)

    x.start()
    y.start()

    x.join()
    y.join()

    print('最终的列表是:', N)
    print('最终的ID是:', os.getpid())
