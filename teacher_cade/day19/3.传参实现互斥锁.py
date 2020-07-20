#!/usr/bin/python3
# coding=utf-8
import threading
import time

g_num = 0


def work1(num, mutex):
    print(id(mutex))
    global g_num
    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work1, g_num is %d---" % g_num)


def work2(num, mutex):
    print(id(mutex))
    global g_num
    for i in range(num):
        # 加1操作不是原子操作
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("----in work2, g_num is %d---" % g_num)


def main():
    print("---线程创建之前g_num is %d---" % g_num)
    mutex = threading.Lock()
    print(id(mutex))
    t1 = threading.Thread(target=work1, args=(1000000, mutex))
    t1.start()

    t2 = threading.Thread(target=work2, args=(1000000, mutex))
    t2.start()

    while len(threading.enumerate()) != 1:
        time.sleep(1)

    print("2个线程对同一个全局变量操作之后的最终结果是:%s" % g_num)


if __name__ == '__main__':
    main()
