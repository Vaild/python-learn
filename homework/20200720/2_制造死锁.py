#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import threading
import time
lock1 = threading.Lock()
lock2 = threading.Lock()
def test1():
    lock1.acquire()
    print(1)
    time.sleep(1)
    lock2.acquire()
    print(2)
    time.sleep(1)
    lock2.release()
    lock1.release()

def test2():
    lock2.acquire()
    print(1)
    time.sleep(1)
    lock1.acquire()
    print(2)
    time.sleep(1)
    lock1.release()
    lock2.release()

if __name__ == '__main__':
    x = threading.Thread(target=test1)
    y = threading.Thread(target=test2)
    x.start()
    y.start()