#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import threading
import time
NUM = 0
def add1():
    global NUM
    for i in range(10000000):
        NUM += 1


def add2():
    global NUM
    for i in range(10000000):
        NUM += 1

if __name__ == '__main__':
    x = threading.Thread(target=add1)
    x.start()
    print(NUM)
    y = threading.Thread(target=add2)
    y.start()
    print(NUM)
    x.join()
    y.join()
    print(NUM)