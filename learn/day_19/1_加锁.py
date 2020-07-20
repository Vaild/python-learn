#!/usr/bin/python3
# coding = UTF-8
# code by va1id

import threading
import time
NUM = 0
lock1 = threading.Lock()
lock2 = threading.Lock()
def work1(num):
    global NUM
    for i in range(num):
        lock1.acquire()
        NUM += 1
        lock1.release()
    print(NUM)

def work2(num):
    global NUM
    for i in range(num):
        lock1.acquire()
        NUM += 1
        lock1.release()
    print(NUM)

if __name__ == '__main__':
    x = threading.Thread(target=work1, args=(1000000, ))
    x.start()
    y = threading.Thread(target=work2, args=(1000000, ))
    y.start()
    x.join()
    y.join()
    while len(threading.enumerate()) != 1:
        print(NUM)