#!/usr/bin/python3
# coding = UTF-8
# code by va1id


from greenlet import greenlet
import time
def work1():
    while True:
        print('1')
        y.switch()
        z.switch()
        time.sleep(1)

def work2():
    while True:
        print('2')
        x.switch()
        z.switch()
        # time.sleep(1)

def work3():
    while True:
        print(3)
        x.switch()
        y.switch()
        # time.sleep(1)


x = greenlet(work1)
y = greenlet(work2)
z = greenlet(work3)
x.switch()

