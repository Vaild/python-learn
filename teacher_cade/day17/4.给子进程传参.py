#!/usr/bin/python3
# coding=utf-8
from multiprocessing import Process
import os
from time import sleep


def run_proc(name, age, **kwargs):
    for i in range(10):
        print('子进程运行中，name= %s,age=%d ,pid=%d...' % (name, age, os.getpid()))
        print(kwargs)
        sleep(0.2)


if __name__ == '__main__':
    p_dict = {"m": 20}
    p = Process(target=run_proc, args=('熊大', 18), kwargs=p_dict)
    p.start()
    sleep(1)  # 1秒中之后，立即结束子进程
    p_dict['m'] = 30
    print(p_dict)
    # p.terminate()
    p.join()
