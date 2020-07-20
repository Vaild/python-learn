#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import threading
import time
NUM = 0
lock = threading.Lock()
# 这里用两个不同的锁对两个不同的线程分别上锁得不到想要的结果
# lock1 = threading.Lock()
def work1(num):
    global NUM
    for i in range(num):
        lock.acquire()
        NUM += 1
        lock.release()
    print(NUM)


def work2(num):
    global NUM
    for i in range(num):
        lock.acquire()
        NUM += 1
        lock.release()
    print(NUM)


if __name__ == '__main__':
    start = time.time()
    x = threading.Thread(target=work1, args=(1000000, ))
    x.start()
    y = threading.Thread(target=work2, args=(1000000, ))
    y.start()
    x.join()
    y.join()
    end = time.time()
    print(NUM)
    print('共用时间：%d s' % (end - start))