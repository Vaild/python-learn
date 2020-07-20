#!/usr/bin/python3
# coding = UTF-8
# code by va1id


import gevent
import time
def test1(name):
    print('test1a, %s' % name)
    # time.sleep(1)
    # 在这等待的时候会跳转到下一个协程，等从另一个协程跳转回来的时候还从这里开始
    # 但是如果用time.sleep怎不会完成自动的协程间的跳转
    gevent.sleep(1)
    print('test1b, %s' % name)
    print('test1b, %s' % name)

def test2(name):
    print('test2a, %s' % name)
    # time.sleep(1)
    gevent.sleep(1)
    print('test2b, %s' % name)
    print('test2b, %s' % name)

x = gevent.spawn(test1, 'wb')
y = gevent.spawn(test1, 'rb')
x.join()
y.join()