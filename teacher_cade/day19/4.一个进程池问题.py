#!/usr/bin/python3
# coding=utf-8
from multiprocessing import Manager, Pool
import os, time


def reader(q):
    print('reader 启动(%s),父进程(%s)' % (os.getpid(), os.getppid()))
    print('read(%s) %d from queue' % (os.getpid(), q.get(True)))
    print('reader 结束(%s),父进程(%s)' % (os.getpid(), os.getppid()))


def write(q):
    print('writer 启动(%s),父进程(%s)' % (os.getpid(), os.getppid()))
    for i in range(5):
        q.put(i)
        print('writter put %d in queue' % i)
    print('writer 结束(%s),父进程(%s)' % (os.getpid(), os.getppid()))


if __name__ == '__main__':
    print('(%s) start' % os.getpid())
    q = Manager().Queue()
    p2 = Pool()
    p2.apply_async(write, (q,))
    time.sleep(1)
    while True:
        if not q.empty():
            p2.apply_async(reader, (q,))
        else:
            break
    p2.close()
    p2.join()
    print('(%s) end' % os.getpid())
