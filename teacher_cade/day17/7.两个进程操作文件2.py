#!/usr/bin/python3
# coding=utf-8
from multiprocessing import Process
from time import sleep


def run_proc(filename):
    sleep(1)
    file = open(filename, mode='r+', encoding='utf-8')
    text = file.read(5)
    print('I am child %s' % text)


# 创建子进程，不能够传file文件对象
if __name__ == '__main__':
    file = open('readme', mode='r+', encoding='utf-8')
    p = Process(target=run_proc, args=("readme",))
    p.start()
    file.write('HELLO')
    sleep(10)
    file.close()
    p.join()
