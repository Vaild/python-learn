#!/usr/bin/python3
# coding=utf-8
from gevent import monkey
import gevent
import random
import time


def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name, i)
        time.sleep(1)


g_list = []
for i in range(2):
    g_list.append(gevent.spawn(coroutine_work, "work" + str(i + 1)), )

gevent.joinall(g_list)
