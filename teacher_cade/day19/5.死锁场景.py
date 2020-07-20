#!/usr/bin/python3
# coding=utf-8
# 单个线程加锁两次
import threading

mutex = threading.Lock()

mutex.acquire()
mutex.acquire()

print('you can see me?')
