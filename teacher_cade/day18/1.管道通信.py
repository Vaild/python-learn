#!/usr/bin/python3
# coding=utf-8
import multiprocessing

conn1, conn2 = multiprocessing.Pipe(duplex=False)

conn2.send('hello')
conn2.send('world')
text = conn1.recv()
print(text)
text = conn1.recv()
print(text)
