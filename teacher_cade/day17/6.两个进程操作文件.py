#!/usr/bin/python3
# coding=utf-8
from multiprocessing import Process
from time import sleep


def run_proc(file):
    sleep(1)
    text = file.read(5)
    print('I am child %s' % text)


# 创建子进程，不能够传file文件对象
if __name__ == '__main__':
    file = open('readme', mode='r+', encoding='utf-8')
    p = Process(target=run_proc, args=(file,))
    p.start()
    text = file.read(5)
    print('I am parent %s' % text)
    p.join()
